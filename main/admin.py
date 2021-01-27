from django.contrib import admin

# Register your models here.

from .models import ToDo, Books

admin.site.register(ToDo)
admin.site.register(Books)