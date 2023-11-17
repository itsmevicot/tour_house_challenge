from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter, SearchFilter
from .filters import CompanyFilter
from .models import Company
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CompanySerializer
from rest_framework import viewsets, permissions


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.actives()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name', 'address', 'country']
    filterset_class = CompanyFilter
    ordering_fields = ['name']
    ordering = ['name']

    @swagger_auto_schema(
        operation_summary="List all active companies",
        operation_description="Retrieve a paginated list of active companies with the ability to filter"
                              " by exact name, CNPJ, and country. "
                              "You can also perform a generic search across specified fields.",
        manual_parameters=[
            openapi.Parameter(
                'name',
                openapi.IN_QUERY,
                description="Filter companies by exact name, case-insensitive. E.g., 'Tech Corp'.",
                type=openapi.TYPE_STRING,
                example="Netflix"
            ),
            openapi.Parameter(
                'cnpj',
                openapi.IN_QUERY,
                description="Filter companies by exact CNPJ, case-insensitive. E.g., '12.345.678/0001-90'.",
                type=openapi.TYPE_STRING,
                example="60.795.926/0001-42"
            ),
            openapi.Parameter(
                'address',
                openapi.IN_QUERY,
                description="Filter companies by address. Supports partial matches.",
                type=openapi.TYPE_STRING,
                example="Church Street"
            ),
            openapi.Parameter(
                'country',
                openapi.IN_QUERY,
                description="Filter companies by exact country, case-insensitive. E.g., 'Brazil'.",
                type=openapi.TYPE_STRING,
                example="Brasil"
            ),
            openapi.Parameter(
                'search',
                openapi.IN_QUERY,
                description="A generic search term to look up companies, searching across fields like name,"
                            " address, and country.",
                type=openapi.TYPE_STRING,
                example="Rua"
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new company")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a specific company")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a company")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partially update a company")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a company (set inactive)")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
