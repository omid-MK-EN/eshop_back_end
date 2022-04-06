from rest_framework import viewsets
from .seriallizers import *
from .models import *

class EshopProductColorViewSet(viewsets.ModelViewSet):
    queryset = EshopProductColor.objects.all()
    serializer_class = EshopProductColorSerializer


class EshopProductSizeViewSet(viewsets.ModelViewSet):
    queryset = EshopProductSize.objects.all()
    serializer_class =EshopProductSizeSerializer

class EshopProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = EshopProductCategory.objects.all()
    serializer_class= EshopProductCategorySerializer

class EshopProductBrandViewSet(viewsets.ModelViewSet):
    queryset = EshopProductBrand.objects.all()
    serializer_class= EshopProductBrandSerializer

class EshopProductBrandViewSet(viewsets.ModelViewSet):
    queryset = EshopProductBrand.objects.all()
    serializer_class= EshopProductBrandSerializer


class ProductRelatedPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductRelatedPhotos.objects.all()
    serializer_class= ProductRelatedPhotosSerializer

class EshopProductPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductRelatedPhotos.objects.all()
    serializer_class= EshopProductSerializer




