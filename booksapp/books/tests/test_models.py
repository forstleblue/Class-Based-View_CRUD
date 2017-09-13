from django.test import TestCase

from booksapp.books.models import Book


class TestBook(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            isbn='0132350882',
            title='Clean Code',
            publisher='Prentice Hall',
            author='Robert C. Martin',
            pages=464,
        )

    def test__str__(self):
        self.assertEqual(self.book.__str__(), 'Clean Code')

    def test_get_absolute_url(self):
        self.assertEqual(
            self.book.get_absolute_url(),
            '/books/0132350882/'
        )

    def test_title(self):
        self.assertEqual(self.book.title, 'Clean Code')
