
import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QDockWidget, QCalendarWidget,\
    QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, QCheckBox, QLabel, QComboBox
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


class Dock(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def init(self):
        self.setGeometry(300,300,300,250)
        self.setStyleSheet('background-color:white;')

        self.button1 = QPushButton('Button', self)
        self.button1.resize(50,50)


        self.dock1 = QDockWidget('My First Dock', self)
        self.dock1.move(20,20)
        self.dock1.resize(50,50)
        self.dock1.setWidget(self.button1)
        self.dock1.setFloating(False)
        self.dock1.setFeatures(self.dock1.DockWidgetClosable|self.dock1.DockWidgetMovable)
        self.dock1.setFeatures(self.dock1.AllDockWidgetFeatures)

        self.show()

class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()


        self.addTab(self.tab1, "Download Page")
        self.addTab(self.tab2, "History")


        self.tab_1()
        self.tab_2()
        # self.tab_3()
        # self.tab_4()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        layout = QFormLayout()
        line = QLineEdit()
        combo = QComboBox()
        combo.addItems(["Download stuff on the platform", "Download stuff on internet"])
        layout.addRow(combo)
        layout.addRow("Website Link", line)
        # layout.addRow("", QLineEdit())
        line.setPlaceholderText("Please paste the link here")

        self.tab1.setLayout(layout)


    def tab_2(self):
        layout = QFormLayout()
        h_layout = QHBoxLayout()
        calendar = QCalendarWidget(self)
        h_layout.addWidget(calendar)
        # h_layout.addWidget(QRadioButton("Female"))
        layout.addRow(h_layout)
        self.tab2.setLayout(layout)

    """
    def tab_3(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Majors"))
        layout.addWidget(QCheckBox("Engineer"))
        layout.addWidget(QCheckBox("Physic"))
        self.tab3.setLayout(layout)

    def tab_4(self):
        layout = QFormLayout()
        layout.addRow("Female guardian", QLineEdit())
        layout.addRow("Male guardian", QLineEdit())
        self.tab4.setLayout(layout)
    """

    def init(self):
        self.setWindowTitle('Download Platform')
        self.show()

app = QApplication(sys.argv)
w = Tab()
w.init()
exit(app.exec_())
