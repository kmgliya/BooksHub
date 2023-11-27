from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # И этот импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include("forum.urls")),
    path("", include("books.urls"))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
