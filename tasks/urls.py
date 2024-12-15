# project_management/urls.py
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'', TaskViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls