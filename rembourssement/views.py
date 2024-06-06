import logging
from django.shortcuts import get_object_or_404
from django.http import FileResponse, Http404, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from .models import Rembourssement, Comment, ActionLog, File
from .serializers import RembourssementSerializer, CommentSerializer, ActionLogSerializer, FileSerializer

logger = logging.getLogger(__name__)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from .serializers import CommentSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Comment, Rembourssement
from .serializers import CommentSerializer

class CommentListView(APIView):
    def get(self, request, rembourssement_id):
        comments = Comment.objects.filter(rembourssement_id=rembourssement_id, parent=None)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, rembourssement_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            serializer.save(rembourssement_id=rembourssement_id, user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailView(APIView):
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
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id, format=None):
        comment = self.get_object(comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentLikeView(APIView):
    def post(self, request, comment_id, format=None):
        comment = Comment.objects.get(id=comment_id)
        comment.likes += 1
        comment.save()
        return Response({'status': 'comment liked'}, status=status.HTTP_200_OK)


class CommentDislikeView(APIView):
    def post(self, request, comment_id, format=None):
        comment = Comment.objects.get(id=comment_id)
        comment.dislikes += 1
        comment.save()
        return Response({'status': 'comment disliked'}, status=status.HTTP_200_OK)


class CommentReplyView(APIView):
    def post(self, request, comment_id, format=None):
        parent_comment = Comment.objects.get(id=comment_id)
        text = request.data.get('text')
        reply_comment = Comment.objects.create(
            text=text, 
            rembourssement=parent_comment.rembourssement, 
            parent=parent_comment, 
            user=request.user,
            first_name=request.user.first_name,
            last_name=request.user.last_name
        )
        serializer = CommentSerializer(reply_comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RembourssementUpdateView(generics.UpdateAPIView):
    queryset = Rembourssement.objects.all()
    serializer_class = RembourssementSerializer

    def update(self, request, *args, **kwargs):
        logger.debug(f"Received update data: {request.data}")
        partial = kwargs.pop('partial', True)
        serializer = self.get_serializer(data=request.data, instance=self.get_object(), partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
from django.conf import settings




class RembourssementDeleteView(APIView):
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        rembourssement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
from django.utils.dateparse import parse_date
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementSerializer
import logging

logger = logging.getLogger(__name__)

class RembourssementListView(APIView):
    def get(self, request):
        logger.debug("Received request to list rembourssements")
        try:
            rembourssements = Rembourssement.objects.all()
            serializer = RembourssementSerializer(rembourssements, many=True)
            return Response(serializer.data)
        except Exception as e:
            logger.error(f"Error retrieving rembourssements: {str(e)}")
            return Response({'error': 'Failed to retrieve rembourssements'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
            return Response({'error': 'Rembourssment not found'}, status=status.HTTP_404_NOT_FOUND)



class RembourssementStatusUpdateView(APIView):
    def patch(self, request, pk):
        rembourssement = Rembourssement.objects.get(pk=pk)
        serializer = RembourssementSerializer(rembourssement, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.permissions import IsAdminUser

class RembourssementLogsView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        logs = ActionLog.objects.filter(rembourssement__id=pk).order_by('-created_at')
        if not logs.exists():
            return Response({'message': 'No logs found'}, status=404)
        serializer = ActionLogSerializer(logs, many=True)
        return Response(serializer.data)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RembourssementSerializer
from .models import Rembourssement
import logging

logger = logging.getLogger(__name__)

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



@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, pk, format=None):
        rembourssement = get_object_or_404(Rembourssement, pk=pk)
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save(rembourssement=rembourssement)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.decorators import api_view

@csrf_exempt

@api_view(['DELETE'])
def delete_file(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@csrf_exempt

def download_file(request, file_id):
    file_obj = get_object_or_404(File, id=file_id)
    response = FileResponse(file_obj.file.open(), as_attachment=True, filename=file_obj.file.name)
    return response





class FileDetailView(APIView):
    def get(self, request, rembourssement_id, file_id, format=None):
        file = get_object_or_404(File, rembourssement__id=rembourssement_id, id=file_id)
        serializer = FileSerializer(file)
        return Response(serializer.data)
from django.db.models import Sum

from rest_framework import status
from .models import Rembourssement
from .serializers import RembourssementChartDataSerializer
from django.db.models.functions import TruncMonth

class RembourssementDataView(APIView):
    def get(self, request):
        rembourssements = Rembourssement.objects.annotate(month=TruncMonth('creation_date')).values('month').annotate(total_amount=Sum('amount')).order_by('month')
        serializer = RembourssementChartDataSerializer(rembourssements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
