# 그림 그리기 - 직사각형 그리기 2

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        x1, y1, x2, y2 = 20, 10, 100, 60
        x3, y3 = 20, 90

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.SolidPattern')

        x1, x3 = 150, 150
        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.Dense1Pattern')

        x1, x3 = 280, 280
        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.Dense2Pattern')

        x1, x3 = 20, 20
        y1, y3 = 110, 190
        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.HorPattern')

        x1, x3 = 150, 150
        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.VerPattern')

        x1, x3 = 280, 280
        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.CrossPattern')

        x1, x3 = 20, 20
        y1, y3 = 210, 290
        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.BDiagPattern')

        x1, x3 = 150, 150
        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.FDiagPattern')

        x1, x3 = 280, 280
        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(x1, y1, x2, y2)
        qp.drawText(x3, y3, 'Qt.DiagCrossPattern')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())