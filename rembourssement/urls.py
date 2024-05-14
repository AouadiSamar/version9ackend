from django.urls import path
from .views import RembourssementCreateView,AssignRembourssementView, CommentView,RembourssementListView,RembourssementDetailView,RembourssementUpdateView,RembourssementCreateView,RembourssementDeleteView
from .views import  RembourssementStatusUpdateView,RembourssementLogsView
from .views import RembourssementLogsView 
from .views import CancelRembourssementView, ReactivateRembourssementView


# urls.py
from django.urls import path
from .views import FileUploadView, FileDetailView


from django.urls import path

urlpatterns = [
    path('rembourssement/',RembourssementCreateView.as_view(), name='rembourssement-create'),
    path('rembourssement/<int:rembourssement_id>/comments', CommentView.as_view(), name='rembourssement-comments'),
    path('rembourssement/<int:pk>/assign/', AssignRembourssementView.as_view(), name='assign-rembourssement'),
    path('rembourssement/<int:pk>/update-status/', RembourssementStatusUpdateView.as_view(), name='update-rembourssement-status'),

    path('rembourssement/list/',RembourssementListView.as_view(), name='rembourssement-list'),
    path('rembourssement/<int:pk>/edit/',RembourssementUpdateView.as_view(), name='rembourssement-update'),
    path('rembourssement/delete/<int:pk>/',RembourssementDeleteView.as_view(), name='rembourssement-delete'),


    path('rembourssement/<int:pk>/',RembourssementDetailView.as_view(), name='rembourssement-detail'),


    path('rembourssement/<int:rembourssement_id>/files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),


    path('rembourssement/<int:pk>/cancel/', CancelRembourssementView.as_view(), name='cancel-rembourssement'),
    path('rembourssement/<int:pk>/reactivate/', ReactivateRembourssementView.as_view(), name='reactivate-rembourssement'),




        path('rembourssement/<int:pk>/upload-file/', FileUploadView.as_view(), name='rembourssement-file-upload'),

    path('rembourssement/<int:pk>/logs/',RembourssementLogsView.as_view(), name='rembourssement-logs'),


]


