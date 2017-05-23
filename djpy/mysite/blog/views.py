# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.shortcuts import render, render_to_response
from .models import *

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def index(req):
    # get all blogpost objects
    blog_list = BlogPost.objects.all()
    template = loader.get_template('index.html')

    context = {
        'blog_list': blog_list
    }
    return HttpResponse(template.render(context, req))
    # blog_list = BlogPost.objects.all()
    # return HttpResponse("hello world! YOU're at the blog index")
    # return render_to_response('index.html', {'blog_list': blog_list})
