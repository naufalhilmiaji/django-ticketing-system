from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from .models import User


class UserAdminForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"../password/\">this form</a>."))

    def clean_password(self) -> str:
        return self.initial["password"]


class UserAdmin(DjangoUserAdmin):
    form = UserAdminForm
    fieldsets = (
        (None, {'fields': ('name', 'email', 'mobile_number', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}),
    )

    list_display = ('email', 'name', 'is_active', )
    search_fields = ('name', 'email', )
    ordering = ('email', 'name', )


admin.site.register(User, UserAdmin)
