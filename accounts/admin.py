from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import UserBalance
# Register your models here.

class UserInLine(admin.StackedInline):
    model = UserBalance
    can_delete = False
    verbose_name_plural = 'user'

class UserAdmin(BaseUserAdmin):
    inlines = (UserInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
