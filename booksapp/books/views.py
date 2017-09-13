# -*- coding: utf-8 -*-

"""Books views."""

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from .models import Book
from .forms import UpdateForm
from django.views.generic.edit import FormView

class BookListView(ListView):
    """Show all books."""

    model = Book
    pk_url_kwarg ="isbn"

class BookDetailView(DetailView):
    """Show the requested book."""
    model = Book
    pk_url_kwarg ="isbn"


class BookCreateView(SuccessMessageMixin, CreateView):
    """Create a new book."""
    model = Book
    fields = ['isbn', 'title', 'publisher', 'author', 'pages']
    success_message = 'Book successfully created.'
    form_class = UpdateForm
    def form_valid(self, form):
        isbn = form.cleaned_data['isbn']
        return super(BookCreateView, self).form_valid(form)
    # TODO: make it work
    # TODO: add a message on the page if form is valid: 'The book created successfully!'
    # TODO: add a message on the page if form is invalid: 'The creation has failed.'


class BookUpdateView(SuccessMessageMixin, UpdateView):
    """Update the requested book."""
    model = Book
    fields = ['isbn', 'title', 'publisher', 'author', 'pages']
    success_message = 'Book successfully updated.'
    pk_url_kwarg ="isbn"

    # TODO: make it work
    # TODO: add a message on the page if form is valid: 'The book updated successfully!'
    # TODO: add a message on the page if form is invalid: 'The update has failed.'


class BookDeleteView(DeleteView):
    """Delete the requested book."""
    model = Book
    success_message = 'Book successfully deleted.'
    pk_url_kwarg ="isbn"
    def get_success_url(self):
        return reverse_lazy('books:index')
    # TODO: make it work
    # TODO: add a message on the page if form is valid: 'The book deleted successfully!'
    # TODO: add a message on the page if form is invalid: 'The deletion has failed.'

