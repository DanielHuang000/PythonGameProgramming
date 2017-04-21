import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox, QComboBox



class T01 (QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()
      self.check = True

  def initUI(self):
      self.setGeometry(300, 300, 500, 500)
      # self.setStyleSheet("background-color:black;")
      self.setWindowTitle('Task 01 GUI')
      self.btn1 = QPushButton('Button A', self)
      self.btn2 = QPushButton('Button B', self)

      self.btn1.resize(100, 50)
      self.btn2.resize(100, 50)
      self.btn1.move(50, 100)
      self.btn2.move(350, 100)

      self.btn1.clicked.connect(self.A)
      self.btn2.clicked.connect(self.B)

      self.show()

  def A(self):
      self.setWindowTitle("Button A was pressed")

  def B(self):
      self.setWindowTitle("Button B was pressed")





# --- main program
app = QApplication(sys.argv)
ex = T01()
sys.exit(app.exec_())
