# Form implementation generated from reading ui file 'newcollege.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox

class Ui_collegeFeeCalculator(object):
    def setupUi(self, collegeFeeCalculator):
        collegeFeeCalculator.setObjectName("collegeFeeCalculator")
        collegeFeeCalculator.resize(594, 451)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        collegeFeeCalculator.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=collegeFeeCalculator)
        self.centralwidget.setObjectName("centralwidget")
        self.lblTitle = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTitle.setGeometry(QtCore.QRect(120, 20, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.lblDetail = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblDetail.setGeometry(QtCore.QRect(10, 70, 161, 21))
        self.lblDetail.setObjectName("lblDetail")
        self.lblFirst = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblFirst.setGeometry(QtCore.QRect(10, 90, 91, 21))
        self.lblFirst.setObjectName("lblFirst")
        self.lblLast = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblLast.setGeometry(QtCore.QRect(10, 120, 91, 21))
        self.lblLast.setObjectName("lblLast")
        self.txtFirst = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtFirst.setGeometry(QtCore.QRect(120, 90, 171, 21))
        self.txtFirst.setObjectName("txtFirst")
        self.txtLast = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtLast.setGeometry(QtCore.QRect(120, 120, 171, 21))
        self.txtLast.setObjectName("txtLast")
        self.lblProgram = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblProgram.setGeometry(QtCore.QRect(10, 180, 121, 21))
        self.lblProgram.setObjectName("lblProgram")
        self.lblSelect = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblSelect.setGeometry(QtCore.QRect(10, 200, 171, 21))
        self.lblSelect.setObjectName("lblSelect")
        self.comboMajor = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboMajor.setGeometry(QtCore.QRect(190, 200, 151, 21))
        self.comboMajor.setObjectName("comboMajor")
        self.comboMajor.addItem("")
        self.comboMajor.addItem("")
        self.comboMajor.addItem("")
        self.comboMajor.addItem("")
        self.lblAge = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblAge.setGeometry(QtCore.QRect(360, 90, 61, 21))
        self.lblAge.setObjectName("lblAge")
        self.txtAge = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtAge.setGeometry(QtCore.QRect(450, 90, 121, 21))
        self.txtAge.setObjectName("txtAge")
        self.lblStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(360, 180, 121, 21))
        self.lblStatus.setObjectName("lblStatus")
        self.lblSelect_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblSelect_2.setGeometry(QtCore.QRect(360, 200, 161, 21))
        self.lblSelect_2.setObjectName("lblSelect_2")
        self.checkStatus = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkStatus.setGeometry(QtCore.QRect(520, 200, 91, 16))
        self.checkStatus.setObjectName("checkStatus")
        self.lblTotal = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblTotal.setGeometry(QtCore.QRect(90, 304, 131, 21))
        self.lblTotal.setObjectName("lblTotal")
        self.txtTotal = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txtTotal.setGeometry(QtCore.QRect(210, 304, 201, 21))
        self.txtTotal.setReadOnly(True)
        self.txtTotal.setObjectName("txtTotal")
        self.btnCalculate = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCalculate.setGeometry(QtCore.QRect(250, 270, 81, 21))
        self.btnCalculate.setObjectName("btnCalculate")
        self.btnClear = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(130, 370, 81, 31))
        self.btnClear.setObjectName("btnClear")
        self.lblClear = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblClear.setGeometry(QtCore.QRect(10, 370, 121, 21))
        self.lblClear.setObjectName("lblClear")
        self.lblClear_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.lblClear_2.setGeometry(QtCore.QRect(420, 370, 161, 21))
        self.lblClear_2.setObjectName("lblClear_2")
        self.btnClear_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnClear_2.setGeometry(QtCore.QRect(510, 370, 71, 31))
        self.btnClear_2.setObjectName("btnClear_2")
        collegeFeeCalculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=collegeFeeCalculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 18))
        self.menubar.setObjectName("menubar")
        collegeFeeCalculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=collegeFeeCalculator)
        self.statusbar.setObjectName("statusbar")
        collegeFeeCalculator.setStatusBar(self.statusbar)

        self.retranslateUi(collegeFeeCalculator)
        QtCore.QMetaObject.connectSlotsByName(collegeFeeCalculator)
        
        # When the calculate button is clicked, execute the calculate function
        self.btnCalculate.clicked.connect(self.college)
        
        # When the clear button is clicked, execute the clearall function
        self.btnClear.clicked.connect(self.clearall)
        
        # When the Exit button is clicked, execute the appexit function
        self.btnClear_2.clicked.connect(self.appexit)

    def retranslateUi(self, collegeFeeCalculator):
        _translate = QtCore.QCoreApplication.translate
        collegeFeeCalculator.setWindowTitle(_translate("collegeFeeCalculator", "MainWindow"))
        self.lblTitle.setText(_translate("collegeFeeCalculator", "College Fee Calculator"))
        self.lblDetail.setText(_translate("collegeFeeCalculator", "Student Personal Details:"))
        self.lblFirst.setText(_translate("collegeFeeCalculator", "First Name:"))
        self.lblLast.setText(_translate("collegeFeeCalculator", "Last Name:"))
        self.lblProgram.setText(_translate("collegeFeeCalculator", "Program Selection:"))
        self.lblSelect.setText(_translate("collegeFeeCalculator", "Select Your Intended Program:"))
        self.comboMajor.setItemText(0, _translate("collegeFeeCalculator", "Computer Science"))
        self.comboMajor.setItemText(1, _translate("collegeFeeCalculator", "Business Administration"))
        self.comboMajor.setItemText(2, _translate("collegeFeeCalculator", "Arts and Humanities"))
        self.comboMajor.setItemText(3, _translate("collegeFeeCalculator", "Sciences"))
        self.lblAge.setText(_translate("collegeFeeCalculator", "Age:"))
        self.lblStatus.setText(_translate("collegeFeeCalculator", "Residency Status:"))
        self.lblSelect_2.setText(_translate("collegeFeeCalculator", "Check the Box If It Applies:"))
        self.checkStatus.setText(_translate("collegeFeeCalculator", "In-State"))
        self.lblTotal.setText(_translate("collegeFeeCalculator", "Total Tuition Cost:"))
        self.btnCalculate.setText(_translate("collegeFeeCalculator", "Calculate Fee"))
        self.btnClear.setText(_translate("collegeFeeCalculator", "Clear"))
        self.lblClear.setText(_translate("collegeFeeCalculator", "Clear the Form:"))
        self.lblClear_2.setText(_translate("collegeFeeCalculator", "Exit App:"))
        self.btnClear_2.setText(_translate("collegeFeeCalculator", "Exit"))

    def clearall(self):
        # Clear the first name text box
        self.txtFirst.clear()
        
        # Clear the last name text box
        self.txtLast.clear()
        
        # Clear the age text box
        self.txtAge.clear()
        
        # Clear the check from the checkbox
        self.checkStatus.setChecked(False)
        
        # Clear the total cost text box
        self.txtTotal.clear()
        
        # Reset the combo box back to its default value
        self.comboMajor.setCurrentIndex(0)
    
    def appexit(self):
        # When the exit button is clicked, this will quit the application
        QtWidgets.QApplication.quit()
    
    def college (self):
        # Define some variables
        input_age = self.txtAge.text()
        program_select = self.comboMajor.currentText()
        
        # Create a Message box instance
        msg = QtWidgets.QMessageBox()
        
        # Set the message box window title 
        msg.setWindowTitle("College Fee Calculator")
        
        # Make sure the any numeric inputs are actually integers
        if (input_age.isdigit()):
            input_age = int (input_age)
            # Input validation to ensure that the value is a valid age
            if (input_age >= 0 and input_age <= 120):
                input_age = int (input_age)
                
                # Add correct tuition amount based on status
                if (self.checkStatus.isChecked()):
                    tuition = 10000.00
                else:
                    tuition = 15000.00
                
                # Apply additional charges based on the program
                if (program_select == "Computer Science"):
                    prgm_cost = 2000
                elif (program_select == "Business Administration"):
                    prgm_cost = 1500
                elif (program_select == "Arts and Humanities"):
                    prgm_cost = 1000
                else:
                    prgm_cost = 1800
                
            
                #Calculate the total cost
                total_cost = tuition + prgm_cost
            
                #Display the total cost in the text box
                self.txtTotal.setText(str(f"${total_cost:.2f}"))
            
            else:
            # Make a message when the second if conditions aren't met
                msg.setText("Please enter a valid age")
                msg.exec()
            
        else:
        # Make a message when the initial if conditions aren't met
            msg.setText("Please enter a numeric value in the Age field")
            msg.exec()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    collegeFeeCalculator = QtWidgets.QMainWindow()
    ui = Ui_collegeFeeCalculator()
    ui.setupUi(collegeFeeCalculator)
    collegeFeeCalculator.show()
    sys.exit(app.exec())
