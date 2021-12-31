from rest_framework.routers import DefaultRouter
from applications.pruebas.api.views.ventas_views import ProcesoVentaViewSet

router  = DefaultRouter()
router.register(r'ventas',ProcesoVentaViewSet,basename='ventas')

urlpatterns = router.urls