from django.urls import path
from user import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('users/', views.CustomUserView.as_view({'post':'create_user'})),
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]