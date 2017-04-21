# QCheckBox
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QPushButton, QCheckBox
from PyQt5.QtGui import QIcon

class CheckDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(400,400,450,350)
        self.setWindowTitle("CheckBox Demonstration")

        # --- add a checkbox
        self.check = QCheckBox("This is a Checkbox",self)
        self.check.setTristate(True) # Allowing tristate
        self.check.resize(250, 30)
        self.check.move(150, 30)
        self.check.stateChanged.connect(self.dosth)
        self.check.setIcon(QIcon("a.png"))

        # --- add a button for reset
        self.btn1 = QPushButton('Reset', self)
        self.btn1.setToolTip("lalala")
        self.btn1.resize(250,90)
        self.btn1.move(100,100)
        self.btn1.clicked.connect(self.reset)

        # --- add a button for disabling/enabling
        self.btn2 = QPushButton("Disable,Enable", self)
        self.btn2.setToolTip("lalalalala")
        self.btn2.resize(250,90)
        self.btn2.move(100,200)
        self.btn2.clicked.connect(self.toggle)

        self.show()

    def dosth(self):
        # if self.check.isChecked():
        #     self.setWindowTitle("The checkbox was checked")
        # else:
        #     self.setWindowTitle("The checkbox was unchecked")

        state = self.check.checkState()

        if state == 0:
            self.setWindowTitle('The checkbox was unchecked')
        elif state == 2:
            self.setWindowTitle('The checkbox was checked')
        else:
            self.setWindowTitle('The checkbox was unchecked')

    def reset(self):
        self.check.setChecked(False)
        self.setWindowTitle("CheckBox Demonstration")

    def toggle(self):

        if self.check.isEnabled():
            self.check.setEnabled(False)
            self.check.setWindowTitle('The checkbox has been disabled')

        else:
            self.check.setEnabled(True)
            self.setWindowTitle("The checkbox has been enabled")

        # if self.check.isCheckable():
        #     self.check.setCheckable(False)
        #     self.check.setWindowTitle('The checkbox has been disabled')
        #
        # else:
        #     self.check.setCheckable(True)
        #     self.setWindowTitle("The checkbox has been enabled")





app = QApplication(sys.argv)
Demo = CheckDemo()
sys.exit(app.exec_())
