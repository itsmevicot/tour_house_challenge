from django_filters import rest_framework as filters
from apis.companies.models import Company


class CompanyFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='iexact')
    city = filters.CharFilter(lookup_expr='iexact')
    cnpj = filters.CharFilter(lookup_expr='iexact')
    country = filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'address', 'country', 'city']
