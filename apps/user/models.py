from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models


class UserProfileManager(BaseUserManager):
    """
    User profile manager for User model
    """

    def create_user(self, email=None, password=None):
        # Create a new user
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        # Create a new superuser.
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    User details
    """

    TYPE_CHOICES = [
        ("Admin", "Admin"),
        ("Staff", "Staff"),
        ("OrgUser", "OrgUser"),
        ("AccountManager", "AccountManager"),
    ]
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        max_length=64, null=True, blank=True, help_text="Name of the user"
    )
    email = models.EmailField(
        unique=True, null=True, blank=True, help_text="Email ID of user"
    )
    mobile = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        blank=True,
        validators=[
            RegexValidator(
                regex="^[+][0-9]{10,15}$", message="Enter valid number (max 15 digits)"
            )
        ],
        help_text="Mobile number of user",
    )
    verified = models.BooleanField(default=False, help_text="User verification status")
    role = models.CharField(max_length=16, choices=TYPE_CHOICES, null=True)
    photo = models.TextField(null=True, blank=True, help_text="photo file field")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserProfileManager()

    USERNAME_FIELD = "email"

    class Meta:
        verbose_name_plural = "User details"

    def __str__(self):
        return str(self.name)

    def clean(self):
        if not self.email and not self.mobile:
            raise ValidationError("Even one of email or mobile should have a value.")
        return super().clean()

