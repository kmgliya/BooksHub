from django.http import HttpResponseRedirect
from django.urls import reverse
from axes.models import AccessLog, AccessAttempt

class AxesLoginRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Проверяем, была ли блокировка для текущего пользователя
        if request.user.is_authenticated:
            access_logs = AccessLog.objects.filter(username=request.user.username, path_info='accounts/login/')

            if access_logs.exists():
                last_log = access_logs.latest('attempt_time')
                cool_off_remaining = last_log.get_cooloff_time_remaining()

                if cool_off_remaining == 0:
                    return HttpResponseRedirect(reverse('accounts:login'))

        return response
