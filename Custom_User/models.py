from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password, check_password


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.password = make_password(user.password)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        superuser = self.model(email=email, **extra_fields)

        superuser.set_password(password)
        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
        return superuser


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    password = models.CharField(max_length=300)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    pincode = models.IntegerField()
    phone_number = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'address', 'city', 'country', 'pincode', 'state']
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()

