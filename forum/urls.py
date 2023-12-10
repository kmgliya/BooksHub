from django.urls import path
from .views import bye
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path("", bye),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
