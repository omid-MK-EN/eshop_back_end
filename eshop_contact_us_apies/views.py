from rest_framework import viewsets
from .seriallizers import EshopContactUsSerializer,EshopContactUsMessageSerializer,EshopSocialMediaSerializer
from .models import EshopContactUs,EshopForwardContactUsMessage,EshopSocialMedia

class EshopContactUsViewSet(viewsets.ModelViewSet):
    queryset = EshopContactUs.objects.all()
    serializer_class = EshopContactUsSerializer
    paginations_class= None
    paginator = None

class EshopContactUsMessageViewSet(viewsets.ModelViewSet):
    queryset = EshopForwardContactUsMessage.objects.all()
    serializer_class = EshopContactUsMessageSerializer
    paginations_class= None
    paginator = None

class EshopSocialMediasViewSet(viewsets.ModelViewSet):
    queryset = EshopSocialMedia.objects.all()
    serializer_class = EshopSocialMediaSerializer
    paginations_class= None
    paginator = None



