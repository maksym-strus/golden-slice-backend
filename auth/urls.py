from django.urls import path
from auth.views import MyObtainTokenPairView, RegisterView, ChangePasswordView, UpdateProfileView, LogoutView
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView,TokenObtainPairView


urlpatterns = [
    path('/login', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('/login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('/register', RegisterView.as_view(), name='auth_register'),
    path('/change_password/<int:pk>', ChangePasswordView.as_view(), name='auth_change_password'),
    path('/update_profile/<int:pk>', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('/logout', LogoutView.as_view(), name='auth_logout'),
    path('/check', TokenVerifyView.as_view(), name='check_token')
]
