from django.contrib import admin
from applications.pruebas.models import Product,Sale,SaleDetail
# Register your models here.
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleDetail)