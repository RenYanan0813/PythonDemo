# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse
from disk.models import User

# Create your views here.
class UserForm(forms.Form):
    """docstring for UserForm" def __init__(self, arg):
        super(UserForm,.__init__()
        self.arg = arg"""
    username = forms.CharField()
    headImg = forms.FileField()

def register1(request):
    # return render_to_response('register.html',{})
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            #获取表单信息
            username = uf.cleaned_data['username']
            headImg = uf.cleaned_data['headImg']
            #写入数据库
            user = User()
            user.username = username
            user.headImg = headImg
            user.save()
            return HttpResponse('upload ok!')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf':uf})
