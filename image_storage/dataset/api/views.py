from rest_framework import generics, serializers
from rest_framework.permissions import BasePermission
from rest_framework.response import Response 
from ..models import Image, Dataset
from .serializers import ImageSerializer

class ImageListAPIView(generics.ListAPIView):
    """ Return specific image """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def has_permission(self, request, obj):
        return obj.owner == request.user

    def get_queryset(self):
        return Image.objects.filter(dataset__id=self.kwargs['pk'])

    def get(self, request, *args, **kwargs):
        try:
            dataset = Dataset.objects.get(pk=self.kwargs['pk'])
            if not self.has_permission(request, dataset):
                raise serializers.ValidationError('Nutzer hat keine Rechte auf den Datensatz zu zugreifen.')
            images = self.queryset.filter(dataset = dataset)
            response_data = self.get_serializer(images, many=True)
            return Response (
                {
                'data': response_data.data
                }
            )
        except Dataset.DoesNotExist:
            raise serializers.ValidationError('Datensatz existiert nicht.')
    