from django.contrib import admin

# Register your models here.
from . models import House,Cars,Products
admin.site.register(House)
admin.site.register(Cars)
admin.site.register(Products)

