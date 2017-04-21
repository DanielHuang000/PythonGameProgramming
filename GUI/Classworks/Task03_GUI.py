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

      self.line1 = QLineEdit(self)
      self.line1.resize(300,30)
      self.line1.move(250, 50)
      self.combo1 = QComboBox(self)
      self.combo1.resize(150, 40)
      self.combo1.move(50, 50)


      for x in self.dictStore.keys():
          self.combo1.addItem(x)

      self.combo1.currentIndexChanged.connect(self.getOutput)


      self.show()


   def getOutput(self):
       self.key = self.combo1.currentText()
       self.item = self.dictStore[self.key]
       self.line1.setText(self.key + " cost " + self.item)


# --- main program
app = QApplication(sys.argv)
ex = T03()
sys.exit(app.exec_())
