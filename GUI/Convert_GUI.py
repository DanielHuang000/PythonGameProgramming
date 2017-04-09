
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox
from PyQt5.QtGui import QIcon

class Example(QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()
      self.check = True

  def initUI(self):
      self.setGeometry(300, 300, 500, 500)
      self.setStyleSheet("background-color:black;")
      self.setWindowTitle('Converter GUI')
      self.btn1 = QPushButton('- SWAP -', self)
      self.btn2 = QPushButton('Convert', self)

      self.setWindowIcon(QIcon("D.png"))

      self.btn1.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
      self.btn2.setStyleSheet('QPushButton {background-color: #A3C1DA; color: black;}')
      self.btn1.setToolTip('Press the button \nto switch')

      self.btn1.resize(100, 50)
      self.btn2.resize(100, 50)
      self.btn1.move(50, 100)
      self.btn2.move(350, 100)

      self.btn1.clicked.connect(self.swap)
      self.btn2.clicked.connect(self.convert)


      # self.text1 = QTextEdit(self)
      # self.text1.resize(200, 40)
      # self.text1.move(50, 250)
      # self.text1.setPlaceholderText("This is a EditText Widget")

      self.num1 = QDoubleSpinBox(self)
      self.num1.setMaximum(99999999)
      self.num1.setMinimum(0.00)
      self.num1.setSuffix(" sec")
      self.num1.resize(200,50)
      self.num1.move(150,250)

      self.num2 = QDoubleSpinBox(self)
      self.num2.setMaximum(999999)
      self.num2.setMinimum(0.00)
      self.num2.setSuffix(" hours")
      self.num2.resize(200,50)
      self.num2.move(150,350)

      self.num1.setStyleSheet('QDoubleSpinBox {background-color: white; color: black;}')
      self.num2.setStyleSheet('QDoubleSpinBox {background-color: black; color: white;}')

      self.show()

  def convert(self):
      if (self.check == True and self.num1.value() is not 0.0):
          self.num2.setValue(self.num1.value()/3600)
          self.num1.setValue(self.num1.minimum())
      elif (self.check == False and self.num2.value() is not 0.0):
          self.num1.setValue(self.num2.value()*3600)
          self.num2.setValue(self.num2.minimum())



  def swap(self):

      if (self.num1.x(), self.num1.y()) == (150,350):
          self.num1.move(150,250)
          self.num2.move(150,350)
          self.check = True
          self.num2.setStyleSheet('QDoubleSpinBox {background-color: black; color: white;}')
          self.num1.setStyleSheet('QDoubleSpinBox {background-color: white; color: black;}')

      elif (self.num1.x(), self.num1.y()) == (150,250):
          self.num1.move(150,350)
          self.num2.move(150,250)
          self.check = False
          self.num2.setStyleSheet('QDoubleSpinBox {background-color: white; color: black;}')
          self.num1.setStyleSheet('QDoubleSpinBox {background-color: black; color: white;}')





# --- main program
app = QApplication(sys.argv)
ex = Example()
sys.exit(app.exec_())
