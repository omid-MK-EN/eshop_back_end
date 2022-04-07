
from rest_framework import viewsets
from .seriallizers import NewslettersSerializer
from .models import Newsletters

class NewslettersViewSet(viewsets.ModelViewSet):

    queryset= Newsletters.objects.all()
    serializer_class = NewslettersSerializer

    
