from dataclasses import fields
from itertools import product
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
    product_related= serializers.StringRelatedField(many=True)

    class Meta:
        model= EshopProduct
        # fields=['title','brand','category','product_related']
        fields="__all__"
        extra_fields = ['product_related']


class EshopProductCategorySerializer(serializers.ModelSerializer):

    # def get_products(self,obj):
    #     qs= EshopProduct.objects.filter(category=obj.id)
    #     # print(EshopProductSerializer(qs, many=True).data['title'])
    #     return EshopProductSerializer(qs, many=True).data
       
    # products = serializers.StringRelatedField(many=True)

    def get_products(self,obj):
        ides=[]
        titles=[]
        prices=[]
        images=[]
        info=[]
        active_products= EshopProduct.objects.filter(active=True,category=obj.id)
        for product in active_products:
             ides.append(product.id)
             titles.append(product.title)
             prices.append(product.price)
             images.append(product.image.url)

        info=[{"id":ides[index],"title":titles[index],'price':prices[index],'image':images[index]}for index in range(0,len(ides))]
        # print("================================")
        # print(active_products)
       
        return info


    products = serializers.SerializerMethodField()

    class Meta:
        model= EshopProductCategory
        fields="__all__"
        # extra_fields=['products']
class EshopProductBrandSerializer(serializers.ModelSerializer):

    def get_count(self,obj):
        count= EshopProduct.objects.filter(brand=obj.id).count()
        return count

    count = serializers.SerializerMethodField()
    # product = serializers.StringRelatedField(many=True)
    class Meta:
        model= EshopProductBrand
        fields="__all__"
      
       
       

class ProductRelatedPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProductRelatedPhotos
        fields="__all__"






