from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView

urlpatterns = [
    path('api/get_user',UserDetailAPI.as_view()),
    path('api/register_user',RegisterUserAPIView.as_view())
]