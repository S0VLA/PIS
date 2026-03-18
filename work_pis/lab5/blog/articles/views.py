# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from models import Article

def archive(request):
    """
    Представление для главной страницы со списком всех статей.
    """
    posts = Article.objects.all().order_by('-created_date')
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    """
    Представление для отображения отдельной статьи по её ID.
    Если статья не найдена, возвращает 404.
    """
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        raise Http404

def create_post(request):
    """
    Представление для создания новой статьи.
    Доступно только авторизованным пользователям.
    При GET-запросе отображает пустую форму.
    При POST-запросе проверяет данные и создаёт статью.
    """
    # Проверяем, авторизован ли пользователь (в Django 1.4 используется метод)
    if not request.user.is_authenticated():
        # Если не авторизован, возвращаем 404 (по методичке)
        raise Http404

    if request.method == "POST":
        # Собираем данные из POST-запроса
        form = {
            'title': request.POST.get('title', ''),
            'text': request.POST.get('text', '')
        }

        # Валидация: проверяем, что поля не пустые
        if form['title'] and form['text']:
            # Дополнительная проверка на уникальность заголовка
            if Article.objects.filter(title=form['title']).exists():
                form['errors'] = u"Статья с таким названием уже существует"
                return render(request, 'create_post.html', {'form': form})

            # Создаём статью (автор — текущий пользователь)
            article = Article.objects.create(
                title=form['title'],
                text=form['text'],
                author=request.user
            )
            # Перенаправляем на страницу созданной статьи
            return redirect('get_article', article_id=article.id)
        else:
            # Ошибка: не все поля заполнены
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})
    else:
        # GET-запрос: просто показываем пустую форму
        return render(request, 'create_post.html', {})