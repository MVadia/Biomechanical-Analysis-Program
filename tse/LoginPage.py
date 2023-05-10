
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import AlphaDesignCode, doctorEntries, patientRegister, HelpPage
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        app = QtWidgets.QApplication(sys.argv)
        Dialog.setObjectName("Dialog")
        Dialog.resize(1359, 998)
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 90, 1361, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(710, 100, 16, 871))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 190, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 240, 201, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(860, 190, 201, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(860, 240, 201, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.DoctorLoginButton = QtWidgets.QPushButton(Dialog)
        self.DoctorLoginButton.setGeometry(QtCore.QRect(210, 300, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)



        self.DoctorLoginButton.setFont(font)
        self.DoctorLoginButton.setObjectName("DoctorLoginButton")
        self.PatientLoginButton = QtWidgets.QPushButton(Dialog)
        self.PatientLoginButton.setGeometry(QtCore.QRect(870, 300, 61, 31))
        ##doctor login pressed
        self.DoctorLoginButton.clicked.connect(lambda: self.doctor_login_pressed(app, Dialog))

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PatientLoginButton.setFont(font)
        self.PatientLoginButton.setObjectName("PatientLoginButton")

        ##patient login pressed
        self.PatientLoginButton.clicked.connect(lambda: self.patient_login_pressed(app, Dialog))

        self.DoctorLoginButton_2 = QtWidgets.QPushButton(Dialog)
        self.DoctorLoginButton_2.setGeometry(QtCore.QRect(960, 300, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)



        self.DoctorLoginButton_2.setFont(font)
        self.DoctorLoginButton_2.setObjectName("DoctorLoginButton_2")

        ##patient login pressed
        self.DoctorLoginButton_2.clicked.connect(lambda: self.patient_register_pressed(app, Dialog))

        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(1000, 110, 131, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(600, 20, 231, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(280, 110, 141, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(20, 190, 101, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(20, 240, 101, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(750, 190, 101, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(750, 240, 101, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1260, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.launch_help_page(Dialog, app))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def doctor_login_pressed(self, app, Dialog):
        # Retrieve the input values
        doctor_id_input = self.lineEdit.text()
        doctor_pass_input = self.lineEdit_2.text()

        #query db
        connect = sqlite3.connect("loginData.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM doctors WHERE id=? AND password=?", (doctor_id_input, doctor_pass_input))
        row = cursor.fetchone()

        ##check for match
        if row is not None:
            #login successfull
            print("successfull")
            doctorEntries.Dialog = QtWidgets.QDialog()
            doctorEntries.ui = doctorEntries.Ui_Dialog()
            doctorEntries.ui.setupUi(doctorEntries.Dialog)
            doctorEntries.Dialog.show()
            app.exec_()
            Dialog.close()
        else:
            #login failed
            QtWidgets.QMessageBox.warning(Dialog, "Login Failed", "Invalid Login")




    def patient_login_pressed(self, app, Dialog):
        #retrieve input
        patient_id_input = self.lineEdit_3.text()
        patient_pass_input = self.lineEdit_4.text()

        ##query db
        connect = sqlite3.connect("loginData.db")
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM patient_login WHERE id=? AND password=?", (patient_id_input, patient_pass_input))
        row = cursor.fetchone()

        ##check for match
        if row is not None:
            
            #login successfull
            print("successfull")

            self.connect = sqlite3.connect("loginData.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT name, id, age, address, contact FROM patientDetails WHERE id = ? ", (patient_id_input,))
            result = self.cursor.fetchone()
            self.connect.close()

            self.name = result[0]
            self.id_number = result[1]
            self.age = result[2]
            self.address = result[3]
            self.contact_number = result[4]


            AlphaDesignCode.Dialog = QtWidgets.QDialog()
            AlphaDesignCode.ui = AlphaDesignCode.Ui_Dialog()
            AlphaDesignCode.ui.patient_id = patient_id_input
            AlphaDesignCode.ui.setupUi(AlphaDesignCode.Dialog, patient_id_input, self.name, self.address, self.contact_number, self.age, self.id_number)
            AlphaDesignCode.Dialog.show()
            app.exec_()
            Dialog.close()
            
        else:
            #login failed
            QtWidgets.QMessageBox.warning(Dialog, "Login Failed", "Invalid Login")
        

    def patient_register_pressed(self, app, Dialog):
        patientRegister.Dialog = QtWidgets.QDialog()
        patientRegister.ui = patientRegister.Ui_Dialog()
        patientRegister.ui.setupUi(patientRegister.Dialog)
        patientRegister.Dialog.show()
        app.exec_()
        Dialog.close()

    def launch_help_page(self, app, Dialog):
        HelpPage.Dialog = QtWidgets.QDialog()
        HelpPage.ui = HelpPage.Ui_Dialog()
        HelpPage.ui.setupUi(HelpPage.Dialog)
        HelpPage.Dialog.show()
        app.exec_()
        Dialog.close() 
        


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lineEdit.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter ID</p></body></html>"))
        self.lineEdit_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Password</p></body></html>"))
        self.lineEdit_3.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter ID (6 digits)</p></body></html>"))
        self.lineEdit_4.setToolTip(_translate("Dialog", "<html><head/><body><p>Enter Password</p></body></html>"))
        self.DoctorLoginButton.setText(_translate("Dialog", "Login"))
        self.PatientLoginButton.setText(_translate("Dialog", "Login"))
        self.DoctorLoginButton_2.setText(_translate("Dialog", "Register"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Patient Login</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">GAIT Analysis</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Version 0.5</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Doctor Login</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Doctor ID:</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Patient ID:</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Help Page</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
