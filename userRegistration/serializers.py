from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }  # Write-only for input

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(
            **validated_data
        )  # Use create_user for best practices
        return user  # No extra save needed; create_user handles it
