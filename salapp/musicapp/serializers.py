from rest_framework import serializers
from .models import music


class musicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music
        fields = '__all__'
