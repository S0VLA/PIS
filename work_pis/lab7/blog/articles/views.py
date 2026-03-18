# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from models import Article

def archive(request):
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    if not request.user.is_authenticated():
        raise Http404
    if request.method == "POST":
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }
        if form['title'] and form['text']:
            if Article.objects.filter(title=form['title']).exists():
                form['errors'] = u"Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})
            article = Article.objects.create(
                title=form['title'],
                text=form['text'],
                author=request.user
            )
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        return render(request, 'create_post.html', {})

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', ''),
            'email': request.POST.get('email', ''),
            'password': request.POST.get('password', ''),
        }
        if form['username'] and form['email'] and form['password']:
            try:
                User.objects.get(username=form['username'])
                form['errors'] = u"Пользователь с таким именем уже существует"
                return render(request, 'register.html', {'form': form})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=form['username'],
                    email=form['email'],
                    password=form['password']
                )
                user = authenticate(username=form['username'], password=form['password'])
                if user is not None:
                    login(request, user)
                return redirect('archive')
        else:
            form['errors'] = u"Заполните все поля"
            return render(request, 'register.html', {'form': form})
    else:
        return render(request, 'register.html', {})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get('username', ''),
            'password': request.POST.get('password', ''),
        }
        if form['username'] and form['password']:
            user = authenticate(username=form['username'], password=form['password'])
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                form['errors'] = u"Неверное имя пользователя или пароль"
                return render(request, 'login.html', {'form': form})
        else:
            form['errors'] = u"Заполните все поля"
            return render(request, 'login.html', {'form': form})
    else:
        return render(request, 'login.html', {})