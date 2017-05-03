# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interest.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_interestUI(object):
    def setupUi(self, interestUI):
        interestUI.setObjectName("interestUI")
        interestUI.resize(400, 300)
        interestUI.setStyleSheet("QWidget{\n"
            "background-color: #0D56A6;\n"
            "\n"
            "gridline-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "}\n"
            "\n"
            "QDoubleSpinBox{\n"
            "background-color:#FFFFFF;\n"
            "\n"
            "}\n"
            "\n"
            "QComboBox{\n"
            "font: 14pt \"Helvetica\";\n"
            "background-color: #FFFFFF;\n"
            "}\n"
            "\n"
            "QLineEdit{\n"
            "background-color:#FFFFFF;\n"
            "}\n"
            "\n"
            "QLabel{\n"
            "color: white;\n"
            "}")
        self.verticalLayoutWidget = QtWidgets.QWidget(interestUI)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 361, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.principal = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.principal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.principal.setObjectName("principal")
        self.horizontalLayout_2.addWidget(self.principal)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.rate = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rate.setObjectName("rate")
        self.horizontalLayout_4.addWidget(self.rate)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.years = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.years.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.years.setStyleSheet("")
        self.years.setEditable(True)
        self.years.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.years.setIconSize(QtCore.QSize(20, 20))
        self.years.setObjectName("years")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.years.addItem("")
        self.horizontalLayout_3.addWidget(self.years)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setMouseTracking(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(interestUI)
        QtCore.QMetaObject.connectSlotsByName(interestUI)

    def retranslateUi(self, interestUI):
        _translate = QtCore.QCoreApplication.translate
        interestUI.setWindowTitle(_translate("interestUI", "Interest Caculator"))
        self.label_2.setText(_translate("interestUI", "Principal"))
        self.principal.setPrefix(_translate("interestUI", "$"))
        self.label.setText(_translate("interestUI", "Rate"))
        self.rate.setSuffix(_translate("interestUI", "%"))
        self.label_3.setText(_translate("interestUI", "Years"))
        self.years.setItemText(0, _translate("interestUI", "1 year"))
        self.years.setItemText(1, _translate("interestUI", "2 year"))
        self.years.setItemText(2, _translate("interestUI", "3 year"))
        self.years.setItemText(3, _translate("interestUI", " 4 years"))
        self.label_4.setText(_translate("interestUI", "Amount                $"))

    def calculate(self):
        principal = self.principalbox.value()
        rate = self.ratebox.value()
        years = self.yearBox()
        amount = principal * ((1 + (rate / 100.0)) ** rate)
        self.labelResult.setText("${0:2f}".format(amount))


    def retranslateUI(self, Form):
        pass
