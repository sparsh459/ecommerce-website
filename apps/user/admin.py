from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.user.forms import UserDetailsChangeForm, UserDetailsCreationForm
from apps.user.models import User


class UserDetailsAdmin(UserAdmin):
    """
    Custom admin for User model
    """

    form = UserDetailsChangeForm
    add_form = UserDetailsCreationForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "mobile",
                    "password",
                    "role",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("verified", "is_active", "is_staff", "is_superuser")},
        ),
        ("Groups", {"fields": ("groups",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )

    list_display = (
        "id",
        "email",
        "name",
        "mobile",
        "verified",
        "is_active",
        "date_joined",
    )
    list_filter = ("is_staff", "is_superuser", "is_active", "role")
    search_fields = ("email", "name", "mobile")
    ordering = ("email",)

admin.site.register(User, UserDetailsAdmin)