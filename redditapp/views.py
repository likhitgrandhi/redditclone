# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render


# Create your views here.

def index(request):
    context_dict = {'title': "Reddit-JNTU"}
    return render(request, 'reddit/index.html', context_dict)
