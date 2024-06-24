from django.urls import path
from .views import RembourssementCreateView,AssignRembourssementView,RembourssementListView,RembourssementDetailView,RembourssementUpdateView,RembourssementCreateView,RembourssementDeleteView
from .views import  RembourssementStatusUpdateView,RembourssementLogsView
from .views import RembourssementLogsView 
from .views import CancelRembourssementView, ReactivateRembourssementView,ToggleActiveStatus,rembourssement_data
from django.urls import path
from .views import (
    FileUploadView, FileCreateView, FileListView, FileDetailView
)


# urls.py
from django.urls import path

from .views import (
    RembourssementCommentView,download_file,  RembourssementCommentListView,
    RembourssementCommentDetailView, RembourssementCommentLikeView,
)

from django.urls import path

urlpatterns = [


    path('rembourssement/comments/<int:comment_id>/', RembourssementCommentDetailView.as_view(), name='comment-detail'),

    path('rembourssement/<int:rembourssement_id>/comments/', RembourssementCommentView.as_view(), name='rembourssement-comments'),
    path('rembourssement/<int:rembourssement_id>/comments/list/', RembourssementCommentListView.as_view(), name='rembourssement-comments-list'),
    path('rembourssement/comments/<int:comment_id>/', RembourssementCommentDetailView.as_view(), name='rembourssement-comment-detail'),
    path('comments/<int:comment_id>/lik/', RembourssementCommentLikeView.as_view(), name='rembourssement-comment-like'),


    path('rembourssement/',RembourssementCreateView.as_view(), name='rembourssement-create'),
    path('rembourssement/<int:pk>/assign/', AssignRembourssementView.as_view(), name='assign-rembourssement'),
    path('rembourssement/<int:pk>/update-status/', RembourssementStatusUpdateView.as_view(), name='update-rembourssement-status'),

    path('rembourssement/list/',RembourssementListView.as_view(), name='rembourssement-list'),
    path('rembourssement/delete/<int:pk>/',RembourssementDeleteView.as_view(), name='rembourssement-delete'),


    path('rembourssement/<int:pk>/',RembourssementDetailView.as_view(), name='rembourssement-detail'),


    path('rembourssement/create/', RembourssementCreateView.as_view(), name='rembourssement-create'),
    path('rembourssement/<int:id>/', RembourssementDetailView.as_view(), name='rembourssement-detail'),
    path('rembourssement/<int:pk>/update/', RembourssementUpdateView.as_view(), name='rembourssement-update'),




    path('rembourssement/<int:pk>/cancel/', CancelRembourssementView.as_view(), name='cancel-rembourssement'),
    path('rembourssement/<int:pk>/reactivate/', ReactivateRembourssementView.as_view(), name='reactivate-rembourssement'),


    path('rembourssement/<int:rembourssement_id>/ac_des/', ToggleActiveStatus.as_view(), name='toggle-rembourssement-active'),

    path('rembourssement/data/', rembourssement_data, name='rembourssement-data'),

    path('rembourssement/<int:pk>/upload/', FileUploadView.as_view(), name='rembourssement-file-upload'),
    path('files/create/', FileCreateView.as_view(), name='file-create'),
    path('files/', FileListView.as_view(), name='file-list'),
    path('files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),

    path('files/<int:file_id>/download/', download_file, name='file-download'),


    path('rembourssement/<int:pk>/logs/',RembourssementLogsView.as_view(), name='rembourssement-logs'),


]


