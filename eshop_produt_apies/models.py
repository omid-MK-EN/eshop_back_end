from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

class EshopProductColor(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField(upload_to="color_image/", null=True, blank=True)
    active = models.BooleanField(default=True)
    is_exit = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class EshopProductSize(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField(upload_to="size_image/", null=True, blank=True)
    active = models.BooleanField(default=True)
    is_exit = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class EshopProductCategory(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField(upload_to="category_images/", null=True, blank=True)
    active = models.BooleanField(default=True)
    is_exit = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

class EshopProductBrand(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    image = models.ImageField(upload_to="brand_images/", null=True, blank=True)
    active = models.BooleanField(default=True)
    is_exit = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductRelatedPhotos(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to="related_images/", null=True, blank=True)
    active = models.BooleanField(default=True)
    

    def __str__(self):
        return self.name



class EshopProduct(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.TextField()
    slug = models.SlugField()
    price = models.FloatField(default=0)
    discount = models.FloatField(blank=True, null=True, default=0)
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=datetime.now())
    updated_at = models.DateTimeField(auto_now=datetime.now())
    image = models.ImageField(upload_to="eshop_products_images/")
    active = models.BooleanField(default=True)
    color = models.ManyToManyField(EshopProductColor, related_name="color")
    size = models.ManyToManyField(EshopProductSize, related_name="size",null=True,blank=True)
    brand = models.ForeignKey(EshopProductBrand, on_delete=models.CASCADE, related_name="brand")
    category = models.ForeignKey(EshopProductCategory, on_delete=models.CASCADE, related_name="category")
    is_sale_product = models.BooleanField(default=False)
    is_whole_product = models.BooleanField(default=False)
    is_popular_product = models.BooleanField(default=False)
    # mojodi der enbar
    is_exit = models.BooleanField(default=True)
    is_favorite= models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='is_favorite',null=True,blank=True)
    product_photo= models.ManyToManyField(ProductRelatedPhotos,related_name="product_related",null=True,blank=True)


    def __str__(self) -> str:
        return self.title

    @property
    def total_price(self):
        if self.discount == 0:
            return self.price
        return (self.price * self.discount) / 100