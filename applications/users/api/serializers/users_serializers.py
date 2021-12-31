from rest_framework import  serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from applications.users.models import User

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','fullname',
                  'genero']

    def create(self, validated_data):
        user = User.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                fullname = validated_data['fullname'],
                genero = validated_data['genero'],
            )

        user.set_password(validated_data['password'])
        user.save()

        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk','username', 'email', 'fullname',
                 'genero', 'password', 'datebirth']


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6,write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self,data):
        if data['password'] != data['password2']:
            raise  serializers.ValidationError({'password':'Debe ingresar ambas contraseñas iguales'})
        return data