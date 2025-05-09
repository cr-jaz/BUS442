# Form implementation generated from reading ui file 'evenodd.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_evenOdd(object):
    def setupUi(self, evenOdd):
        evenOdd.setObjectName("evenOdd")
        evenOdd.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(24)
        evenOdd.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=evenOdd)
        self.centralwidget.setObjectName("centralwidget")
        self.lblEvenOdd = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblEvenOdd.setGeometry(QtCore.QRect(190, 110, 221, 51))
        self.lblEvenOdd.setObjectName("lblEvenOdd")
        self.txtInput = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtInput.setGeometry(QtCore.QRect(200, 160, 371, 41))
        self.txtInput.setObjectName("txtInput")
        self.btnEvalulate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnEvalulate.setGeometry(QtCore.QRect(260, 220, 201, 41))
        self.btnEvalulate.setObjectName("btnEvalulate")
        self.lblResult = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblResult.setGeometry(QtCore.QRect(180, 280, 221, 51))
        self.lblResult.setObjectName("lblResult")
        self.txtResult = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtResult.setGeometry(QtCore.QRect(190, 330, 371, 41))
        self.txtResult.setReadOnly(True)
        self.txtResult.setObjectName("txtResult")
        evenOdd.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=evenOdd)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        evenOdd.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=evenOdd)
        self.statusbar.setObjectName("statusbar")
        evenOdd.setStatusBar(self.statusbar)

        self.retranslateUi(evenOdd)
        QtCore.QMetaObject.connectSlotsByName(evenOdd)
        
        self.btnEvalulate.clicked.connect(self.even_odd)

    def retranslateUi(self, evenOdd):
        _translate = QtCore.QCoreApplication.translate
        evenOdd.setWindowTitle(_translate("evenOdd", "Even Odd"))
        self.lblEvenOdd.setText(_translate("evenOdd", "Enter a number"))
        self.btnEvalulate.setText(_translate("evenOdd", "Even or Odd"))
        self.lblResult.setText(_translate("evenOdd", "Result"))
    
    # Code the functionality
    def even_odd (self):
        input_value = self.txtInput.text()
        # Transformed the value into integer, since the input is a string
        input_value = int(input_value)
        if (input_value%2 == 0):
            self.txtResult.setText("The value is even")
        else:
            self.txtResult.setText("The value is odd")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    evenOdd = QtWidgets.QMainWindow()
    ui = Ui_evenOdd()
    ui.setupUi(evenOdd)
    evenOdd.show()
    sys.exit(app.exec())
