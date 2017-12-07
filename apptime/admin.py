# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from apptime.models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ["first","created","latest"]
    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)