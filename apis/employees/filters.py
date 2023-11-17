from django_filters import rest_framework as filters
from .models import Employee


class EmployeeFilter(filters.FilterSet):
    full_name = filters.CharFilter(lookup_expr='icontains')
    company_name = filters.CharFilter(field_name='department__company__name', lookup_expr='iexact')
    department = filters.CharFilter(field_name='department__name', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['company_name', 'department', 'city']
