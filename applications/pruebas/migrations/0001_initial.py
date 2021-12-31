# Generated by Django 3.2.9 on 2021-12-29 15:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.TextField(blank=True, verbose_name='Descripcion producto')),
                ('man', models.BooleanField(default=True, verbose_name='Para Hombre')),
                ('woman', models.BooleanField(default=True, verbose_name='Para Mujer')),
                ('weight', models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Peso')),
                ('price_purchase', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Precio de Compra')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio de Venta')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stok')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad de Productos')),
                ('type_invoce', models.CharField(choices=[('0', 'BOLETA'), ('3', 'FACTURA'), ('4', 'OTRO')], max_length=2, verbose_name='TIPO')),
                ('cancelado', models.BooleanField(default=False)),
                ('type_payment', models.CharField(choices=[('0', 'TARJETA'), ('1', 'DEPOSITO'), ('2', 'CONTRAENTREGA')], max_length=2, verbose_name='TIPO PAGO')),
                ('adreese_send', models.TextField(blank=True, verbose_name='Direccion de Envio')),
                ('anulate', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'ventas',
            },
        ),
        migrations.CreateModel(
            name='SaleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('count', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('price_purchase', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Precio Compra')),
                ('price_sale', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio Venta')),
                ('anulate', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebas.sale', verbose_name='Codigo de Venta')),
            ],
            options={
                'verbose_name': 'Detalle Venta',
                'verbose_name_plural': 'Detalles de una Venta',
            },
        ),
    ]
