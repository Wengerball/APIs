from django.shortcuts import render
from rest_framework import viewsets
from .models import platforms
from .serializers import platformsSerializer
# Create your views here.

class platformsView(viewsets.ModelViewSet):
    queryset = platforms.objects.all()
    serializer_class = platformsSerializer
