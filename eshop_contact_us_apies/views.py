from rest_framework import viewsets
from .seriallizers import EshopContactUsSerializer,EshopContactUsMessageSerializer
from .models import EshopContactUs,EshopForwardContactUsMessage

class EshopContactUsViewSet(viewsets.ModelViewSet):
    queryset = EshopContactUs.objects.all()
    serializer_class = EshopContactUsSerializer


class EshopContactUsMessageViewSet(viewsets.ModelViewSet):
    queryset = EshopForwardContactUsMessage.objects.all()
    serializer_class = EshopContactUsMessageSerializer



