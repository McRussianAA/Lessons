from unittest import TestCase
from Library.LibraryException import BookException
from Library.Book import Book


class TestBook(TestCase):
    def test_SetYear(self):
        book = Book(year=2000, pages=100)
        self.assertRaises(BookException, book.SetYear, ('reeerre'))
        self.assertRaises(BookException, book.SetYear, (-9))
        self.assertRaises(BookException, book.SetYear, (2300))

    def test_SetPages(self):
        book = Book(year=2000, pages=100)
        self.assertRaises(BookException, book.SetPages, ('reeerre'))
        self.assertRaises(BookException, book.SetPages, (-9))
        self.assertRaises(BookException, book.SetPages, (5300))

    def test_GetPages(self):
        book = Book(year=2000, pages=100)
        self.assertEqual(100, book.GetPages())
