# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)


    def __str__(self):
        return self.first
