from rest_framework import routers
from .views import NewslettersViewSet,UserViewSet
from django.urls import path,include

router = routers.SimpleRouter()
router.register('newletters', NewslettersViewSet,basename="newletters")
router.register('user', UserViewSet,basename="user")



urlpatterns = [
   path("",include(router.urls)),
]