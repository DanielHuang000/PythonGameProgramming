# QLable

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap

class Lable(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(100,100,900,700)
        self.setWindowTitle('gui demo')

        self.lable1 = QLabel(self)
        self.lable1.setText('Python Class')
        self.lable1.move(390, 40)

        self.lable2 = QLabel(self)
        self.lable2.setToolTip('http://goo.gl/pB9kmb')
        self.lable2.setText("<a href='http://goo.gl/pB9kmb'> Surprise URL </a>")
        self.lable2.move(390,90)
        self.lable2.setOpenExternalLinks(True)

        self.lable3 = QLabel(self)
        self.lable3.move(80, 130)
        self.lable3.setPixmap(QPixmap('a.png'))

        self.show()




if __name__ == "__main__":
        app = QApplication(sys.argv)
        Lable = Lable()
        sys.exit(app.exec_())
