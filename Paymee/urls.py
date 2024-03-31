from django.contrib import admin
from django.urls import path, include

# Dans Paymee.urls


# urls.py à la racine du projet
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Assurez-vous que ceci correspond à l'emplacement de votre fichier urls.py de l'application
]
