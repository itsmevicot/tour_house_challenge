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

    @swagger_auto_schema(operation_summary="List all active employees")
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
