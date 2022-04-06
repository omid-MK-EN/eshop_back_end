from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.SimpleRouter()
router.register('product_color', EshopProductColorViewSet,basename="product_color")
router.register('product_size', EshopProductSizeViewSet,basename="product_size")
router.register('product_brand', EshopProductBrandViewSet,basename="product_brand")
router.register('related_photo', ProductRelatedPhotosViewSet,basename="related_photo")
router.register('product', EshopProductPhotosViewSet,basename="product")


urlpatterns = [
   path("",include(router.urls)),
]