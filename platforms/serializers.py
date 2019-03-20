from rest_framework import serializers
from .models import platforms

class platformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = platforms
        fields = ('Pid','type')

