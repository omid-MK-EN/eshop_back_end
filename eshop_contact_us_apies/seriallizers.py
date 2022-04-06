from rest_framework import serializers
from .models import EshopContactUs,EshopForwardContactUsMessage


class EshopContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopContactUs
        fields="__all__"


class EshopContactUsMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopForwardContactUsMessage
        fields="__all__"