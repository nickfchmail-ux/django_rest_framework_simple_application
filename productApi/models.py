from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.conf import settings




class UserProfileManager(BaseUserManager):
    def create_user(self, email, account_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, account_name=account_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, account_name, password):
        user = self.create_user(email, account_name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    account_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["account_name"]

    def __str__(self):
        return self.email

class UserDetail(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=8)
    address = models.CharField(max_length=300)

    def __str__ (self):
        return f"{self.user.email}"

class ProductSourcing(models.Model):


    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_remaining = models.IntegerField()

    def __str__ (self):
        return f"{self.product_name}"

class ProductSelling(models.Model):

    product_source = models.ForeignKey(ProductSourcing, on_delete=models.CASCADE)
    selling_name = models.CharField(max_length=50)
    selling_url_image = models.CharField(max_length=200)
    selling_description = models.CharField(max_length=500)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return f"{self.selling_name} @ ${self.selling_price}"


class Order(models.Model):

    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    buying_product = models.ForeignKey(ProductSelling, on_delete=models.CASCADE)
    buying_quantity = models.IntegerField()
    order_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.buyer.email}"
