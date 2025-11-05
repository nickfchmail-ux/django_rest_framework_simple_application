from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.core.validators import RegexValidator
from productApi.models import UserProfile, UserDetail, ProductSourcing, ProductSelling, Order

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=50,
        validators=[UniqueValidator(queryset=UserProfile.objects.all())]
    )
    account_name = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True, min_length=8, required=True)
    last_name = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    contact_number = serializers.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', 'Enter a valid 8-digit number.')]
    )
    address = serializers.CharField(max_length=300)

    def normalize_email(self, email):
        return email.lower().strip()

    def create(self, validated_data):
        user_data = {
            'email': self.normalize_email(validated_data.pop('email')),
            'account_name': validated_data.pop('account_name'),
            'password': validated_data.pop('password')
        }
        user = UserProfile.objects.create_user(**user_data)
        details_data = validated_data
        details_data['user'] = user
        UserDetail.objects.create(**details_data)
        return user

    def to_representation(self, instance):
        # Fetch the linked details (adjust 'userdetails' to your model's related_name if different)
        details = getattr(instance, 'userdetails', None)  # e.g., if FK reverse is 'userdetails'
        if not details:
            details = UserDetail.objects.filter(user=instance).first()  # Fallback query
        return {
            'email': instance.email,
            'account_name': instance.account_name,
            'last_name': details.last_name if details else None,
            'first_name': details.first_name if details else None,
            'contact_number': details.contact_number if details else None,
            'address': details.address if details else None,
        }

class ProductSourcingSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductSourcing

        fields = '__all__'



class ProductSellingSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductSelling

        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order

        fields = '__all__'

        read_only_fields = ['buyer']
