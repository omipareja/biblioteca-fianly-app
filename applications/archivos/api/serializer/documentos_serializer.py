from rest_framework import serializers
from applications.archivos.models import Archivos

class DocumentosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archivos
        fields = '__all__'

    def to_representation(self, instance):
        nombre = instance.get_nombre_archivo()[1]

        return {
            'pk':instance.pk,
            'carpeta':{
                'pk':instance.carpeta.pk,
                'nombre':instance.carpeta.nombre
            },
            'user': {
                'pk':instance.user.pk,
                'username':instance.user.username,
                'email':instance.user.email
            },
            'archivo': instance.archivo.url if instance.archivo != '' else '',
            'nombre': nombre

        }