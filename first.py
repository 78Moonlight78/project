import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.show_calendar()

    def show_zam(self):
        uic.loadUi('zametki.ui', self)
        self.btn_calendar.clicked.connect(self.show_calendar)
        self.btn_dv.clicked.connect(self.show_developments)

    def show_calendar(self):
        uic.loadUi('calendar.ui', self)
        self.btn_zam.clicked.connect(self.show_zam)
        self.btn_dv.clicked.connect(self.show_developments)

    def show_developments(self):
        uic.loadUi('developments.ui', self)
        self.btn_calendar.clicked.connect(self.show_calendar)
        self.btn_zam.clicked.connect(self.show_zam)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())