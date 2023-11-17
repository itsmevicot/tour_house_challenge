from rest_framework import serializers
from .models import Department
from ..companies.models import Company


class DepartmentSerializer(serializers.ModelSerializer):
    company = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Company.objects.actives(),
        required=False
    )

    class Meta:
        model = Department
        fields = '__all__'


class DepartmentWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
