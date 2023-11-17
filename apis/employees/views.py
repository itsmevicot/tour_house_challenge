from drf_yasg import openapi
from rest_framework import viewsets, permissions
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema

from .filters import EmployeeFilter
from .models import Employee
from .serializers import EmployeeSerializer, EmployeeWriteSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.actives()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['full_name', 'email', 'department__name', 'city']
    filterset_class = EmployeeFilter
    ordering_fields = ['full_name', 'email', 'department', 'city']
    ordering = ['full_name']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return EmployeeSerializer
        return EmployeeWriteSerializer

    @swagger_auto_schema(
        operation_summary="List all active employees",
        operation_description="Retrieve a paginated list of active employees filtered by various parameters. "
                              "Use the search parameter to perform a text search across multiple fields.",
        manual_parameters=[
            openapi.Parameter(
                'full_name',
                in_=openapi.IN_QUERY,
                description="Filter employees by full name, allowing partial, case-insensitive matches. "
                            "For example, 'John' will match 'John Doe' and 'Johnny'.",
                type=openapi.TYPE_STRING,
                example="John"
            ),
            openapi.Parameter(
                'company_name',
                in_=openapi.IN_QUERY,
                description="Filter employees by their company's name using a case-insensitive, exact match. "
                            "For example, 'Tour House' must be provided in full.",
                type=openapi.TYPE_STRING,
                example="Tour House"
            ),
            openapi.Parameter(
                'department',
                in_=openapi.IN_QUERY,
                description="Filter employees by their department's name using a case-insensitive, exact match. "
                            "For example, 'Human Resources' will only match 'Human Resources'.",
                type=openapi.TYPE_STRING,
                example="Recursos Humanos"
            ),
            openapi.Parameter(
                'city',
                in_=openapi.IN_QUERY,
                description="Filter employees by city. For example, searching for 'New York' will return employees "
                            "located in New York.",
                type=openapi.TYPE_STRING,
                example="Império"
            ),
            openapi.Parameter(
                'search',
                in_=openapi.IN_QUERY,
                description="A generic search term to look up employees, searching across fields like full name, "
                            "email, department name, and city. For example, a search for 'developer' might return "
                            "employees with 'developer' in their job title or department.",
                type=openapi.TYPE_STRING,
                example="developer"
            ),
        ]
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new employee")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Retrieve an active employee")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update an employee")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Partially update an employee")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete an employee (set inactive)")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
