# from django.shortcuts import render
from rest_framework import viewsets
from .seriallizers import EshopAboutUsSerializer
from .models import EshopAboutUs

class EshopAboutUsViewSet(viewsets.ModelViewSet):
    paginations_class= None
    paginator = None
    serializer_class = EshopAboutUsSerializer

    def get_queryset(self):
        return EshopAboutUs.objects.filter(is_active=True)
       
