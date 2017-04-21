# QTabWidget

import sys
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, \
    QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QRadioButton, QCheckBox, QLabel

class Tab(QTabWidget):
    def __init__(self):
        super(Tab, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()


        self.addTab(self.tab1, "Contact Details")
        self.addTab(self.tab2, "Personal Details")
        self.addTab(self.tab3, "Educational Details")
        self.addTab(self.tab4, "Family Details")


        self.tab_1()
        self.tab_2()
        self.tab_3()
        self.tab_4()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        layout = QFormLayout()
        layout.addRow("First name", QLineEdit())
        self.tab1.setLayout(layout)


    def tab_2(self):
        layout = QFormLayout()
        gender = QHBoxLayout()
        gender.addWidget(QRadioButton("Male"))
        gender.addWidget(QRadioButton("Female"))
        layout.addRow(QLabel("Gender"), gender)
        self.tab2.setLayout(layout)


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


    def init(self):
        self.show()

app = QApplication(sys.argv)
w = Tab()
w.init()
exit(app.exec_())
