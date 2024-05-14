from django.shortcuts import render
from .models import Chargeback,Comment
from .serializers import ChargebackSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChargebackSerializer
from .models import Chargeback


from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Chargeback
from rest_framework.permissions import IsAuthenticated

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from django.utils.dateparse import parse_date
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chargeback
from .serializers import ChargebackSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Comment




# views.py
from rest_framework import status
from rest_framework.response import Response
from .models import Chargeback
from .serializers import ChargebackSerializer

from .serializers import ActionLogSerializer

from .models import ActionLog

import logging
import logging
import logging

from django.http import HttpResponse
from django.core.files import File

from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import File

# views.py in your Django app

# views.py

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Chargeback
from .serializers import ChargebackSerializer


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Chargeback, File
from .serializers import FileSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Chargeback
from .serializers import ChargebackSerializer

# views.py in your Django app
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback, File
from django.shortcuts import get_object_or_404
import logging
import logging



from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
    
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChargebackSerializer
from .models import Chargeback
from .serializers import ChargebackSerializer



from rest_framework import viewsets
from .models import Comment
from .serializers import CommentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback, File
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChargebackSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback
from .serializers import ChargebackSerializer

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback, ActionLog
from .serializers import ActionLogSerializer

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import ActionLog
from .serializers import ActionLogSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File, Chargeback
from .serializers import FileSerializer
from django.shortcuts import get_object_or_404

from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ActionLog, Chargeback
from .serializers import ActionLogSerializer
import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Chargeback
from .serializers import ChargebackSerializer

###CRUDChargebacks
from rest_framework.permissions import IsAuthenticated

from rest_framework import views, status
from rest_framework.response import Response
from .models import Chargeback
from .serializers import ChargebackSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Chargeback
from rest_framework.response import Response
from rest_framework import status
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Chargeback
from .serializers import ChargebackSerializer
from rest_framework.response import Response










import logging
logger = logging.getLogger(__name__)
class ChargebackUpdateView(generics.UpdateAPIView):
    queryset = Chargeback.objects.all()
    serializer_class = ChargebackSerializer



def update(self, request, *args, **kwargs):
    logger.debug(f"Received update data: {request.data}")
    partial = kwargs.pop('partial', True)  # Allowing partial updates
    serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response(serializer.data)

    




class ChargebackDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        chargeback = get_object_or_404(Chargeback, pk=pk)
        chargeback.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ChargebackListView(APIView):
    def get(self, request):
        # Get the date parameter from the query string
        date = request.query_params.get('date', None)
        if date:
            # Parse the string date to a date object
            date_obj = parse_date(date)
            # Filter chargebacks by the parsed date
            chargebacks = Chargeback.objects.filter(creation_date__date=date_obj)
        else:
            chargebacks = Chargeback.objects.all()
        
        serializer = ChargebackSerializer(chargebacks, many=True)
        return Response(serializer.data)




class ChargebackDetailView(APIView):

    def get(self, request, pk):
        try:
            chargeback = Chargeback.objects.get(pk=pk)
            serializer = ChargebackSerializer(chargeback)
            return Response(serializer.data)
        except Chargeback.DoesNotExist:
            return Response({'error': 'Chargeback not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

    def put(self, request, pk):
        try:
            chargeback = Chargeback.objects.get(pk=pk)
            serializer = ChargebackSerializer(chargeback, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Chargeback.DoesNotExist:
            return Response({'error': 'Chargeback not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

    def delete(self, request, pk):
        try:
            chargeback = Chargeback.objects.get(pk=pk)
            chargeback.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Chargeback.DoesNotExist:
            return Response({'error': 'Chargeback not found'}, status=status.HTTP_404_NOT_FOUND)




   



class CommentView(APIView):

    def get(self, request, chargeback_id):
        comments = Comment.objects.filter(chargeback_id=chargeback_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

    def post(self, request, chargeback_id):
        print("Received data:", request.data)
        serializer = CommentSerializer(data=request.data, context={'request': request, 'view': self})
        if serializer.is_valid():
            comment = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
   




    

class AssignChargebackView(APIView):
    def patch(self, request, pk):
        chargeback = Chargeback.objects.get(pk=pk)
        user_id = request.data.get('assigned_to')
        if user_id:
            chargeback.assigned_to_id = user_id
            chargeback.save(update_fields=['assigned_to'])
            return Response({"status": "Chargeback assigned successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)



class ChargebackStatusUpdateView(APIView):
    def patch(self, request, pk):
        chargeback = Chargeback.objects.get(pk=pk)
        serializer = ChargebackSerializer(chargeback, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class ChargebackLogsView(APIView):
    permission_classes = [IsAdminUser]  # This ensures only admin users can access this view

    def get(self, request, pk):
        logs = ActionLog.objects.filter(chargeback__id=pk).order_by('-created_at')
        if not logs.exists():
            return Response({'message': 'No logs found'}, status=404)
        serializer = ActionLogSerializer(logs, many=True)
        return Response(serializer.data)
    
    
class ChargebackCreateView(APIView):
    def get(self, request):
        chargebacks = Chargeback.objects.all()
        serializer = ChargebackSerializer(chargebacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ChargebackSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class FileUploadView(APIView):
    def post(self, request, pk):
        chargeback = get_object_or_404(Chargeback, pk=pk)
        file_serializer = FileSerializer(data=request.data, context={'request': request})
        
        if file_serializer.is_valid():
            file_serializer.save(chargeback=chargeback)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer



class ToggleActiveStatus(APIView):
    """
    API view to toggle the active status of a Chargeback instance.
    """
    def patch(self, request, pk):
        chargeback = get_object_or_404(Chargeback, pk=pk)
        print(f"Original is_active status: {chargeback.is_active}")  # Log original status
        chargeback.is_active = not chargeback.is_active
        chargeback.save(update_fields=['is_active'])
        print(f"Updated is_active status: {chargeback.is_active}")  # Log updated status
        serializer = ChargebackSerializer(chargeback, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)



def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    response = FileResponse(file_obj.file.open(), as_attachment=True, filename=file_obj.file.name)
    return response




@api_view(['DELETE'])
def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)






# views.py


# def send_email_to_merchant(request, chargeback_id):

#     try:
#         chargeback = Chargeback.objects.get(pk=chargeback_id)
#         subject = "Request for Chargeback Documentation"
#         message = f"Dear {chargeback.merchant_name},\n\nWe are reviewing a chargeback claim on a transaction and require additional documentation from you."
#         email_from = 'samaraouadi7@gmail.com'
#         recipient_list = [chargeback.merchant_email]

#         send_mail(subject, message, email_from, recipient_list)
#         return JsonResponse({'message': 'Email sent successfully!'}, status=200)
#     except Chargeback.DoesNotExist:
#         return JsonResponse({'error': 'Chargeback not found'}, status=404)
