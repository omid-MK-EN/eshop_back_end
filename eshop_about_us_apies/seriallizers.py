from rest_framework import serializers
from .models import EshopAboutUs


class EshopAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopAboutUs
        fields="__all__"