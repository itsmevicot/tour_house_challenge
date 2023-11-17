from django_filters import rest_framework as filters
from .models import Department


class DepartmentFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    company_name = filters.CharFilter(field_name='company__name', lookup_expr='iexact')

    class Meta:
        model = Department
        fields = ['company_name', 'cost_center', 'integration_code', 'name']
