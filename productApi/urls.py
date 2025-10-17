from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, RegistrationViewSet, UserLoginApiView

router = DefaultRouter()
router.register(r"applications", ProductViewSet, basename="applications")
router.register(r"registration", RegistrationViewSet, basename="registration")

urlpatterns = [
    path("", include(router.urls)),
    path("login/", UserLoginApiView.as_view(), name="login"),
]
