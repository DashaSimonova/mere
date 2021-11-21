import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication
from random import randint


class Figures(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('Ui.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_round(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        radius = randint(3, 80)
        qp.drawEllipse(randint(0, 400), randint(0, 300), radius, radius)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Figures()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
