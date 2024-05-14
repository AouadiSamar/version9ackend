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




class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        rembourssement__id_id = self.kwargs.get('pk')  
        rembourssement = get_object_or_404(Rembourssement, pk=rembourssement__id_id)
        serializer.save(author=self.request.user, rembourssement=rembourssement)






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



class CommentView(APIView):
    def get(self, request, rembourssement__id_id):
        comments = Comment.objects.filter(rembourssement__id_id=rembourssement__id_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


    def post(self, request, rembourssement__id_id):
        # Ensure context is passed here with the serializer instantiation
        serializer = CommentSerializer(data=request.data, context={'request': request, 'view': self})
        if serializer.is_valid():
            rembourssement = Rembourssement.objects.get(id=rembourssement__id_id)
            try:
                # Pass rembourssement directly to the save method if needed
                serializer.save(rembourssement=rembourssement)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

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



class FileCreateView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer

class FileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class RembourssementCreateView(APIView):
    def get(self, request):
        rembourssements = Rembourssement.objects.all()
        serializer = RembourssementSerializer(rembourssements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RembourssementSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FileUploadView(APIView):
    def post(self, request, pk):
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        file_serializer = FileSerializer(data=request.data, context={'request': request})
        
        if file_serializer.is_valid():
            file_serializer.save(rembourssement=rembourssement)  # Pass rembourssement to save method
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
