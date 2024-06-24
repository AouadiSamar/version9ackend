from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import CommentSerializer
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status







# views.py
from rest_framework import status
from rest_framework.response import Response
from .models import Rembourssement
from .serializers import RembourssementSerializer

from .serializers import ActionLogSerializer

from .models import ActionLog

import logging
import logging
import logging



# views.py in your Django app
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import  File
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
from .models import Rembourssement, File
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RembourssementSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementSerializer

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement, ActionLog
from .serializers import ActionLogSerializer

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from .models import ActionLog
from .serializers import ActionLogSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import File, Rembourssement
from .serializers import FileSerializer
from django.shortcuts import get_object_or_404

from rest_framework import generics
from .models import File
from .serializers import FileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ActionLog, Rembourssement
from .serializers import ActionLogSerializer
import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Rembourssement
from .serializers import RembourssementSerializer

###CRUDRembourssements
from rest_framework.permissions import IsAuthenticated

from rest_framework import views, status
from rest_framework.response import Response
from .models import Rembourssement
from .serializers import RembourssementSerializer

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Rembourssement
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework.response import Response



import logging
logger = logging.getLogger(__name__)
class RembourssementUpdateView(generics.UpdateAPIView):
    queryset = Rembourssement.objects.all()
    serializer_class = RembourssementSerializer



def update(self, request, *args, **kwargs):
    logger.debug(f"Received update data: {request.data}")
    partial = kwargs.pop('partial', True)  # Allowing partial updates
    serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)
    return Response(serializer.data)

    




class RembourssementDeleteView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        rembourssement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class RembourssementListView(APIView):

    def get(self, request):
        rembourssements = Rembourssement.objects.all()
        serializer = RembourssementSerializer(rembourssements, many=True)
        return Response(serializer.data)




