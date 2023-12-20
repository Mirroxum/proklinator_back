from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', include('posts.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
