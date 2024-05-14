from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Import settings to access DEBUG and file serving settings
from django.conf.urls.static import static  # Helper function for serving files in development

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/', include('chargebacks.urls')),
    path('api/v1/', include('rembourssement.urls')),  # Ensure correct spelling if different
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


