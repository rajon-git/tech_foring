# views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Project
from .serializers import ProjectSerializer
# from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
