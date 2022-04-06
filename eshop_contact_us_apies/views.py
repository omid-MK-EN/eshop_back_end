from rest_framework import viewsets
from .seriallizers import EshopContactUsSerializer,EshopContactUsMessageSerializer,EshopSocialMediaSerializer
from .models import EshopContactUs,EshopForwardContactUsMessage,EshopSocialMedia

class EshopContactUsViewSet(viewsets.ModelViewSet):
    queryset = EshopContactUs.objects.all()
    serializer_class = EshopContactUsSerializer


class EshopContactUsMessageViewSet(viewsets.ModelViewSet):
    queryset = EshopForwardContactUsMessage.objects.all()
    serializer_class = EshopContactUsMessageSerializer

class EshopSocialMediasViewSet(viewsets.ModelViewSet):
    queryset = EshopSocialMedia.objects.all()
    serializer_class = EshopSocialMediaSerializer



