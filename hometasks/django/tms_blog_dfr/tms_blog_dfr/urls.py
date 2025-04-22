from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from post.views import PostViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from user.views import RegisterView, UserMeView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
# router.register(r'commets', CommentsViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('test/me/', UserMeView.as_view(), name='user-me'),
    path('auth/sign-up/', RegisterView.as_view(), name='sign-up'),
    path('auth/sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
