from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QFileDialog
from PyQt5.QtWidgets import QAction
from GUILibrary import BookWidget
from Library.Book import Book
from DataBase import DataBase

class MainLibraryWindow(QMainWindow):
    _table = None
    _main_menu = None
    _book = None
    _db = None

    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        self.setWindowTitle("My Library")
        self._db = DataBase(dbname='SQLite//library.db')
        self._CreateTable()
        self._CreateMainMenu()
        self._book = BookWidget()
        self._book._signals_book.haveBook.connect(self._HandleNewBook)
        self.show()

    def _CreateTable(self):
        self._table = QTableWidget(self)
        self._table.setGeometry(20, 20, 560, 360)
        self._table.setColumnCount(5)
        self._table.setHorizontalHeaderLabels(["Author", "Title", "Publisher", "Year", "Pages"])
        self._table.setColumnWidth(1, 150)
        self._table.setColumnWidth(2, 150)
        self._table.setColumnWidth(3, 100)
        self._table.setColumnWidth(4, 30)
        self._table.setColumnWidth(5, 30)
        self._FillTableFromDataBase()

    def _CreateMainMenu(self):
        self._main_menu = self.menuBar()
        command_menu = self._main_menu.addMenu("Command")
        add = QAction("Add", self)
        add.setShortcut("Qtrl+Q")
        add.triggered.connect(self._AddNewBook)

        save = QAction("Save", self)
        save.triggered.connect(self._SaveLibrary)

        command_menu.addAction(add)
        command_menu.addAction(save)

    def _SaveLibrary(self):
        fileName = QFileDialog.getOpenFileName(self, "Open File", "", "Image Files (*.txt *.csv)")

    def _AddNewBook(self):
        self._book.Show()

    def _HandleNewBook(self):
        book = self._book.GetBook()
        self._AddBookInTable(book)
        self._db.AddBook(book)

    def _AddBookInTable(self, book: Book):
        count = self._table.rowCount()
        self._table.insertRow(count)
        self._table.setItem(count, 0, QTableWidgetItem(book.GetAuthor()))
        self._table.setItem(count, 1, QTableWidgetItem(book.GetTitle()))
        self._table.setItem(count, 2, QTableWidgetItem(''))
        self._table.setItem(count, 3, QTableWidgetItem(book.GetYear()))
        self._table.setItem(count, 4, QTableWidgetItem(book.GetPages()))

    def _FillTableFromDataBase(self):
        for book in self._db.GetAllBook():
            self._AddBookInTable(book)

