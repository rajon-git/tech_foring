# project_management/urls.py
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CommentViewSet
from rest_framework_nested.routers import NestedDefaultRouter


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

tasks_router = NestedDefaultRouter(router, r'tasks', lookup='task')
tasks_router.register(r'comments', CommentViewSet)

urlpatterns = router.urls + tasks_router.urls