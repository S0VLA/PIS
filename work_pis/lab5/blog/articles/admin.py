# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
    list_filter = ('author', 'created_date')
    search_fields = ('title', 'text')

admin.site.register(Article, ArticleAdmin)