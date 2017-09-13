from django.apps import AppConfig


class BooksConfig(AppConfig):
    name = 'booksapp.books'
    verbose_name = 'Books'

    def ready(self):
        pass
