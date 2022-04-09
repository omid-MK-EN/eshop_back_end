from unicodedata import category
from rest_framework import serializers
from .models import *


class EshopProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopProductColor
        fields="__all__"

class EshopProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopProductSize
        fields="__all__"

class EshopProductSerializer(serializers.ModelSerializer):
    def get_brand(self,obj):
        return obj.brand.name
    
    def get_category(self,obj):
        return obj.category.name

    brand=serializers.SerializerMethodField()
    category=serializers.SerializerMethodField()
    class Meta:
        model= EshopProduct
        fields="__all__"


class EshopProductCategorySerializer(serializers.ModelSerializer):

    def get_products(self,obj):
       
      
        qs= EshopProduct.objects.filter(category=obj.id)
        # print(EshopProductSerializer(qs, many=True).data['title'])
        return EshopProductSerializer(qs, many=True).data
       
    products= serializers.SerializerMethodField()
    class Meta:
        model= EshopProductCategory
        fields="__all__"

class EshopProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopProductBrand
        fields=['product']

class ProductRelatedPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductRelatedPhotos
        fields="__all__"






