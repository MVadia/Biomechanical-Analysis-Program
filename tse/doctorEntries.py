
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import AlphaDesignCode, HelpPage, dropCSV
from generateGraphs import setInputFile
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        app = QtWidgets.QApplication(sys.argv)
        Dialog.setObjectName("Dialog")
        Dialog.resize(1358, 891)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(0, 100, 1461, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(620, 20, 211, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(630, 120, 201, 41))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(280, 190, 20, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(290, 490, 271, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(340, 200, 151, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(290, 240, 51, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(290, 280, 91, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(290, 320, 51, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(290, 360, 71, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(290, 440, 121, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(350, 240, 201, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(390, 280, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(350, 320, 61, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 360, 181, 71))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(420, 440, 131, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(550, 190, 20, 311))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(290, 180, 271, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.textBrowser_9 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(970, 190, 121, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(890, 180, 20, 311))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(900, 170, 271, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(1160, 180, 20, 311))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(900, 480, 271, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(978, 270, 105, 31))
        self.pushButton.setObjectName("pushButton") ##add csv
        self.pushButton.clicked.connect(self.add_csv)

        self.post_csv = QtWidgets.QPushButton(Dialog)
        self.post_csv.setGeometry(QtCore.QRect(978, 305, 105, 31))
        self.post_csv.setObjectName("addPostCSV") ##add csv
        self.post_csv.clicked.connect(self.add_csv)

        

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1250, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2") ##help page
        self.pushButton_2.clicked.connect(self.launch_help_page)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 530, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3") ##confirm button
        self.pushButton_3.clicked.connect(lambda: self.add_details(app, Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def add_csv(self):
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Pre-Treatment CSV File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            filename = os.path.basename(file_path)
            setInputFile(file_path)
            QMessageBox.information(None, "File Added", "CSV File added successfully, add patient information: " + filename, QMessageBox.Ok )


    def add_post_csv(self):
        import os
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Post-Treatment CSV File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            filename = os.path.basename(file_path)
            setInputFile(file_path)
            QMessageBox.information(None, "File Added", "CSV File added successfully, add patient information: " + filename, QMessageBox.Ok )



    def add_details(self, app, Dialog):
        patient_name = self.lineEdit.text()
        patient_id = self.lineEdit_2.text()
        patient_age = self.lineEdit_3.text()
        patient_address = self.lineEdit_4.text()
        patient_contact = self.lineEdit_5.text()

        connect = sqlite3.connect("loginData.db")
        cursor = connect.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS patientDetails_fromDoctor (id INTEGER PRIMARY KEY, patient_id INTEGER, name TEXT, address TEXT,
        age TEXT, contact INTEGER)''')

        ##insert data into table
        cursor.execute("INSERT INTO patientDetails_fromDoctor (patient_id, name, address, age, contact) VALUES (?, ?, ?, ?, ?)", (patient_id, patient_name, patient_address,
                                                                                                                   patient_age,
                                                                                                                   patient_contact))
        connect.commit()

        ##contrinue to main page
        AlphaDesignCode.Dialog = QtWidgets.QDialog()
        AlphaDesignCode.ui = AlphaDesignCode.Ui_Dialog()
        AlphaDesignCode.ui.setupUi(AlphaDesignCode.Dialog, patient_id, patient_name, patient_address, patient_contact, patient_age, patient_id)
        AlphaDesignCode.Dialog.show()
        app.exec_()
        Dialog.close()

    def launch_help_page(self):
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">GAIT Analysis</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Version 0.5</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Welcome Dr James</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Patient Entry Details</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Name:</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">ID Number:</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Age:</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Address:</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Contact Number:</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:600;\">Add a CSV File</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Add Pre Data CSV"))
        self.pushButton_2.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Help Page</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "?"))
        self.pushButton_3.setText(_translate("Dialog", "Confirm "))
        self.post_csv.setText("Add Post Data CSV")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
