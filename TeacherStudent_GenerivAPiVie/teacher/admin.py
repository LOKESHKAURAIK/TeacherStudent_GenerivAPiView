from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'tname', 'email', 'subject', 'address']