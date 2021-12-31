from rest_framework import  status
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView
from applications.archivos.api.serializer.archivos_serializer import CarpetaSerializer

from rest_framework.permissions import IsAuthenticated
from applications.archivos.models import Archivos,Carpetas
from applications.archivos.api.serializer.documentos_serializer import DocumentosSerializer



class CarpetasViewSet(viewsets.ModelViewSet):
    serializer_class = CarpetaSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()





    def list(self, request, *args, **kwargs):
        user = request.user
        list = self.serializer_class.Meta.model.objects.filter(user=user)
        serializer = self.serializer_class(list,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = {}
        data['nombre']=request.data['nombre']
        data['user']=request.user.pk


        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg':'Carpeta Creada con exito'
            },
            status= status.HTTP_201_CREATED
            )
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            pk = kwargs['pk']
            data = {}
            data['nombre'] = request.data['nombre']
            data['user'] = request.user.pk
            album = self.serializer_class.Meta.model.objects.get(pk=pk)

            serializer = self.serializer_class(album, data=data)
        except Exception as e:
            print('Excepcion:',e)
            return Response({'message':'No se encontro la carpeta'},status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Carpeta Actualizada con exito'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            pk=kwargs['pk']
            carpeta_datail = Carpetas.objects.get(pk=pk)
            carpeta = Archivos.objects.filter(carpeta=carpeta_datail)
        except:
            return  Response({'msg: La carpeta no existe'},status=status.HTTP_404_NOT_FOUND)

        serializer = DocumentosSerializer(carpeta,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        try:
            pk=kwargs['pk']
            carpeta = self.serializer_class.Meta.model.objects.get(pk=pk)
            if carpeta:
                carpeta.delete()
                return Response({'msg':'La carpeta ha sifo eliminada con exito'},status=status.HTTP_200_OK)
            else:
                return Response({'msg':'Porfavor Contacte con el administrador'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'msg':'No se ha encontrado la carperta'},status=status.HTTP_400_BAD_REQUEST)


class CarpetasRetrieveView(RetrieveAPIView):
    serializer_class = CarpetaSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()