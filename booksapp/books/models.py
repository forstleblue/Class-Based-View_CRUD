# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):
    #  TODO: Do not forget to add a validator for isbn field,
    #  it may only contain digits and hyphens!
    isbn = models.CharField(_('ISBN'), max_length=13, unique=True, primary_key=True)
    title = models.CharField(_('Book\'s title'), max_length=128)
    publisher = models.CharField(_('Publisher'), max_length=64)
    author = models.CharField(_('Author'), max_length=64)
    pages = models.IntegerField(_('Pages'), default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:detail', kwargs={'isbn': self.isbn})
