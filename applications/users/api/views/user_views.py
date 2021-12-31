from rest_framework import status
from  django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from applications.users.api.serializers.users_serializers import CreateUserSerializer,PasswordSerializer
from rest_framework.decorators import action


class UserViewset(viewsets.ModelViewSet):
    serializer_class = CreateUserSerializer


    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    @action(detail=True,methods=['POST'],url_path='update_pass')
    def set_password(self,request,pk=None):
        print(pk)
        user = self.serializer_class.Meta.model.objects.get(pk=pk)
        print(user)
        password_serializer = PasswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({
                'message':'contraseña actualizada correctamente'
            })
        return Response({
            'message':'Hay errores en la informacion enviada',
            'errors': password_serializer.errors
        },status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Usuario creado con exito'
            },
                status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)