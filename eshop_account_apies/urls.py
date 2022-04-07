from rest_framework import routers
from .views import NewslettersViewSet
from django.urls import path,include

router = routers.SimpleRouter()
router.register('newsletters', NewslettersViewSet,basename="newletters")


urlpatterns = [
   path("",include(router.urls)),
]