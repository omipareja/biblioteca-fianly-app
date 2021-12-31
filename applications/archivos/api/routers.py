from  rest_framework.routers import  DefaultRouter
from applications.archivos.api.views.archivos_views import CarpetasViewSet
from  applications.archivos.api.views.documentos_views import  DocumentoViewSet
router= DefaultRouter()

router.register(r'carpetas',CarpetasViewSet,basename='carpetas')
router.register(r'documentos',DocumentoViewSet,basename='documentos')

urlpatterns = router.urls