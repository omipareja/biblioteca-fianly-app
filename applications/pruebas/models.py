from django.db import models
from model_utils.models import TimeStampedModel


class Product(TimeStampedModel):
    """Modelo que representa a un producto de tienda"""

    name = models.CharField(
        'Nombre',
        max_length=100
    )
    description = models.TextField(
        'Descripcion producto',
        blank=True
    )
    man = models.BooleanField(
        'Para Hombre',
        default=True
    )
    woman = models.BooleanField(
        'Para Mujer',
        default=True
    )
    weight = models.DecimalField(
        'Peso',
        max_digits=5,
        decimal_places=2,
        default=1
    )
    price_purchase = models.DecimalField(
        'Precio de Compra',
        max_digits=10,
        decimal_places=3
    )
    price_sale = models.DecimalField(
        'Precio de Venta',
        max_digits=10,
        decimal_places=2
    )
    stock = models.PositiveIntegerField('Stok', default=0)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return str(self.id) + ' ' + str(self.name)


class Sale(TimeStampedModel):
    """Modelo que representa a una Venta Global"""

    TIPO_INVOCE = (
        ('0', 'BOLETA'),
        ('3', 'FACTURA'),
        ('4', 'OTRO'),
    )

    TIPO_PAYMENT = (
        ('0', 'TARJETA'),
        ('1', 'DEPOSITO'),
        ('2', 'CONTRAENTREGA'),
    )
###########################################
    amount = models.DecimalField(
        'Monto',
        max_digits=10,
        decimal_places=2
    )
    count = models.PositiveIntegerField('Cantidad de Productos')
    type_invoce = models.CharField(
        'TIPO',
        max_length=2,
        choices=TIPO_INVOCE
    )
    cancelado = models.BooleanField(default=False)
    type_payment = models.CharField(
        'TIPO PAGO',
        max_length=2,
        choices=TIPO_PAYMENT
    )
    adreese_send = models.TextField(
        'Direccion de Envio',
        blank=True,
    )
    anulate = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'ventas'

    def __str__(self):
        return  str(self.id)


class SaleDetail(TimeStampedModel):
    """Modelo que representa a una venta en detalle"""

    sale = models.ForeignKey(
        Sale,
        on_delete=models.CASCADE,
        verbose_name='Codigo de Venta'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField('Cantidad')
    price_purchase = models.DecimalField(
        'Precio Compra',
        max_digits=10,
        decimal_places=3
    )
    price_sale = models.DecimalField(
        'Precio Venta',
        max_digits=10,
        decimal_places=2
    )
    anulate = models.BooleanField(default=False)
    #

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalles de una Venta'

    def __str__(self):
        return str(self.sale.id) + ' - ' + str(self.product.name)