from django.contrib import admin
from . import models
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')

admin.site.register(models.CustomUser, UserAdmin)
