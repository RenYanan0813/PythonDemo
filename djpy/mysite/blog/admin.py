# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import BlogPost, BlogPostAdmin

# Register your models here.
# admin.site.register(BlogPost)
admin.site.register(BlogPost, BlogPostAdmin)
