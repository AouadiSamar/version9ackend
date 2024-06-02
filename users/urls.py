from django.urls import path
from . import views
from .views import ResetPasswordConfirm, SendResetEmailView, ProfileView,UserView,UserListView, PermissionListView ,UserDetailView, UserCreateView, UserUpdateView, RoleCreateView,RoleListView

from django.urls import path
from .views import login_with_2fa, verify_2fa

from .views import ToggleUserActiveStatus

urlpatterns = [





    path('login/2fa/', login_with_2fa, name='login_with_2fa'),
    path('login/verify/', verify_2fa, name='verify_2fa'),
    # Ajoutez d'autres chemins d'URL ici

    
    path('active-sessions/', views.active_sessions, name='active_sessions'),
    path('send-reset-email/', SendResetEmailView.as_view(), name='send_reset_email'),

    path('terminate-session/<str:session_key>/', views.terminate_session, name='terminate_session'),

    path('profile/update', ProfileView, name='profile'),

    path('', UserView.as_view(), name='users'),
    path('reset-password-confirm/', ResetPasswordConfirm.as_view(), name='reset_password_confirm'),

    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),

    path('<int:user_id>/toggle-active/', ToggleUserActiveStatus.as_view(), name='toggle-user-active'),

    path('permissions/', PermissionListView.as_view(), name='permission-list'),
    path('usersc/', UserCreateView.as_view(), name='user-create'),



    path('profile/', UserDetailView.as_view(), name='user-profile'),

    path('users/', UserListView.as_view(), name='user-list'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('roles/', RoleListView.as_view(), name='role-list'),


    path('rolesc/', RoleCreateView.as_view(), name='role-crer'),]

