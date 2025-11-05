from django.urls import path
from rest_framework.routers import DefaultRouter  # Optional: For auto-routing
from .views import ProductSourcingViewSet, ProductSellingViewSet, UserLoginApiView, RegistrationViewSet, OrderViewSet # Adjust import as needed

# Option 1: Manual paths with actions (simple for specific endpoints)
urlpatterns = [
    path("product/sourcing", ProductSourcingViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy', 'post':'create'})),  # GET for list
    path("product/sourcing/<int:pk>/", ProductSourcingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),  # GET for single item
    path("product/selling", ProductSellingViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy', 'post':'create'})),  # GET for list
    path("product/selling/<int:pk>/", ProductSellingViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("product/order", OrderViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy', 'post':'create'})),  # GET for list
    path("product/order/<int:pk>/", OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path("login", UserLoginApiView.as_view()),
    path("registration", RegistrationViewSet.as_view({'get': 'list', 'put': 'update', 'delete': 'destroy', 'post':'create'})),
]

