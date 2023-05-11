
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
import sys
import generateGraphs, HelpPage, LoginPage


class Ui_Dialog(object):
    
    def setupUi(self, Dialog, patient_id, name, address, contact_number, age, id_number):
        pre_data, post_data, self.pre_Lknee_flexion, self.post_Lknee_flexion, self.pre_Rknee_flexion, self.post_Rknee_flexion, self.pre_LElbow_flexion, self.post_LElbow_flexion, self.pre_RElbow_flexion, self.post_RElbow_flexion, self.pre_Pelvis_flexion, self.post_Pelvis_flexion, self.LKneediff, self.RKneediff, self.LElbowdiff, self.RElbowdiff, self.Pelvisdiff = generateGraphs.compareData()
        self.patient_id = patient_id
        self.id_number = id_number
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.age = age
        app = QtWidgets.QApplication(sys.argv)
        Dialog.setObjectName("Dialog")
        Dialog.resize(1363, 899)

        ##Graph widget creation
        self.layout = QVBoxLayout(Dialog)
        Dialog.setLayout(self.layout)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(500, 400, 800, 800))
        self.widget.setObjectName("widget")      
        self.label = QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(374, -73, 800, 800))
        self.label.setObjectName("label")
        self.layout.addWidget(self.widget)


        Dialog.setAutoFillBackground(False)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(290, 90, 20, 768))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(0, 800, 1351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        ##knee flex button
        self.pushButton.clicked.connect(self.on_button_click_Kneeflex)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 260, 221, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        ##Button Press Handle: Elbow Flex
        self.pushButton_2.clicked.connect(self.on_button_clickElbowFlex)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 370, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.on_button_clickPelvisFlex)


        ##post knee data
        self.postKnee_button = QtWidgets.QPushButton(Dialog)
        self.postKnee_button.setGeometry(QtCore.QRect(20, 470, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.postKnee_button.setFont(font)
        self.postKnee_button.setObjectName("postKnee_button")
        self.postKnee_button.clicked.connect(self.on_button_click_PostKneeflex)


        ##post elbow data
        self.postElbow_button = QtWidgets.QPushButton(Dialog)
        self.postElbow_button.setGeometry(QtCore.QRect(20, 570, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.postElbow_button.setFont(font)
        self.postElbow_button.setObjectName("postElbow_button")
        self.postElbow_button.clicked.connect(self.on_button_clickPostElbowFlex)


        ##post pelvis data
        self.postPelvis_button = QtWidgets.QPushButton(Dialog)
        self.postPelvis_button.setGeometry(QtCore.QRect(20, 670, 261, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.postPelvis_button.setFont(font)
        self.postPelvis_button.setObjectName("postPelvis_button")
        self.postPelvis_button.clicked.connect(self.on_button_click_PostPelvisflex)       




        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(0, 80, 1361, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(1103, 90, 20, 768))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(1110, 370, 251, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(1130, 450, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        

        self.checkBox_2 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_2.setGeometry(QtCore.QRect(1130, 480, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(1130, 510, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(1130, 540, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_5.setGeometry(QtCore.QRect(1130, 570, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(1130, 600, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(1130, 630, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(1130, 660, 141, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setObjectName("checkBox_8")
        self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(1180, 730, 91, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.graph_selection) ##graph select

        self.line_6 = QtWidgets.QFrame(Dialog)
        self.line_6.setGeometry(QtCore.QRect(300, 590, 811, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(Dialog)
        self.line_7.setGeometry(QtCore.QRect(480, 600, 20, 260))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(Dialog)
        self.line_8.setGeometry(QtCore.QRect(690, 600, 20, 260))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(Dialog)
        self.line_9.setGeometry(QtCore.QRect(910, 600, 20, 260))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(Dialog)
        self.line_10.setGeometry(QtCore.QRect(300, 630, 811, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(Dialog)
        self.line_11.setGeometry(QtCore.QRect(300, 670, 811, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(Dialog)
        self.line_12.setGeometry(QtCore.QRect(300, 710, 811, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(Dialog)
        self.line_13.setGeometry(QtCore.QRect(300, 760, 811, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(Dialog)
        self.line_14.setGeometry(QtCore.QRect(300, 850, 811, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(570, 0, 271, 81))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 90, 271, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(1190, 100, 111, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_4.setGeometry(QtCore.QRect(1130, 160, 211, 91))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_5.setGeometry(QtCore.QRect(1120, 390, 231, 31))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_6.setGeometry(QtCore.QRect(350, 600, 101, 31))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_7.setGeometry(QtCore.QRect(520, 600, 141, 31))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_8.setGeometry(QtCore.QRect(740, 600, 151, 31))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_9.setGeometry(QtCore.QRect(970, 600, 101, 31))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_10.setGeometry(QtCore.QRect(360, 640, 81, 31))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_11.setGeometry(QtCore.QRect(360, 680, 81, 31))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_12.setGeometry(QtCore.QRect(360, 730, 81, 31))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_13.setGeometry(QtCore.QRect(360, 770, 81, 31))
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.textBrowser_14 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_14.setGeometry(QtCore.QRect(360, 815, 61, 31))
        self.textBrowser_14.setObjectName("textBrowser_14")


        ##flexion difference text boxes
        self.Rknee_flex_pre = QtWidgets.QTextBrowser(Dialog)
        self.Rknee_flex_pre.setGeometry(QtCore.QRect(520, 680, 150, 31))
        self.Rknee_flex_pre.setObjectName("Rknee_flex_pre")

        self.Rknee_flex_post = QtWidgets.QTextBrowser(Dialog)
        self.Rknee_flex_post.setGeometry(QtCore.QRect(740, 680, 150, 31))
        self.Rknee_flex_post.setObjectName("Rknee_flex_post")

        ##flexion difference text boxes
        self.Lknee_flex_pre = QtWidgets.QTextBrowser(Dialog)
        self.Lknee_flex_pre.setGeometry(QtCore.QRect(520, 640, 150, 31))
        self.Lknee_flex_pre.setObjectName("Lknee_flex_pre")

        self.Lknee_flex_post = QtWidgets.QTextBrowser(Dialog)
        self.Lknee_flex_post.setGeometry(QtCore.QRect(720, 640, 150, 31))
        self.Lknee_flex_post.setObjectName("Lknee_flex_post")        


        ##elbow diff text boxes
        self.Relbow_flex_pre = QtWidgets.QTextBrowser(Dialog)
        self.Relbow_flex_pre.setGeometry(QtCore.QRect(520, 770, 150, 31))
        self.Relbow_flex_pre.setObjectName("Relbow_flex_pre")

        self.Relbow_flex_post = QtWidgets.QTextBrowser(Dialog)
        self.Relbow_flex_post.setGeometry(QtCore.QRect(740, 770, 150, 31))
        self.Relbow_flex_post.setObjectName("Relbow_flex_post")        

        self.Lelbow_flex_pre = QtWidgets.QTextBrowser(Dialog)
        self.Lelbow_flex_pre.setGeometry(QtCore.QRect(520, 730, 150, 31))
        self.Lelbow_flex_pre.setObjectName("Lelbow_flex_pre")

        self.Lelbow_flex_post = QtWidgets.QTextBrowser(Dialog)
        self.Lelbow_flex_post.setGeometry(QtCore.QRect(740, 730, 150, 31))
        self.Lelbow_flex_post.setObjectName("Lelbow_flex_post")

        ##pelvis diff text boxes
        self.pelvis_flex_pre = QtWidgets.QTextBrowser(Dialog)
        self.pelvis_flex_pre.setGeometry(QtCore.QRect(520, 815, 150, 31))
        self.pelvis_flex_pre.setObjectName("pelvis_flex_pre")

        self.pelvis_flex_post = QtWidgets.QTextBrowser(Dialog)
        self.pelvis_flex_post.setGeometry(QtCore.QRect(740, 815, 150, 31))
        self.pelvis_flex_post.setObjectName("pelvis_flex_post")        


        self.RKneeDiff = QtWidgets.QTextBrowser(Dialog)
        self.RKneeDiff.setGeometry(970, 680, 140, 31)
        self.RKneeDiff.setObjectName("RKnee_Diff")

        self.LKneeDiff = QtWidgets.QTextBrowser(Dialog)
        self.LKneeDiff.setGeometry(970, 640, 140, 31)
        self.LKneeDiff.setObjectName("LKnee_Diff")

        self.LElbowDiff = QtWidgets.QTextBrowser(Dialog)
        self.LElbowDiff.setGeometry(970, 730, 140, 31)
        self.LElbowDiff.setObjectName("LElbow_Diff")

        self.RElbowDiff = QtWidgets.QTextBrowser(Dialog)
        self.RElbowDiff.setGeometry(970, 770, 140, 31)
        self.RElbowDiff.setObjectName("RElbow_Diff")

        self.PelvisDiff = QtWidgets.QTextBrowser(Dialog)
        self.PelvisDiff.setGeometry(970, 815, 140, 31)
        self.PelvisDiff.setObjectName("PelvisDiff")

        




        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(1260, 20, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4") ##help butotn
        self.pushButton_4.clicked.connect(lambda: self.launch_help_page(app, Dialog))
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(60, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5") ##log out
        self.pushButton_5.clicked.connect(lambda: self.logout(app, Dialog))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        ##Button press handler: Knee Flex
    def on_button_click_Kneeflex(self):
        kneePNG = ('Pre_Knee_Flexion.png')
        if os.path.isfile(kneePNG):
            pixmap = QPixmap (kneePNG)
        else:
            kneePNG = generateGraphs.preKneeData()
            pixmap = QPixmap(kneePNG)
        self.label.setPixmap(pixmap)
        pass

        ##Button Handler: Elbow Flex
    def on_button_clickElbowFlex(self):
        elbowPNG = ('Pre_Elbow_Flexion.png')
        if os.path.isfile(elbowPNG):
            pixmap = QPixmap (elbowPNG)
        else:
            elbowPNG = generateGraphs.preelbowData()
            pixmap = QPixmap(elbowPNG)
        self.label.setPixmap(pixmap)
        

    def on_button_clickPelvisFlex(self):
        pelvisPNG = ('Pre_Pelvis_Flexion.png')
        if os.path.isfile(pelvisPNG):
            pixmap = QPixmap(pelvisPNG)
        else:
            pelvisPNG = generateGraphs.prepelvisData()
            pixmap = QPixmap(pelvisPNG)
        self.label.setPixmap(pixmap)

    def launch_help_page(self, app, Dialog):
        HelpPage.Dialog = QtWidgets.QDialog()
        HelpPage.ui = HelpPage.Ui_Dialog()
        HelpPage.ui.setupUi(HelpPage.Dialog)
        HelpPage.Dialog.show()
        app.exec_()
        Dialog.close()


    def logout(self, app, Dialog):
        LoginPage.Dialog = QtWidgets.QDialog()
        LoginPage.ui = LoginPage.Ui_Dialog()
        LoginPage.ui.setupUi(LoginPage.Dialog)
        LoginPage.Dialog.show()
        app.exec_
        Dialog.close()

    def graph_selection(self):

        self.graph_selected = { "Pre_Knee_Flexion.png": self.checkBox.isChecked(),     
                            "Pre_Elbow_Flexion.png": self.checkBox_2.isChecked(),
                           "Pre_Pelvis_Flexion.png": self.checkBox_3.isChecked(),
                           "Post_Knee_Flexion.png": self.checkBox_4.isChecked(),
                           "Post_Elbow_Flexion.png": self.checkBox_5.isChecked(),
                           "Post_Pelvis_flexion.png": self.checkBox_6.isChecked()}
        import PDFGenerator
        PDFGenerator.get_graph_data(self.name, self.address, self.age, self.contact_number, self.graph_selected, self.RKneediff, self.LKneediff, self.RElbowdiff, self.LElbowdiff, self.Pelvisdiff)
        

        


    def on_button_click_PostKneeflex(self):
        PostkneePNG = ('Post_Knee_Flexion.png')
        if os.path.isfile(PostkneePNG):
            pixmap = QPixmap (PostkneePNG)
        else:
            PostkneePNG = generateGraphs.PostKneeData()
            pixmap = QPixmap(PostkneePNG)
        self.label.setPixmap(pixmap)
        pass

        ##Button Handler: Elbow Flex
    def on_button_clickPostElbowFlex(self):
        PostElbowPNG = ('Post_Elbow_Flexion.png')
        if os.path.isfile(PostElbowPNG):
            pixmap = QPixmap (PostElbowPNG)
        else:
            PostElbowPNG = generateGraphs.PostElbowData()
            pixmap = QPixmap(PostElbowPNG)
        self.label.setPixmap(pixmap)


    def on_button_click_PostPelvisflex(self):
        PostPelvisPNG = ('Post_Pelvis_flexion.png')
        if os.path.isfile(PostPelvisPNG):
            pixmap = QPixmap (PostPelvisPNG)
        else:
            PostPelvisPNG = generateGraphs.PostpelvisData()
            pixmap = QPixmap(PostPelvisPNG)
        self.label.setPixmap(pixmap)
        pass


        
                    

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">1. Knee Flexion Pre-Treatment</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "1. Knee Flexion Pre-Treatment"))
        self.pushButton_2.setText(_translate("Dialog", "2. Elbow Flexion Pre-Treatment"))
        self.pushButton_3.setText(_translate("Dialog", "3. Pelvis Flexion Pre-Treatment"))
        self.checkBox.setText(_translate("Dialog", "Graph 1"))
        self.checkBox_2.setText(_translate("Dialog", "Graph 2"))
        self.checkBox_3.setText(_translate("Dialog", "Graph 3"))
        self.checkBox_4.setText(_translate("Dialog", "Graph 4"))
        self.checkBox_5.setText(_translate("Dialog", "Graph 5"))
        self.checkBox_6.setText(_translate("Dialog", "Graph 6"))
        self.checkBox_7.setText(_translate("Dialog", "Bold Text"))
        self.checkBox_8.setText(_translate("Dialog", "Increased Font Size"))
        self.pushButton_7.setText(_translate("Dialog", "Generate PDF"))

        

        
        ##set text values
        text = "<p><strong>Name:</strong> {0}</p>".format(self.name)
        text += "<p><strong>ID Number:</strong> {0}</p>".format(self.id_number)
        text += "<p><strong>Age:</strong> {0}</p>".format(self.age)
        text += "<p><strong>Address:</strong> {0}</p>".format(self.address)
        text += "<p><strong>Contact Number:</strong> {0}</p>".format(self.contact_number)    
        

        
        pre_Rknee_flexion_str = str(self.pre_Rknee_flexion)
        pre_Lknee_flexion_str = str(self.pre_Lknee_flexion)
        post_Lknee_flexion_str = str(self.post_Lknee_flexion)
        post_Rknee_flexion_str = str(self.post_Rknee_flexion)
        RKneediff_str = str(self.RKneediff)
        LKneediff_str = str(self.LKneediff)

        pre_RElbow_flexion_str = str(self.pre_RElbow_flexion)
        pre_LElbow_flexion_str = str(self.pre_LElbow_flexion)
        post_RElbow_flexion_str = str(self.post_RElbow_flexion)
        post_LElbow_flexion_str = str(self.post_LElbow_flexion)
        RElbowdiff_str = str(self.RElbowdiff)
        LElbowdiff_str = str(self.LElbowdiff)

        pre_Pelvis_flexion_str = str(self.pre_Pelvis_flexion)
        post_Pelvis_flexion_str = str(self.post_Pelvis_flexion)
        Pelvisdiff_str = str(self.Pelvisdiff)

        





        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">GAIT Analysis</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">Version 0.5</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Please Select A Graph To View</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Patient Details</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Dialog", f"""
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
    <html>
    <head>
        <meta name="qrichtext" content="1" />
        <style type="text/css">
            p, li {{ white-space: pre-wrap; }}
        </style>
    </head>
    <body style="font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
        <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style="font-size:10pt; font-weight:600;">Name:</span>
            <span style="font-size:10pt;">{self.name}</span>
        </p>
        <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style="font-size:10pt; font-weight:600;">ID Number:</span>
            <span style="font-size:10pt;">{self.id_number}</span>
        </p>
        <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style="font-size:10pt; font-weight:600;">Age:</span>
            <span style="font-size:10pt;">{self.age}</span>
        </p>
        <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style="font-size:10pt; font-weight:600;">Address:</span>
            <span style="font-size:10pt;">{self.address}</span>
        </p>
        <p style="margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
            <span style="font-size:10pt; font-weight:600;">Contact Number:</span>
            <span style="font-size:10pt;">{self.contact_number}</span>
        </p>
    </body>
    </html>
""")) 


        self.textBrowser_5.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; color:#000000;\">Select options required for PDF</span></p></body></html>"))
        
        self.textBrowser_6.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Biomarker</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Pre-Treatment</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Post-Treatment</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; text-decoration: underline;\">Difference</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Knee (L)</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Knee (R)</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Elbow (L)</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Elbow (R)</span></p></body></html>"))
        self.textBrowser_14.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600; font-style:italic;\">Pelvis</span></p></body></html>"))
        self.pushButton_4.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:400;\">Help Page</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Dialog", "?"))
        self.pushButton_5.setText(_translate("Dialog", "Log Out"))
        self.postKnee_button.setText("Post Knee Flexion")
        self.postElbow_button.setText("Post Elbow Flexion")
        self.postPelvis_button.setText("Post Pelvis Flexion")
        self.textBrowser_4.setHtml(text)

        self.Rknee_flex_pre.setHtml(pre_Rknee_flexion_str)
        self.Rknee_flex_post.setHtml(post_Rknee_flexion_str)
        self.Lknee_flex_pre.setHtml(pre_Lknee_flexion_str)
        self.Lknee_flex_post.setHtml(post_Lknee_flexion_str)
        self.Relbow_flex_pre.setHtml(pre_RElbow_flexion_str)
        self.Relbow_flex_post.setHtml(post_RElbow_flexion_str)
        self.Lelbow_flex_pre.setHtml(pre_LElbow_flexion_str)
        self.Lelbow_flex_post.setHtml(post_LElbow_flexion_str)
        self.pelvis_flex_pre.setHtml(pre_Pelvis_flexion_str)
        self.pelvis_flex_post.setHtml(post_Pelvis_flexion_str)
        self.RKneeDiff.setHtml(RKneediff_str+ " %")
        self.LKneeDiff.setHtml(LKneediff_str+ " %")
        self.RElbowDiff.setHtml(RElbowdiff_str+ " %")
        self.LElbowDiff.setHtml(LElbowdiff_str + " %")
        self.PelvisDiff.setHtml(Pelvisdiff_str + " %")




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