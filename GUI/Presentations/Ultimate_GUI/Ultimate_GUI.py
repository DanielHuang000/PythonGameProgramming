
import sys
import time
from PyQt5.QtWidgets import QApplication, QTabWidget, QWidget, QDockWidget, QCalendarWidget,\
    QPushButton, QHBoxLayout, QFormLayout, QLineEdit, QCheckBox, QLabel, QComboBox, QProgressBar
from PyQt5.QtCore import QDate, QThread, pyqtSignal


class Thread(QThread):
        set_max = pyqtSignal(int)
        update = pyqtSignal(int)

        def __init__(self):
                QThread.__init__(self)

        def __del__(self):
                self.wait()

        def run(self):
                self.update.emit(100)
                for index in range(1, 101):
                        self.update.emit(index)
                        time.sleep(0.01)
                self.update.emit(0)


class MainWindow(QWidget):

        def __init__(self):
                super(self.__class__, self).__init__()
                self.setupUi()
                self._tutorial_thread = Thread()
                self._tutorial_thread.set_max.connect(self.set_max)
                self._tutorial_thread.update.connect(self.set_value)

        def setupUi(self):
                self.progress_bar = QProgressBar()

        def start(self):
                self._tutorial_thread.start()

        def stop(self):
                self._tutorial_thread.terminate()

        def set_max(self, data):
                self.progress_bar.setMaximum(data)

        def set_value(self, data):
                self.progress_bar.setValue(data)


class Final(QTabWidget):
    def __init__(self):
        super(Final, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, "Download Page")
        self.addTab(self.tab2, "History")

        self.tab_1()
        self.tab_2()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.closeTab)

        self.Cdate = QDate.currentDate().toString()
        # self.Cdate = self.Cdate[3:4] + self.Cdate[5:]


        self.cal_dict = {}
        self.cal_list = []

    def closeTab(self, currentIndex):
        currentQWidget = self.widget(currentIndex)
        currentQWidget.deleteLater()
        self.removeTab(currentIndex)

    def tab_1(self):
        self.layout = QFormLayout()
        self.combo = QComboBox()
        self.combo.addItems(["Download stuff on the platform", "Download stuff on internet"])
        self.layout.addRow(self.combo)
        print("current index: " + str(self.combo.currentIndex()))

        self.line = QLineEdit()
        self.label = QLabel(self)
        self.label.setText("Website Link")
        self.layout.addRow(self.label, self.line)
        self.line.setPlaceholderText("Please paste the link here")
        self.line.hide()
        self.label.hide()

        self.check01 = QCheckBox(self)
        self.check02 = QCheckBox(self)
        self.label01 = QLabel(self)
        self.label01.setText("E-Book A")
        self.label02 = QLabel(self)
        self.label02.setText("Movie A")
        self.d = QDockWidget(self)
        self.Dlabel = QLabel(" Download Complete! ",self)

        self.layout.addRow(self.label01, self.check01)
        self.layout.addRow(self.label02, self.check02)

        self.combo.currentIndexChanged.connect(self.choose)

        self.d.move(20,20)
        self.d.resize(250,50)
        self.d.setWidget(self.Dlabel)
        self.d.setFloating(True)
        self.d.hide()

        self.Download_button = QPushButton("Download", self)
        self.m = MainWindow()
        self.layout.addRow(self.m.progress_bar)

        self.layout.addRow(self.Download_button)
        self.Download_button.clicked.connect(self.startDownload)

        self.tab1.setLayout(self.layout)
        
    def startDownload(self):
        self.m.start()
        time.sleep(1)
        self.d.show()
        self.addDownload()

    def addDownload(self):
        if self.check01.isChecked() and (self.label01.text() + " downloaded on " + self.Cdate) not in self.cal_list:
            self.cal_list.append(self.label01.text() + " downloaded on " + self.Cdate)

        if self.check02.isChecked() and (self.label02.text() + " downloaded on " + self.Cdate) not in self.cal_list:
            self.cal_list.append(self.label02.text() + " downloaded on " + self.Cdate)

        elif self.line.text() != "" and ("item downloaded from link " + self.line.text() + " on " + self.date) not in self.cal_list:
            self.cal_list.append("item downloaded from link " + self.line.text() + " on " + self.Cdate)

        self.cal_dict[self.Cdate] = self.cal_list

        print(self.cal_dict)


    def choose(self):
        if (self.combo.currentIndex()==0):
            self.line.hide()
            self.label.hide()
            self.label01.show()
            self.label02.show()
            self.check01.show()
            self.check02.show()

        elif (self.combo.currentIndex()==1):
            self.line.show()
            self.label.show()
            self.label01.hide()
            self.label02.hide()
            self.check01.hide()
            self.check02.hide()

    def tab_2(self):
        self.layout2 = QFormLayout()
        self.h_layout = QHBoxLayout()
        self.calendar = QCalendarWidget(self)
        self.Clabel = QLabel(self)
        Sdate = self.calendar.selectedDate().toString()

        self.h_layout.addWidget(self.calendar)
        self.layout2.addRow(self.h_layout)
        self.layout2.addRow(self.Clabel)
        self.tab2.setLayout(self.layout2)

        self.calendar.clicked[QDate].connect(self.showDownload)

    def showDownload(self,Sdate):
        Sdate = Sdate.toString()
        if Sdate in self.cal_dict.keys():
            # self.layout3 = QFormLayout()
            self.list = self.cal_dict[Sdate]

            for num, x in enumerate(self.list):
                self.Clabel = QLabel(self)
                self.layout2.addRow(self.Clabel)
                self.Clabel.setText(x)
            # self.tab2.setLayout(self.layout3)

        elif Sdate not in self.cal_dict.keys():
            self.Clabel.setText("No items downloaded on " + Sdate)
            print(Sdate)
            # self.Clabel.deleteLater()

    def init(self):
        self.setWindowTitle('Download Platform')
        self.show()

app = QApplication(sys.argv)
w = Final()
w.init()
exit(app.exec_())
