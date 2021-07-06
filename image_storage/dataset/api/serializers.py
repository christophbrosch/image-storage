from ..models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    thumbnail_path = serializers.CharField()

    class Meta:
        model = Image
        fields = ('thumbnail_path',)