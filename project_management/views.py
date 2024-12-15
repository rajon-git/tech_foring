# project_management/views.py
from rest_framework.viewsets import ModelViewSet
from .models import  Project
from .serializers import  ProjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

   