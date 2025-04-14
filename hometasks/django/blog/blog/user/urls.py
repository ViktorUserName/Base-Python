from django.urls import path
from .views import RegisterUserView, LoginUserView, CurrentUserView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('', CurrentUserView.as_view(), name='current_user'),
]