from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
# Project
from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordTokenCheckAPI, \
    RequestPasswordResetEmail, SetNewPasswordAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('verify/', VerifyEmail.as_view(), name='verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
    path('password-reset/<uidb64>/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh')
]