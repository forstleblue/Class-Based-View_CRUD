from django.test import TestCase

from booksapp.books.models import Book


class TestBookViews(TestCase):

    def setUp(self):
        Book.objects.create(
            isbn='123456',
            title='Abc',
            publisher='Bca',
            author='Cba',
            pages=100,
        )

    def test_index(self):
        resp = self.client.get('/books/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.context['book_list']), 1)

    def test_detail(self):
        resp = self.client.get('/books/123456/')
        self.assertEqual(resp.status_code, 200)

    def test_create(self):
        resp = self.client.get('/books/create/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/books/create/', {
            'isbn': '111',
            'title': 'AbcbA',
            'publisher': 'Bca',
            'author': 'Cba',
            'pages': 10,
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'AbcbA')
        self.assertContains(resp, 'The book created successfully')

    def test_create_field_required(self):
        resp = self.client.post('/books/create/', {
            'isbn': '',
            'title': 'AbcbA',
            'publisher': 'Hjs',
            'author': 'Cba',
            'pages': 10,
        }, follow=True)
        self.assertContains(resp, 'The creation has failed')
        self.assertFormError(resp, 'form', 'isbn',
                             'This field is required.')

    def test_create_err_isbn_exists(self):
        resp = self.client.post('/books/create/', {
            'isbn': '123456',
            'title': 'AbcbA',
            'publisher': '',
            'author': 'Cba',
            'pages': 10,
        }, follow=True)
        self.assertContains(resp, 'The creation has failed')
        self.assertFormError(resp, 'form', 'isbn',
                             'Book with this ISBN already exists.')

    def test_update(self):
        resp = self.client.get('/books/update/123456/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/books/update/123456/', {
            'isbn': '123456',
            'title': 'AbcbA',
            'publisher': 'Bca',
            'author': 'A new author',
            'pages': 10,
        }, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'A new author')
        self.assertContains(resp, 'The book updated successfully')

    def test_update_wrong_pages(self):
        resp = self.client.post('/books/update/123456/', {
            'isbn': '123456',
            'title': 'AbcbA',
            'publisher': 'Bca',
            'author': 'A new author',
            'pages': 'abc',
        }, follow=True)
        self.assertContains(resp, 'The update has failed')
        self.assertFormError(resp, 'form', 'pages',
                             'Enter a whole number.')

    def test_delete(self):
        resp = self.client.get('/books/delete/123456/')
        self.assertEqual(resp.status_code, 200)

        resp = self.client.post('/books/delete/123456/', follow=True)
        self.assertContains(resp, 'The book deleted successfully')
