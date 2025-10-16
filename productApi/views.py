from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer, UserSerializer
from .permissions import ReadOnlyOrAuthenticated

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [ReadOnlyOrAuthenticated]

    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
