import sqlite3
from Library.Book import Book

class DataBase:
    _db = None
    _cursor = None

    def __init__(self, dbname: str):
        self._db = sqlite3.connect(dbname)
        self._cursor = self._db.cursor()

    def AddBook(self, book: Book):
        query = "Insert Into Books (Title, Authors, Year, Pages, Publisher)" \
                "Values (?, ?, ?, ?, ?)"
        self._cursor.execute(query, [book.GetTitle(), book.GetAuthor(),
                                     book.GetYear(), book.GetPages(), ''])
        self._db.commit()

    def GetAllBook(self) -> list:
        self._cursor.execute("Select * From Books")
        ls = []
        for row in self._cursor.fetchall():
            book = Book(title=row[1], author=row[2],
                        publisher='', year=row[4], pages=row[5])
            ls.append(book)
        return ls

    def SimpleFilter(self, field: str, value: str) -> Book:
        query = "Select Title, Authors, Year, Pages, Publisher From Books " \
                "Where " + field + " = '" + value + "'"
        self._cursor.execute(query)
        row = self._cursor.fetchone()
        if row is None:
            raise Exception()
        book = Book(title=row[0], author=row[1],
                    publisher='', year=row[2], pages=row[3])
        return book



