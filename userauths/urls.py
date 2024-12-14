# userauths/urls.py
from django.urls import path
from .views import RegisterUserView, LoginUserView, UserDetailView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('<int:id>/', UserDetailView.as_view(), name='user_detail'),
]
