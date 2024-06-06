from django.urls import path
from .views import ChargebackCreateView,AssignChargebackView,  ChargebackListView, ChargebackDetailView, ChargebackUpdateView, ChargebackCreateView
from .views import  ChargebackStatusUpdateView,ChargebackLogsView
from .views import ChargebackLogsView ,download_file

from .views import ToggleActiveStatus,PredictResolutionTimeView
# urls.py
from django.urls import path
from .views import FileDetailView

from .views import download_file
# urls.py
from django.urls import path
# from .views import send_email_to_merchant

# urls.py

from .views import AssignChargebackView,ChargebacksByStatusView,ChargebackDataView


from django.urls import path
from .views import (
    CommentListView,
    CommentDetailView,
    CommentLikeView,
    CommentDislikeView,
    CommentReplyView
)

from django.urls import path
from django.urls import path





from django.urls import path
from .views import FileUploadView, FileDetailView, delete_file, download_file

urlpatterns = [
    path('chargebacks/<int:pk>/upload-file/', FileUploadView.as_view(), name='chargeback-file-upload'),
    path('files/<int:pk>/delete/', delete_file, name='delete-file'),
    path('files/download/<int:file_id>/', download_file, name='file-download'),
    path('chargebacks/<int:chargeback_id>/files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),



    path('chargebacks/<int:chargeback_id>/comments/', CommentListView.as_view(), name='chargeback-comments'),
    path('comments/<int:comment_id>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comments/<int:comment_id>/like/', CommentLikeView.as_view(), name='comment-like'),
    path('comments/<int:comment_id>/dislike/', CommentDislikeView.as_view(), name='comment-dislike'),
    path('comments/<int:comment_id>/reply/', CommentReplyView.as_view(), name='comment-reply'),

    path('chargebacks/status/', ChargebacksByStatusView.as_view(), name='chargebacks-by-status'),


    
     path('chargebacks/<int:pk>/assign/', AssignChargebackView.as_view(), name='assign-chargeback'),
    path('chargebacks/<int:chargeback_id>/ac_des/', ToggleActiveStatus.as_view(), name='toggle-chargeback-active'),
    # path('chargebacks/<int:chargeback_id>/send-email/', send_email_to_merchant, name='send-email-to-merchant'),
    path('chargebacks/predict_resolution_time/', PredictResolutionTimeView.as_view(), name='predict-resolution-time'),





    path('chargebacks/', ChargebackCreateView.as_view(), name='chargeback-create'),
    path('chargebacks/<int:pk>/assign/', AssignChargebackView.as_view(), name='assign-chargeback'),
    path('chargebacks/<int:pk>/update-status/',  ChargebackStatusUpdateView.as_view(), name='update-chargeback-status'),
    path('files/download/<int:file_id>/', download_file, name='file-download'),

path('chargebacks/list/', ChargebackListView.as_view(), name='chargeback-list'),
    path('chargebacks/<int:pk>/edit/', ChargebackUpdateView.as_view(), name='chargeback-update'),
    path('chargebacks/data/', ChargebackDataView.as_view(), name='chargeback-data'),


    path('chargebacks/<int:pk>/', ChargebackDetailView.as_view(), name='chargeback-detail'),


    path('chargebacks/<int:chargeback_id>/files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),







    path('chargebacks/<int:pk>/logs/', ChargebackLogsView.as_view(), name='chargeback-logs'),


]


