from rest_framework import  serializers
from  applications.archivos.models import Carpetas

class CarpetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpetas
        fields = '__all__'


    def to_representation(self, instance):
        return {
            'pk':instance.pk,
            'nombre': instance.nombre,
            'created': instance.created,
            'usuario':{
                'pk':instance.user.pk,
                'username':instance.user.username,
                'email':instance.user.email
            }
        }