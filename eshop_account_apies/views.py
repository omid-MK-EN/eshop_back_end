
from rest_framework import viewsets
from .seriallizers import NewslettersSerializer,UserSeriallizer
from .models import Newsletters
from django.contrib.auth import get_user_model

class NewslettersViewSet(viewsets.ModelViewSet):

    queryset= Newsletters.objects.all()
    serializer_class = NewslettersSerializer
    

class UserViewSet(viewsets.ModelViewSet):

    queryset= get_user_model().objects.all()
    serializer_class = UserSeriallizer
    pagination_class= None
    paginator= None

    
