# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    """docstring for User"models.Model def __init__(self, arg):
        super(User,models.Model.__init__()
        self.arg = arg"""
    username = models.CharField(max_length=30)
    headImg = models.FileField(upload_to='./upload/')

    def __unicode__(self):
        return self.username
