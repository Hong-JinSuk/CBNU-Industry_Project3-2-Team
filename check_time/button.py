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
