from PyQt5.QtCore import pyqtSignal, QObject

class BookSignals(QObject):
    haveBook = pyqtSignal()
