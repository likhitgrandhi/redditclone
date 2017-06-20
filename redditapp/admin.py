# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.contrib import admin


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post)
