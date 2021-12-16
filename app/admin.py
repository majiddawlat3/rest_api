from django.contrib import admin
from app.models import *
# Register your models here.

class AdminEmployee(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('full_name','position','date_hire','salary','boss')


admin.site.register(Boss)
admin.site.register(Employee, AdminEmployee)
