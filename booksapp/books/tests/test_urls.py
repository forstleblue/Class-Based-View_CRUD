from django.core.urlresolvers import reverse, resolve
from django.test import TestCase


class TestBookURLs(TestCase):
    """Test URL patterns for books app."""

    def test_index_reverse(self):
        self.assertEqual(reverse('books:index'), '/books/')

    def test_index_resolve(self):
        self.assertEqual(resolve('/books/').view_name, 'books:index')

    def test_detail_reverse(self):
        self.assertEqual(
            reverse('books:detail', kwargs={'isbn': '123456'}),
            '/books/123456/')

    def test_detail_resolve(self):
        self.assertEqual(
            resolve('/books/123456/').view_name,
            'books:detail')

    def test_create_reverse(self):
        self.assertEqual(
            reverse('books:create'),
            '/books/create/')

    def test_create_resolve(self):
        self.assertEqual(
            resolve('/books/create/').view_name,
            'books:create')

    def test_update_reverse(self):
        self.assertEqual(
            reverse('books:update', kwargs={'isbn': '123456'}),
            '/books/update/123456/')

    def test_update_resolve(self):
        self.assertEqual(
            resolve('/books/update/123456/').view_name,
            'books:update')

    def test_delete_reverse(self):
        self.assertEqual(
            reverse('books:delete', kwargs={'isbn': '123456'}),
            '/books/delete/123456/')

    def test_delete_resolve(self):
        self.assertEqual(
            resolve('/books/delete/123456/').view_name,
            'books:delete')
