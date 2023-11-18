from apis.departments.models import Department
from apis.employees.models import Employee
from datetime import datetime
from rest_framework import serializers
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

    def validate_admission_date(self, value):
        today = datetime.today().date()
        if value and value > today:
            raise serializers.ValidationError('Admission date cannot be in the future')
        return value

    def validate_resignation_date(self, value):
        today = datetime.today().date()
        if value and value > today:
            raise serializers.ValidationError('Resignation date cannot be in the future')
        return value

    def validate_birthdate(self, value):
        today = datetime.today().date()
        if value and value > today:
            raise serializers.ValidationError('Birthdate cannot be in the future')
        age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
        if age < 18:
            raise serializers.ValidationError('Employee must be at least 18 years old')
        return value

    def validate(self, data):
        admission_date = data.get('admission_date')
        resignation_date = data.get('resignation_date')

        if resignation_date and admission_date:
            if resignation_date < admission_date:
                raise serializers.ValidationError({
                    'resignation_date': 'Resignation date must be after admission date'
                })

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
