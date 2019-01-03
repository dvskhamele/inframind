from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin

class ProdAdmin(admin.ModelAdmin):
        list_display = ('name','idv', 'cover')

admin.site.register(Prod, ProdAdmin)
admin.site.register(Make)
admin.site.register(RTO)
admin.site.register(Artist)

# Register your models here.
