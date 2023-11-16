from rest_framework import serializers
from .models import BaseUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = BaseUser
        fields = ['email', 'password']

    def create(self, validated_data):
        return BaseUser.objects.create_user(**validated_data)
