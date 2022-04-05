# from django.shortcuts import render
from rest_framework import viewsets
from .seriallizers import EshopAboutUsSerializer
from .models import EshopAboutUs

class EshopViewSet(viewsets.ModelViewSet):

    serializer_class = EshopAboutUsSerializer

    def get_queryset(self):
        return EshopAboutUs.objects.filter(is_active=True).first()
