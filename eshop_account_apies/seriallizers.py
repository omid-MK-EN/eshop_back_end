from rest_framework import serializers
from .models import Newsletters


class NewslettersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Newsletters
        fields="__all__"