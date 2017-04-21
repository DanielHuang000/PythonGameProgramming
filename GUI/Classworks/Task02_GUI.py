import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QDoubleSpinBox, QComboBox, QLineEdit



class T02 (QWidget):
  def __init__(self):
      super().__init__()
      self.initUI()
      self.check = True
      self.dictG = {'A+':[97,100],
                    'A':[93,97],
                    'A-':[90,93],
                    'B+':[87,90],
                    'B':[83,87],
                    'B-':[80,83],
                    'C+':[77,80],
                    'C':[73,77],
                    'C-':[70,73],
                    'D+':[67,70],
                    'D':[63,67],
                    'D-':[60,63],
                    'F':[-1,60]}

  def initUI(self):
      self.setGeometry(300, 300, 300, 360)
      self.setWindowTitle('Task 02 GUI')

      self.line1 = QLineEdit(self)
      self.line1.resize(200, 40)
      self.line1.move(50, 50)
      self.line1.setPlaceholderText("Enter Grade 0-100")

      self.line2 = QTextEdit(self)
      self.line2.resize(200, 40)
      self.line2.move(50, 250)
      self.line2.setPlaceholderText("Letter Grade")

      self.line1.textChanged.connect(self.getGrade)
      self.show()

  def getGrade(self):
      if self.line1.text() != '' and self.line1.text() != '-' and '.' not in self.line1.text():
          self.num = (int)(self.line1.text())

          for y, x in self.dictG.items():
              if self.num > x[0] and self.num <= x[1]:
                  self.line2.setText(y)
              elif self.num > 100 or self.num < 0:
                  self.line2.setText("Invalid value")

      elif self.line1.text() == '-':
          self.line2.setText("No negative scores")

      elif '.' in self.line1.text():
          self.line2.setText("Input value should be integers")

# --- main program
app = QApplication(sys.argv)
ex = T02()
sys.exit(app.exec_())
