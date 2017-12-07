# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Post(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    latest = models.DateTimeField(auto_now=True,auto_now_add=False)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    def __str__(self):
        return self.first