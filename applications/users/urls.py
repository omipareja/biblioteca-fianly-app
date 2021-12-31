from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import  path
from applications.users.views import Login,Logout
urlpatterns = [

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token-verify/',TokenVerifyView.as_view(),name="token_verify"),
    ##CUSTOM LOGIN Y LOGOUT
    path('login2/',Login.as_view(),name='Login'),
    path('logout/',Logout.as_view())
]