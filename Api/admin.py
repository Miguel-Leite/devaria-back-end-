from django.contrib import admin

from .models import Module, Courses

admin.site.register([Module,Courses])