from Library.Book import Book


class Belletristic(Book):
    _price = 0

    def __init__(self, author: str = 0, title: str = '', year: int = 0, pages: int = 0, publisher: str = '',
                 price: float = 0):
        Book.__init__(self, author=author, title=title, year=year, pages=pages, publisher=publisher)
        self._price = price

    def __str__(self):
        return Book.__str__(self) + " || Price: " + str(self._price)

    def SetPrice(self, price: float):
        self._price = price

    def GetPrice(self) -> float:
        return self._price

