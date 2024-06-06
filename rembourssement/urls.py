from django.urls import path
from .views import (
    RembourssementUpdateView,  RembourssementDeleteView, RembourssementListView, 
    RembourssementDetailView,  RembourssementStatusUpdateView, RembourssementLogsView, 
    RembourssementCreateView, ToggleActiveStatus, AssignRembourssementView, FileUploadView, 
    delete_file, download_file, FileDetailView, RembourssementDataView
)


from .views import (
    CommentListView,
    CommentDetailView,
    CommentLikeView,
    CommentDislikeView,
    CommentReplyView)
urlpatterns = [
    path('rembourssements/', RembourssementListView.as_view(), name='rembourssement-list'),
    path('rembourssements/create/', RembourssementCreateView.as_view(), name='rembourssement-create'),
    path('rembourssements/<int:pk>/', RembourssementDetailView.as_view(), name='rembourssement-detail'),
    path('rembourssements/<int:pk>/update/', RembourssementUpdateView.as_view(), name='rembourssement-update'),
    path('rembourssements/<int:pk>/delete/', RembourssementDeleteView.as_view(), name='rembourssement-delete'),
    path('rembourssements/<int:pk>/status/', RembourssementStatusUpdateView.as_view(), name='rembourssement-status-update'),
    path('rembourssements/<int:pk>/logs/', RembourssementLogsView.as_view(), name='rembourssement-logs'),
    path('rembourssements/<int:pk>/assign/', AssignRembourssementView.as_view(), name='assign-rembourssement'),
    path('rembourssements/<int:pk>/files/upload/', FileUploadView.as_view(), name='file-upload'),
    path('rembourssements/files/<int:pk>/delete/', delete_file, name='file-delete'),
    path('files/<int:file_id>/download/', download_file, name='file-download'),
    path('rembourssements/<int:rembourssement_id>/files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),
    path('rembourssements/<int:rembourssement_id>/toggle-active/', ToggleActiveStatus.as_view(), name='toggle-active-status'),

    path('rembourssements/data/', RembourssementDataView.as_view(), name='rembourssement-data'),




    path('rembourssements/<int:rembourssement_id>/comments/', CommentListView.as_view(), name='rembourssement-comments'),
    path('rembourssements/comments/<int:comment_id>/', CommentDetailView.as_view(), name='rembourssement-comment-detail'),
    path('rembourssements/comments/<int:comment_id>/like/', CommentLikeView.as_view(), name='rembourssement-comment-like'),
    path('rembourssements/comments/<int:comment_id>/dislike/', CommentDislikeView.as_view(), name='rembourssement-comment-dislike'),
    path('rembourssements/comments/<int:comment_id>/reply/', CommentReplyView.as_view(), name='rembourssement-comment-reply'),

    
    
    
    
    
    ]