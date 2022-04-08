from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.SimpleRouter()
router.register('product_colorss', EshopProductColorViewSet,basename="product_colors")
router.register('product_sizes', EshopProductSizeViewSet,basename="product_sizes")
router.register('product_categories', EshopProductCategoryViewSet,basename="product_categories")
router.register('product_brands', EshopProductBrandViewSet,basename="product_brands")
router.register('related_photos', ProductRelatedPhotosViewSet,basename="related_photos")
router.register('products',  EshopProductViewSet,basename="products")


urlpatterns = [
   path("",include(router.urls)),
]