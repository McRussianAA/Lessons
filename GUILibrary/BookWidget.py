from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QSpinBox
from PyQt5.QtWidgets import QErrorMessage
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from Library.Book import Book
from GUILibrary.GuiSignals import BookSignals


class BookWidget (QWidget):
    '''
    Object BookWidget - Gui Interface for Add Book.
    Have Field for information....
    '''
    _lbl_author = None
    _lbl_title = None
    _lbl_year = None
    _lbl_pages = None
    _lbl_publisher = None
    _text_author = None
    _text_title = None
    _text_publisher = None
    _spin_year = None
    _spin_pages = None
    _btn_ok = None
    _signals_book = None
    _book = None

    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Информация о книге")
        self.setMinimumWidth(500)
        self.setMinimumHeight(300)
        self.setToolTip("Information from Book")
        self._InitWidget()
        self._signals_book = BookSignals()

    def Show(self):
        self._Clear()
        self.show()

    def Close(self):
        self.close()

    def _InitWidget(self):
        self._lbl_author = QLabel(self)
        self._lbl_author.setGeometry(20, 20, 120, 30)
        self._lbl_author.setText('Enter Author: ')
        self._text_author = QLineEdit(self)
        self._text_author.setGeometry(150, 20, 320, 30)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self._lbl_author)
        hbox1.addSpacing(10)
        hbox1.addWidget(self._text_author)

        self._lbl_title = QLabel(self)
        self._lbl_title.setGeometry(20, 70, 120, 30)
        self._lbl_title.setText("Enter Title for Book")
        self._text_title = QLineEdit(self)
        self._text_title.setGeometry(150, 70, 320, 30)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self._lbl_title)
        hbox2.addSpacing(10)
        hbox2.addWidget(self._text_title)

        self._lbl_year = QLabel(self)
        self._lbl_year.setGeometry(20, 120, 150, 30)
        self._lbl_year.setText("Select Year Publisher")
        self._spin_year = QSpinBox(self)
        self._spin_year.setGeometry(40, 150, 80, 30)
        self._spin_year.setMaximum(2020)
        self._spin_year.setMinimum(1950)
        self._spin_year.setValue(2010)
        grid = QGridLayout()
        grid.addWidget(self._lbl_year, 1, 1)
        grid.addWidget(self._spin_year, 2, 1)

        self._btn_ok = QPushButton(self)
        self._btn_ok.setGeometry(400, 350, 80, 30)
        self._btn_ok.setText('OK')
        self._btn_ok.clicked.connect(self._HandleButtonOK)

        hbox3 = QHBoxLayout()
        hbox3.addSpacing(10)
        hbox3.addWidget(self._btn_ok)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addSpacing(10)
        vbox.addLayout(hbox2)
        vbox.addSpacing(10)
        vbox.addLayout(grid)
        vbox.addSpacing(10)
        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def _HandleButtonOK(self):
        author = self._text_author.text()
        title = self._text_title.text()
        if author == '' or title == '':
            error = QErrorMessage(self)
            error.showMessage("Error Enter", 'Empty Filed...')
            return None

        year = self._spin_year.value()
        try:
            self._book = Book(author=author, title=title, year=year)

            self._signals_book.haveBook.emit()
            self.close()
        except:
            error = QErrorMessage(self)
            error.showMessage("Error Enter", 'Empty Filed...')

    def _Clear(self):
        self._text_title.clear()
        self._text_author.clear()
        self._spin_year.setValue(2010)

    def GetBook(self) -> Book:
        return self._book
