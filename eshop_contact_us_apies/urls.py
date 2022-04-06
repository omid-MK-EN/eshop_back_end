from rest_framework import routers
from .views import EshopContactUsViewSet, EshopContactUsMessageViewSet
from django.urls import path,include
#
router = routers.SimpleRouter()
router.register('contact_us',EshopContactUsViewSet,basename="contact_us")
router.register('forward_message_contact_us',EshopContactUsMessageViewSet,basename="forward_message_contact_us")
#
#
urlpatterns = [
   path("",include(router.urls)),
]