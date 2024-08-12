from django.contrib import admin
from apps.user.models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    fieldsets = None
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("password1", "password2", "username", "first_name", "last_name", "is_staff")
        }),
    )
    
    list_display = ("username", "first_name", "last_name", "is_staff")


admin.site.register(User, CustomUserAdmin)
