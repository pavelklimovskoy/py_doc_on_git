from PySide import QtCore, QtGui
from gui import Ui_Form
import sys

#create aplication
app = QtGui.QApplication(sys.argv)

#create form and init UI
Form = QtGui.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.show()

#logic
n = 0

def press():
    global n
    n = n + 1
    ui.lcdNumber.display(n)

ui.pushButton.clicked.connect( press )

#Loop
sys.exit(app.exec_())
