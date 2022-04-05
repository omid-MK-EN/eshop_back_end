from rest_framework import serializers
from .models import EshopAboutUs


class EshopAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model= EshopAboutUs
        exclude= ["is_active"]