from rest_framework import serializers
from applications.pruebas.models import Sale
class ProductoVentaSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    count = serializers.IntegerField()

class ProcesoVentaSerializer(serializers.Serializer):
    type_invoce = serializers.IntegerField()
    type_payment = serializers.IntegerField()
    adreesed_send = serializers.CharField()
    products = ProductoVentaSerializer(many=True)

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sale
        fields = '__all__'