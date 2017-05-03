import sys
from PyQt5.QtWidgets import QApplication, QDialog
from interest import Ui_interestUI

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_interestUI()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
