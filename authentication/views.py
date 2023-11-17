from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import UserRegistrationSerializer, CustomTokenObtainPairSerializer


class UserRegistrationView(views.APIView):
    @swagger_auto_schema(request_body=UserRegistrationSerializer, operation_summary="Register a new user")
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    @swagger_auto_schema(operation_summary="Obtain JWT Token")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(operation_summary="Refresh JWT Token")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)