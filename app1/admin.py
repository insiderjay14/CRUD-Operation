from django.contrib import admin
from django.db import models
from app1.models import register

# Register your models here.

class registeradmin(admin.ModelAdmin):
    list_display=['username','password','email','phone','gender']
admin.site.register(register,registeradmin)