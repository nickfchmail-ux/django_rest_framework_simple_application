from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User
from rest_framework import serializers
from productApi.models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ["id", "email", "name", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }

    def normalize_email(self, email):
        # Simple normalization: lowercase and strip spaces
        return email.lower().strip()

    def create(self, validated_data):
        password = validated_data.pop("password")
        email = validated_data.get("email")
        name = validated_data.get("name")
        normalized_email = self.normalize_email(email)
        validated_data["email"] = normalized_email  # Update with normalized version
        user = UserProfile.objects.create_user(**validated_data, password=password)
        return user


class ProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Product
        fields = "__all__"
