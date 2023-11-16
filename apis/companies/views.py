from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter
from .models import Company
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import CompanySerializer
from rest_framework import viewsets, permissions


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.actives()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'cnpj']
    ordering_fields = ['name']
    ordering = ['name']

    @swagger_auto_schema(operation_summary="List all active companies")
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

