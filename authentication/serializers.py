from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import BaseUser
import re


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = BaseUser
        fields = ['email', 'password']

    def validate_password(self, value):
        validate_password(value)

        if not any(char.isdigit() for char in value) or not any(char.isalpha() for char in value):
            raise serializers.ValidationError("A senha deve ser alfanumérica.")

        if not re.findall('[^A-Za-z0-9]', value):
            raise serializers.ValidationError("A senha deve conter pelo menos um caractere especial.")

        return value

    def create(self, validated_data):
        user = BaseUser.objects.create_user(**validated_data)
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token
