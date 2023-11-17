from django_filters.rest_framework import DjangoFilterBackend, filters
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
    search_fields = ['name', 'company__name']
    filterset_class = DepartmentFilter
    ordering_fields = ['name']
    ordering = ['name']

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return DepartmentSerializer
        return DepartmentWriteSerializer

    @swagger_auto_schema(operation_summary="List all active departments")
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
