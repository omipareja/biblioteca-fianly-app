from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from applications.pruebas.models import Product,Sale,SaleDetail
from applications.pruebas.api.serializers.serializers import ProcesoVentaSerializer,SaleSerializer


class ProcesoVentaViewSet(ViewSet):
    serializer_class = ProcesoVentaSerializer

    def get_queryset(self):
        return Sale.objects.all()

    def list(self,request):

        sales = Sale.objects.all().order_by('pk')
        serializer = SaleSerializer(sales,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            venta = Sale(
                amount=0,
                count=0,
                type_invoce=serializer.validated_data['type_invoce'],
                cancelado=False,
                type_payment= serializer.validated_data['type_payment'],
                adreese_send=serializer.validated_data['adreesed_send'],
                anulate= False
            )

            productos = serializer.validated_data['products']
            amount = 0
            count = 0
            ventas_detalle = []
            for producto in productos:
                prod = Product.objects.get(pk=producto['pk'])
                venta_detail = SaleDetail(
                    sale= venta,
                    product = prod,
                    count = producto['count'],
                    price_purchase= prod.price_purchase,
                    price_sale= prod.price_sale,
                    anulate=False
                )
                count = count + producto['count']
                amount = amount + (prod.price_sale * producto['count'])
                ventas_detalle.append(venta_detail)
            venta.count = count
            venta.amount = amount
            venta.save()
            SaleDetail.objects.bulk_create(ventas_detalle)
            return Response({'msg':'Factura almacenada con exito'})
        return Response(
            {
                'msg': ' no Valido',
                'errors':serializer.errors
            }
        )