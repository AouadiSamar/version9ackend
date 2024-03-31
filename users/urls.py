from django.urls import path
from . import views
from .views import ProfileView,UserView,UserListView, PermissionListView ,UserDetailView, UserCreateView, UserUpdateView, RoleCreateView,RoleListView,UserDeleteView,ToggleUserActiveStatus


urlpatterns = [
    # URL pour la vue qui liste les sessions actives
    path('active-sessions/', views.active_sessions, name='active_sessions'),

    # URL pour la vue qui permet de terminer une session spécifique
    path('terminate-session/<str:session_key>/', views.terminate_session, name='terminate_session'),

    # URL pour la vue qui permet de mettre à jour le profil de l'utilisateur
    path('profile/update', ProfileView.as_view(), name='profile'),

    path('', UserView.as_view(), name='users'),

    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
# Dans urls.py
    path('usersd/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('users/<int:user_id>/toggle_active/', ToggleUserActiveStatus.as_view(), name='toggle_user_active'),
    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('usersc/', UserCreateView.as_view(), name='user-create'),




    path('users/', UserListView.as_view(), name='user-list'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('roles/', RoleListView.as_view(), name='role-list'),


    path('rolesc/', RoleCreateView.as_view(), name='role-crer'),]
