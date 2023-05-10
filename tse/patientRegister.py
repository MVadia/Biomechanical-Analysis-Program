
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import AlphaDesignCode, HelpPage


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        app = QtWidgets.QApplication(sys.argv)
        
        Dialog.setObjectName("Dialog")
        Dialog.resize(1394, 896)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(580, 20, 231, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 100, 1381, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(580, 160, 191, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(500, 230, 141, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(500, 390, 61, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(500, 430, 41, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(500, 470, 111, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(500, 590, 121, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(500, 310, 91, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(500, 350, 91, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.HomeAddress_UserInput = QtWidgets.QLineEdit(Dialog)
        self.HomeAddress_UserInput.setGeometry(QtCore.QRect(630, 470, 221, 101))
        self.HomeAddress_UserInput.setObjectName("HomeAddress_UserInput")
        self.ContactNumber_UserInput = QtWidgets.QLineEdit(Dialog)
        self.ContactNumber_UserInput.setGeometry(QtCore.QRect(630, 590, 211, 31))
        self.ContactNumber_UserInput.setObjectName("ContactNumber_UserInput")
        self.Age_UserInput = QtWidgets.QLineEdit(Dialog)
        self.Age_UserInput.setGeometry(QtCore.QRect(560, 430, 211, 31))
        self.Age_UserInput.setObjectName("Age_UserInput")
        self.Gender_UserInput = QtWidgets.QLineEdit(Dialog)
        self.Gender_UserInput.setGeometry(QtCore.QRect(570, 390, 211, 31))
        self.Gender_UserInput.setObjectName("Gender_UserInput")
        self.LastName_UserInput = QtWidgets.QLineEdit(Dialog)
        self.LastName_UserInput.setGeometry(QtCore.QRect(600, 350, 211, 31))
        self.LastName_UserInput.setObjectName("LastName_UserInput")
        self.FirstName_Userinput = QtWidgets.QLineEdit(Dialog)
        self.FirstName_Userinput.setGeometry(QtCore.QRect(600, 310, 211, 31))
        self.FirstName_Userinput.setObjectName("FirstName_Userinput")
        self.PatientID_userinput = QtWidgets.QLineEdit(Dialog)
        self.PatientID_userinput.setGeometry(QtCore.QRect(650, 230, 211, 31))
        self.PatientID_userinput.setObjectName("PatientID_userinput")
        self.CreateAccountPushButton = QtWidgets.QPushButton(Dialog)
        self.CreateAccountPushButton.setGeometry(QtCore.QRect(610, 650, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CreateAccountPushButton.setFont(font)
        self.CreateAccountPushButton.setObjectName("CreateAccountPushButton")
        self.CreateAccountPushButton.clicked.connect(lambda: self.patient_data_entry_clicked (app, Dialog))
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1280, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.launch_help_page)
        self.textBrowser_10 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_10.setGeometry(QtCore.QRect(500, 270, 81, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.PatientID_userinput_2 = QtWidgets.QLineEdit(Dialog)
        self.PatientID_userinput_2.setGeometry(QtCore.QRect(590, 270, 211, 31))
        self.PatientID_userinput_2.setObjectName("PatientID_userinput_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def patient_data_entry_clicked(self, app, Dialog):
        patient_name = self.FirstName_Userinput.text() +" - "+ self.LastName_UserInput.text()
        patient_address = self.HomeAddress_UserInput.text()
        patient_age = self.Age_UserInput.text()
        patient_gender = self.Gender_UserInput.text()
        patient_contact = self.ContactNumber_UserInput.text()
        patient_password = self.PatientID_userinput_2.text()
        patientID = self.PatientID_userinput.text()
        
        connect = sqlite3.connect("loginData.db")
        cursor = connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patientDetails (id INTEGER PRIMARY KEY, name TEXT, address TEXT,
        age TEXT, gender TEXT, contact INTEGER)''')

        ##insert data into table
        cursor.execute("INSERT INTO patientDetails (name, address, age, gender, contact) VALUES (?, ?, ?, ?, ?)", (patient_name, patient_address,
                                                                                                                   patient_age, patient_gender,
                                                                                                                   patient_contact))
        connect.commit()
        
        ##add name and pass into login table
        cursor.execute("INSERT INTO patient_login (name, password) VALUES (?, ?)", (patient_name, patient_password))
        connect.commit()
        cursor.execute("SELECT id FROM patient_login WHERE name = ? AND password = ?", (patient_name, patient_password))
        result = cursor.fetchone()
        patient_id = result[0] if result else None
        connect.close()

        #give user their loginID
        QtWidgets.QMessageBox.warning(Dialog, "Account Created", "Your account has been created. Your login ID is: "+ str(patient_id))



        ##continue to main page
        AlphaDesignCode.Dialog = QtWidgets.QDialog()
        AlphaDesignCode.ui = AlphaDesignCode.Ui_Dialog()
        AlphaDesignCode.ui.setupUi(AlphaDesignCode.Dialog, patient_id, patient_name, patient_address, patient_contact, patient_age, patientID )
        AlphaDesignCode.Dialog.show()
        app.exec_()
        Dialog.close()

    def launch_help_page(sel, app, Dialog):
        HelpPage.Dialog = QtWidgets.QDialog()
        HelpPage.ui = HelpPage.Ui_Dialog()
        HelpPage.ui.setupUi(HelpPage.Dialog)
        HelpPage.Dialog.show()
        app.exec_()
        Dialog.close()        



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">GAIT ANALYSIS</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Version 0.5</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Create a New Account</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Patient ID Number: </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Gender:</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Age:</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Home Address:</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Contact Number:</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">First Name:</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Last Name:</span></p></body></html>"))
        self.HomeAddress_UserInput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your Home Address</p></body></html>"))
        self.ContactNumber_UserInput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your Contact Number</p></body></html>"))
        self.Age_UserInput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your Age</p></body></html>"))
        self.Gender_UserInput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Gender</p></body></html>"))
        self.LastName_UserInput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your Last Name</p></body></html>"))
        self.FirstName_Userinput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your First Name</p></body></html>"))
        self.PatientID_userinput.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your 6 Digit Patient ID Number</p></body></html>"))
        self.CreateAccountPushButton.setText(_translate("Dialog", "Create Account"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Help Page</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "?"))
        self.textBrowser_10.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.PatientID_userinput_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Your 6 Digit Patient ID Number</p></body></html>"))

'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''