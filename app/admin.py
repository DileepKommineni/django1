# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Registration
from django.contrib import admin

# Register your models here.
#class Regadmin(admin.ModelAdmin):
#    list_display = ["first","created"]
#    class Meta:
#        module = Registration
admin.site.register(Registration)