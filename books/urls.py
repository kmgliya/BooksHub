from django.urls import path
from .views import hello
from .views import books
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", books),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)