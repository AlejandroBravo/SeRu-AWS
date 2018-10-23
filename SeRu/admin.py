# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User,Post,Vehiculo
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(Post)
admin.site.register(Vehiculo)
