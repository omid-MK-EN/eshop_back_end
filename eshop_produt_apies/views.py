from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
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
    paginations_class= None
    paginator = None

class EshopProductBrandViewSet(viewsets.ModelViewSet):
    queryset = EshopProductBrand.objects.all()
    serializer_class= EshopProductBrandSerializer
    paginations_class= None
    paginator = None



class ProductRelatedPhotosViewSet(viewsets.ModelViewSet):
    queryset = ProductRelatedPhotos.objects.all()
    serializer_class= ProductRelatedPhotosSerializer
    paginations_class= None
    paginator = None

class EshopProductViewSet(viewsets.ModelViewSet):
    queryset =  EshopProduct.objects.filter(active=True)
    serializer_class= EshopProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand']




