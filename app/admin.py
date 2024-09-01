from django.contrib import admin
from django.http import HttpRequest
from . import models

@admin.register(models.addUserData)
class addUserDataAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'your_email', 'your_contact']
    
    def has_add_permission(self, *args, **kwargs):
        return False