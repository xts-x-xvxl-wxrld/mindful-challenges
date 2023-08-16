from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Challenge, Reflection
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Challenge)
admin.site.register(Reflection)