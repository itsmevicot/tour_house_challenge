from rest_framework import serializers
from apis.departments.models import Department
from apis.employees.models import Employee
import re


class EmployeeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def validate_phone_number(self, value):
        normalized_phone = re.sub(r'\D', '', value)
        return normalized_phone

    def validate_city(self, value):
        normalized_city = value.title()
        return normalized_city

    def validate(self, data):
        if 'resignation_date' in data and data['resignation_date'] is not None:
            data['is_active'] = False
        return data


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Department.objects.actives(),
        required=False
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['department'] = instance.department.name
        return representation

    class Meta:
        model = Employee
        fields = '__all__'
