import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox, QComboBox, QLineEdit, QLabel, QPlainTextEdit
from PyQt5.QtWidgets import *


class T03 (QWidget):
  def __init__(self):
      super().__init__()
      self.dictStore = {}
      self.text = open('Task03.csv').read()
      self.text = self.text.replace("\n","")
      self.textList = self.text.split(",")
      self.count = 0

      while self.count < len(self.textList):
          self.dictStore[self.textList[self.count]] = self.textList[self.count + 1]
          self.count += 2

      self.initUI()
      self.check = True



  def initUI(self):
      self.setGeometry(300, 300, 700, 400)
      self.setWindowTitle('Book Store GUI')

      self.combo1 = QComboBox(self)
      self.combo1.resize(150, 40)
      self.combo1.move(50, 50)

      self.line1 = QLineEdit(self)

      for x in self.dictStore.keys():
          self.combo1.addItem(x)

      self.show()


















# --- main program
app = QApplication(sys.argv)
ex = T03()
sys.exit(app.exec_())
