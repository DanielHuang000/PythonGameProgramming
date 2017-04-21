# QCalenderWidget
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate

class Cal(QWidget):
    def __init__(self):
        super(Cal, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("Calender Demo")

        self.cal1 = QCalendarWidget(self)
        self.cal1.setGridVisible(True)
        self.cal1.move(20,20)
        self.cal1.clicked[QDate].connect(self.showDate)

        self.label = QLabel(self)
        date = self.cal1.selectedDate()
        self.label.setText(date.toString())
        self.label.move(20,220)
        self.show()

    def showDate(self, date):
        self.label.setText(date.toString())



if __name__ == "__main__":
        app = QApplication(sys.argv)
        cal = Cal()
        sys.exit(app.exec_())
