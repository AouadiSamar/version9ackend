from django.urls import path
from .views import ChargebackCreateView,AssignChargebackView, CommentView, ChargebackListView, ChargebackDetailView, ChargebackUpdateView, ChargebackCreateView
from .views import  ChargebackStatusUpdateView,ChargebackLogsView
from .views import ChargebackLogsView ,delete_file,download_file

from .views import ToggleActiveStatus

# urls.py
from django.urls import path
from .views import FileUploadView, FileDetailView

from .views import download_file
# urls.py
from django.urls import path
# from .views import send_email_to_merchant


from django.urls import path
urlpatterns = [   
     path('chargebacks/<int:pk>/ac_des/', ToggleActiveStatus.as_view(), name='toggle-active-status'),
    # path('chargebacks/<int:chargeback_id>/send-email/', send_email_to_merchant, name='send-email-to-merchant'),


    path('chargebacks/', ChargebackCreateView.as_view(), name='chargeback-create'),
    path('chargebacks/<int:chargeback_id>/comments', CommentView.as_view(), name='chargeback-comments'),
    path('chargebacks/<int:pk>/assign/', AssignChargebackView.as_view(), name='assign-chargeback'),
    path('chargebacks/<int:pk>/update-status/',  ChargebackStatusUpdateView.as_view(), name='update-chargeback-status'),
    path('files/download/<int:file_id>/', download_file, name='file-download'),

    path('chargebacks/list/', ChargebackListView.as_view(), name='chargeback-list'),
    path('chargebacks/<int:pk>/edit/', ChargebackUpdateView.as_view(), name='chargeback-update'),
    path('files/<int:pk>/delete/', delete_file, name='delete-file'),


    path('chargebacks/<int:pk>/', ChargebackDetailView.as_view(), name='chargeback-detail'),


    path('chargebacks/<int:chargeback_id>/files/<int:file_id>/', FileDetailView.as_view(), name='file-detail'),






        path('chargebacks/<int:pk>/upload-file/', FileUploadView.as_view(), name='chargeback-file-upload'),

    path('chargebacks/<int:pk>/logs/', ChargebackLogsView.as_view(), name='chargeback-logs'),


]


