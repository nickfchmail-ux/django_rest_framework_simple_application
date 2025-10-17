from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistrationViewSet, UserLoginApiView

router = DefaultRouter()
router.register(r"registration", RegistrationViewSet, basename="reg")


urlpatterns = [
    path("", include(router.urls)),
    path("login/", UserLoginApiView.as_view(), name="login"),
]