class RembourssementDetailView(APIView):

    def get(self, request, pk):
        try:
            rembourssement = Rembourssement.objects.get(pk=pk)
            serializer = RembourssementSerializer(rembourssement)
            return Response(serializer.data)
        except Rembourssement.DoesNotExist:
            return Response({'error': 'Rembourssement not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        try:
            rembourssement = Rembourssement.objects.get(pk=pk)
            serializer = RembourssementSerializer(rembourssement, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Rembourssement.DoesNotExist:
            return Response({'error': 'Rembourssement not found'}, status=status.HTTP_404_NOT_FOUND)
        
        

    def delete(self, request, pk):
        try:
            rembourssement = Rembourssement.objects.get(pk=pk)
            rembourssement.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Rembourssement.DoesNotExist:
            return Response({'error': 'Rembourssement not found'}, status=status.HTTP_404_NOT_FOUND)



class ToggleActiveStatus(APIView):
    def patch(self, request, rembourssement_id):
        rembourssement = get_object_or_404(Rembourssement, id=rembourssement_id)
        rembourssement.is_active = not rembourssement.is_active
        rembourssement.save()
        print(f"Rembourssement {rembourssement.id} new is_active status: {rembourssement.is_active}")
        return Response({"success": True, "is_active": rembourssement.is_active}, status=status.HTTP_200_OK)


    

class AssignRembourssementView(APIView):
    def patch(self, request, pk):
        rembourssement = Rembourssement.objects.get(pk=pk)
        user_id = request.data.get('assigned_to')
        if user_id:
            rembourssement.assigned_to_id = user_id
            rembourssement.save(update_fields=['assigned_to'])
            return Response({"status": "Rembourssement assigned successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)



class RembourssementStatusUpdateView(APIView):
    def patch(self, request, pk):
        rembourssement = Rembourssement.objects.get(pk=pk)
        serializer = RembourssementSerializer(rembourssement, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class RembourssementLogsView(APIView):
    permission_classes = [IsAdminUser]  # This ensures only admin users can access this view

    def get(self, request, pk):
        logs = ActionLog.objects.filter(rembourssement__id=pk).order_by('-created_at')
        if not logs.exists():
            return Response({'message': 'No logs found'}, status=404)
        serializer = ActionLogSerializer(logs, many=True)
        return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from .models import Rembourssement, File
from .serializers import FileSerializer

class FileUploadView(APIView):
    def post(self, request, pk):
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        file_serializer = FileSerializer(data=request.data, context={'request': request})
        
        if file_serializer.is_valid():
            file_serializer.save(rembourssement=rembourssement)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from .models import Rembourssement
from .serializers import RembourssementDataSerializer
from django.http import FileResponse

def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    response = FileResponse(file_obj.file.open(), as_attachment=True, filename=file_obj.file.name)
    return response
@api_view(['GET'])
def rembourssement_data(request):
    try:
        # Aggregate rembourssements by month
        rembourssements = Rembourssement.objects.filter(is_active=True).annotate(month=TruncMonth('creation_date')).values('month').annotate(total_amount=Sum('amount')).order_by('month')
        
        # Convert datetime to date
        for rembourssement in rembourssements:
            rembourssement['month'] = rembourssement['month'].date()  # Convert to date
        
        serializer = RembourssementDataSerializer(rembourssements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer



from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rembourssement
from .serializers import RembourssementSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Rembourssement
from .serializers import RembourssementSerializer
import logging

logger = logging.getLogger(__name__)

class RembourssementCreateView(APIView):
    def get(self, request):
        try:
            rembourssements = Rembourssement.objects.all()
            serializer = RembourssementSerializer(rembourssements, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error fetching rembourssements: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            logger.info(f"Received data: {request.data}")  # Log the received data
            serializer = RembourssementSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                logger.info(f"New Rembourssement Created: ID {serializer.data.get('id')}")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                logger.error(f"Validation Error: {serializer.errors}")
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(f"Error creating rembourssement: {e}")
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Rembourssement, File
from .serializers import FileSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementSerializer

class CancelRembourssementView(APIView):
    def patch(self, request, pk):
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        rembourssement.is_active = False  # Set the rembourssement as inactive
        rembourssement.save()
        return Response({'status': 'Rembourssement canceled'}, status=status.HTTP_200_OK)

class ReactivateRembourssementView(APIView):
    def patch(self, request, pk):
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        rembourssement.is_active = True  # Set the rembourssement as active
        rembourssement.save()
        return Response({'status': 'Rembourssement reactivated'}, status=status.HTTP_200_OK)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Comment
from .serializers import CommentSerializer

class RembourssementCommentView(APIView):
    def get(self, request, rembourssement_id):
        comments = Comment.objects.filter(rembourssement_id=rembourssement_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request, rembourssement_id):
        serializer = CommentSerializer(data=request.data, context={'request': request, 'view': self})
        if serializer.is_valid():
            user = request.user
            serializer.validated_data['first_name'] = user.first_name
            serializer.validated_data['last_name'] = user.last_name
            serializer.validated_data['rembourssement_id'] = rembourssement_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Comment.DoesNotExist:
            return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Comment.DoesNotExist:
            return Response({"message": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)


class RembourssementCommentListView(APIView):
    def get(self, request, rembourssement_id):
        comments = Comment.objects.filter(rembourssement_id=rembourssement_id, parent=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, rembourssement_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(rembourssement_id=rembourssement_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Comment
from .serializers import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer

class RembourssementCommentDetailView(APIView):
    def get_object(self, comment_id):
        try:
            return Comment.objects.get(id=comment_id)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, comment_id, format=None):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, comment_id, format=None):
        comment = self.get_object(comment_id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, rembourssement_id):
        serializer = CommentSerializer(data=request.data, context={'request': request, 'view': self})
        if serializer.is_valid():
            user = request.user
            serializer.validated_data['first_name'] = user.first_name
            serializer.validated_data['last_name'] = user.last_name
            serializer.validated_data['rembourssement_id'] = rembourssement_id
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Print the validation errors to the console
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, format=None):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
class RembourssementCommentLikeView(APIView):
    def post(self, request, comment_id, format=None):
        comment = Comment.objects.get(id=comment_id)
        user = request.user
        if user in comment.liked_users.all():
            comment.liked_users.remove(user)
            comment.likes -= 1
            liked = False
        else:
            comment.liked_users.add(user)
            comment.likes += 1
            liked = True
        comment.save()
        return Response({'status': 'success', 'liked': liked, 'likes': comment.likes}, status=status.HTTP_200_OK)

