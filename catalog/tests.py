from django.test import TestCase
from django.urls import reverse

from .models import Publisher, Book


class BookPageTests(TestCase):
    def test_book_in_database_appears_on_books_page(self):
        publisher = Publisher.objects.create(name="Test Publisher")
        Book.objects.create(
            publisher=publisher,
            title="The Midnight Library Test Book",
            publication_year=2020,
        )

        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The Midnight Library Test Book")