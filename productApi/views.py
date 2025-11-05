from django.shortcuts import render
from rest_framework import viewsets, serializers
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, ProductSourcingSerializer, ProductSellingSerializer, OrderSerializer
from .permissions import StaffOrBuyerAuthentication
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .models import ProductSourcing, ProductSelling, Order


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


    def get_queryset(self):

        if self.request.user.is_superuser:
            return super().get_queryset()

        return super().get_queryset().filter(id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save()


class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProductSourcingViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSourcingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return ProductSourcing.objects.all()


class ProductSellingViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSellingSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
    def get_queryset(self):
        return ProductSelling.objects.all()


class OrderViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [StaffOrBuyerAuthentication]

    def get_queryset(self):

        if self.request.user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(buyer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(buyer=self.request.user)
