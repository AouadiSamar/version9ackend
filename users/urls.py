from django.urls import path
from . import views
from .views import ProfileView,UserView

urlpatterns = [
    # URL pour la vue qui liste les sessions actives
    path('active-sessions/', views.active_sessions, name='active_sessions'),

    # URL pour la vue qui permet de terminer une session spécifique
    path('terminate-session/<str:session_key>/', views.terminate_session, name='terminate_session'),

    # URL pour la vue qui permet de mettre à jour le profil de l'utilisateur
    path('api/profile/update', ProfileView.as_view(), name='profile'),

    path('api/users/', UserView.as_view(), name='users'),

]
