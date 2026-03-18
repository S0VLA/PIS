# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    author = models.ForeignKey(User, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')

    def __unicode__(self):
        return u'%s: %s' % (self.author.username, self.title)

    def get_excerpt(self):
        if len(self.text) > 140:
            return self.text[:140] + '...'
        return self.text

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'