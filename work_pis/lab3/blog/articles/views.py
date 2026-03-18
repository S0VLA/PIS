# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Article

def archive(request):
    posts = Article.objects.all().order_by('-created_date')  # сначала новые
    return render(request, 'archive.html', {'posts': posts})