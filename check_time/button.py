from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(620, 200)

        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Information_button
        self.Information_button = QtWidgets.QPushButton(self.centralwidget)
        self.Information_button.setGeometry(QtCore.QRect(140, 90, 100, 30))
        self.Information_button.setObjectName("Information_button")
        self.Information_button.setText("Information")
        self.Information_button.clicked.connect(self.Information_event)
        
        # Warning_button
        self.warning_button = QtWidgets.QPushButton(self.centralwidget)
        self.warning_button.setGeometry(QtCore.QRect(260, 90, 100, 30))
        self.warning_button.setObjectName("warning_button")
        self.warning_button.setText("Warning")
        self.warning_button.clicked.connect(self.Warning_event)

        # Question_button
        self.question_button = QtWidgets.QPushButton(self.centralwidget)
        self.question_button.setGeometry(QtCore.QRect(380, 90, 100, 30))
        self.question_button.setObjectName("question_button")
        self.question_button.setText("Question")
        self.question_button.clicked.connect(self.Question_event)

    def Information_event(self):
        buttonReply = QMessageBox.information(
            self, 'Information Title', "Information Message", 
            QMessageBox.Yes | QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Reset | QMessageBox.No, 
            QMessageBox.No
            )
