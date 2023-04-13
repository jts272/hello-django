from django.contrib import admin
# 'From the current dir's models module, import the Item class'
from .models import Item

# Register your models here.
admin.site.register(Item)
