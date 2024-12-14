# urls.py
from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView

urlpatterns = [
    path('/', ProjectListCreateView.as_view(), name='list_create_project'),
    path('<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='retrieve_update_delete_project'),
]
