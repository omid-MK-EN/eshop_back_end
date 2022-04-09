from rest_framework import serializers
from .models import Newsletters
from django.contrib.auth import get_user_model


class NewslettersSerializer(serializers.ModelSerializer):
    class Meta:
        model= Newsletters
        fields="__all__"

class UserSeriallizer(serializers.ModelSerializer):
    class Meta:
        model= get_user_model()
        fields="__all__"