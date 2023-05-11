import sys, os
from PyQt5 import QtCore

from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QLabel

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog,QPushButton

class MyWidget(QWidget):
    file_selected = QtCore.pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setAcceptDrops(True)
        self.setGeometry(300, 300, 400, 300)
        self.setStyleSheet("""
            QWidget {
                background-color: #f2f2f2;
                border: 2px solid #c2c2c2;
                border-radius: 5px;
                font-family: Arial, sans-serif;
            }
            QLabel {
                font-size: 15pt;
                font-weight: bold;
                color: #333333;
            }
            QPushButton {
                background-color: #292e2d;
                color: #ffffff;
                border: none;
                padding: 10px;
                font-size: 14pt;
                font-weight: bold;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #3e8e41;
            }
            QPushButton:pressed {
                background-color: #27632a;
            }
        """)

        
        self.title_label = QLabel("Drag and Drop a CSV File", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setGeometry(50, 50, 300, 50)
        self.file_label = QLabel("No file selected", self)
        self.file_label.setGeometry(50, 125, 300, 25)
        self.open_button = QPushButton("Open File", self)
        self.open_button.setGeometry(130, 175, 150, 50)
        self.open_button.clicked.connect(self.open_file)
        self.confrim_button = QPushButton("Confirm", self)
        self.confrim_button.setToolTip("Confirm file choice and close window")
        self.confrim_button.move(160, 230)
        self.confrim_button.clicked.connect(self.confirm)






    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            filepath = url.toLocalFile()
            if filepath.endswith('.csv'):
                print(f"CSV file dropped: {filepath}")
                filename = os.path.basename(filepath)
                self.filepath = filepath
                print(filename)
                self.file_label.setText(f"Selected file: "+ filename)
            else:
                print("File dropped is not a CSV file.")
                self.file_label.setText("Invalid file type")
        else:
            event.ignore()

    def open_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            print(f"CSV file selected: {file_path}")
            filename = os.path.basename(file_path)
            self.filepath = file_path
            self.file_label.setText(f"Selected file: {filename}")
            self.file_selected.emit(file_path)

    def confirm (self):
        if hasattr(self, "filepath"):
            self.file_selected.emit(self.filepath)
        self.close()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.setWindowTitle("Drag and Drop CSV")
    widget.show()
    sys.exit(app.exec_())
