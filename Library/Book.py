import re
from Library.LibraryException import BookException


class Book:
    _author = ''
    _title = ''
    _publisher = ''
    _year = None
    _pages = None

    def __init__(self, author: str = '', title: str = '', year: int = 1900, pages: int = 1, publisher: str = ''):
        self.SetAuthor(author=author)
        self.SetTitle(title=title)
        self.SetYear(year=year)
        self.SetPages(pages=pages)
        self._publisher = publisher

    def __str__(self) -> str:
        return "Title: " + self._title + " || Author: " + self._author

    def __eq__(self, other):
        if type(other) != Book:
            return False
        return self._author == other._author and self._title == other._title and self._publisher == other._publisher

    def SetTitle(self, title: str):
        try:
            self._title = self._PrepareString(s=title)
        except TypeError:
            raise BookException(code=1, msg='Bad Type for Title')

    def GetTitle(self) -> str:
        return self._title

    def SetAuthor(self, author: str):
        self._author = self._PrepareString(s=author)

    def GetAuthor(self) -> str:
        return self._author

    def _PrepareString(self, s: str)-> str:
        if type(s) != str:
            raise TypeError()
        return re.sub('[ \t]+', ' ', s).strip().title()

    def SetYear(self, year: int):
        try:
            self._year = self._PrepareInt(year, 1900, 2020)
        except TypeError:
            raise BookException(21, 'Year Have Bad Type')
        except ValueError:
            raise BookException(22, 'Year Have Bad Value')
        except:
            raise BookException(50, 'Unknown Error')

    def GetYear(self) -> int:
        return self._year

    def SetPages(self, pages: int):
        try:
            self._pages = self._PrepareInt(pages, 1, 5000)
        except TypeError:
            raise BookException(31, 'Pages Have Bad Type')
        except ValueError:
            raise BookException(32, 'Pages Have Bad Value')
        except:
            raise BookException(50, 'Unknown Error')

    def GetPages(self) -> int:
        return self._pages

    def _PrepareInt(self, value: int, a: int, b: int) -> int:
        if type(value) != int:
            raise TypeError()
        if value < a or value > b:
            raise ValueError()
        return value