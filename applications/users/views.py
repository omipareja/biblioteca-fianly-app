from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from applications.users.api.serializers.users_serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
from applications.users.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh-token': login_serializer.validated_data.get('refresh'),
                    'user':user_serializer.data,
                    'message': 'Inicio de sesion Exitoso'
                },status=status.HTTP_200_OK)
            return  Response({'error','contraseña o nombre de usuario incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error', 'contraseña o nombre de usuario incorrectos'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self,request):
        print(request.data.get('user',''))
        user = User.objects.filter(pk=request.data.get('user',''))
        print(user.exists())
        if user.exists():
            RefreshToken.for_user(user.first())#cambia el token de refresh y no funcionara mas
            return Response({'message':'Sesion cerrada correctamente'},status=status.HTTP_200_OK)
        return Response({'error':'No existe este usuarsio'})
