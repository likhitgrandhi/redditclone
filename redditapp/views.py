# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render


# Create your views here.

def index(request):
    category_list = Category.objects.all()
    context_dict = {'title': "Reddit-JNTU", 'categories': category_list}
    return render(request, 'reddit/index.html', context_dict)


def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category_list = Category.objects.all()
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
        context_dict['categories'] = category_list
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['posts'] = None

    return render(request, 'reddit/category.html', context_dict)
