from django_filters.rest_framework import DjangoFilterBackend, filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter

from .filters import DepartmentFilter
from .models import Department
from .serializers import DepartmentSerializer, DepartmentWriteSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.actives()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['name', 'company__name', 'cost_center', 'integration_code']
    filterset_class = DepartmentFilter
    ordering_fields = ['name', 'company__name', 'cost_center', 'integration_code']
    ordering = ['id']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DepartmentSerializer
        return DepartmentWriteSerializer

    @swagger_auto_schema(
        operation_summary="List all active departments",
        operation_description="Retrieve a paginated list of active departments filtered by name, company name, or other attributes. "
                              "Use the search parameter to perform a text search across multiple department-related fields.",
        manual_parameters=[
            openapi.Parameter(
                'name',
                in_=openapi.IN_QUERY,
                description="Search for departments by name. Supports partial, case-insensitive matches. "
                            "E.g., 'fin' will match 'Finance'.",
                type=openapi.TYPE_STRING,
                example="Sales"
            ),
            openapi.Parameter(
                'company_name',
                in_=openapi.IN_QUERY,
                description="Search for departments by the exact name of their associated company, case-insensitive. "
                            "E.g., 'Acme Corp' must be provided in full.",
                type=openapi.TYPE_STRING,
                example="Tour House"
            ),
            openapi.Parameter(
                'cost_center',
                in_=openapi.IN_QUERY,
                description="Filter departments by cost center identifier.",
                type=openapi.TYPE_STRING,
                example="CC001"
            ),
            openapi.Parameter(
                'integration_code',
                in_=openapi.IN_QUERY,
                description="Filter departments by integration code.",
                type=openapi.TYPE_STRING,
                example="IC001"
            ),
            openapi.Parameter(
                'search',
                in_=openapi.IN_QUERY,
                description="A general search filter that looks through all department fields for a match.",
                type=openapi.TYPE_STRING,
                example="Research"
            )
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new department")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve a specific department")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a department")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partially update a department")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a department (set inactive)")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
