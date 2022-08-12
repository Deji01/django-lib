from django.contrib import admin
from .models import Book, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)
admin.site.register(Book)