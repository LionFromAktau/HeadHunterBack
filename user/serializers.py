from rest_framework import serializers
from . import models
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('email', 'password', 'first_name', 'last_name')