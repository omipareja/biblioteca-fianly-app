from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from applications.archivos.api.serializer.documentos_serializer import DocumentosSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from applications.archivos.models import Archivos
class DocumentoViewSet(viewsets.ModelViewSet):

    serializer_class = DocumentosSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

    def create(self, request, *args, **kwargs):

        data = {}
        print(request.user.pk)
        data['carpeta'] =request.data['carpeta']
        data['archivo'] = request.data['archivo']
        data['user'] = request.user.pk

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Archivo creado con exito',
            },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        user = request.user
        list = self.serializer_class.Meta.model.objects.filter(user=user)
        serializer = self.serializer_class(list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            archivo =self.serializer_class.Meta.model.objects.get(pk=pk)
        except:
            return Response({
                'msg':'El archivo no existe'
            },
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = self.serializer_class(archivo)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            archivo =self.serializer_class.Meta.model.objects.get(pk=pk)
            if archivo:
                archivo.delete()
                return Response({
                    'msg':'El archivo fue borrado con exito'
                },
                    status= status.HTTP_200_OK
                )
            else:
                return Response({
                    'msg':'No fue Posible borrar el archivo'
                },
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response({
                'msg':'No se ha encontrado el archivo'
            },
                status=status.HTTP_404_NOT_FOUND
            )

class DocumentoByNombre(ListAPIView):

    serializer_class = DocumentosSerializer

    def get_queryset(self,nombre):
        archivo = Archivos.objects.filter(archivo__icontains=nombre)
        print(archivo)
        if archivo:
            return archivo
        else:
            return []

    def get(self, request):
        nombre = request.GET['nombre']
        queryset = self.get_queryset(nombre)
        serializer = DocumentosSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)