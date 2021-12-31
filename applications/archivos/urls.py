from django.urls import path
from applications.archivos.api.views.documentos_views import DocumentoByNombre
from applications.archivos.api.views.archivos_views import CarpetasRetrieveView
urlpatterns = [
    path('search-archivo/',DocumentoByNombre.as_view(),name="document_by_Nombre"),
    path('carpeta/retrieve/<int:pk>/',CarpetasRetrieveView.as_view(),name="carpeta-retrie")
]