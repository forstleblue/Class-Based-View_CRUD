# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$',
        view=views.BookListView.as_view(),
        name='index'),
    url(r'^(?P<isbn>[\d\-]+)/$',
        view=views.BookDetailView.as_view(),
        name='detail'),
    url(r'^create/$',
        view=views.BookCreateView.as_view(),
        name='create'),
    url(r'^update/(?P<isbn>[\d\-]+)/$',
        view=views.BookUpdateView.as_view(),
        name='update'),
    url(r'^delete/(?P<isbn>[\d\-]+)/$',
        view=views.BookDeleteView.as_view(),
        name='delete'),
]
