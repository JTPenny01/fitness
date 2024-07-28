from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHeaderView, QCheckBox, QDateEdit, QLineEdit
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import matplotlib.pyplot as plt\
# need to get matplot compatible with pyqt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from sys import exit



#main stuff
class Fitness(QWidget):
    def __init__(self):
        super().__init__()
    
    def initUI(self):
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())

        self.kal_box = QLineEdit()
        self.kal_box.setPlaceholderText("number of burned calories")

        self.distance_box = QLineEdit()
        self.distance_box.setPlaceholderText("enter distance  ran")
        self.description = QLineEdit()
        self.description.setPlaceholderText("Enter a description")

        self.submit_btn = QPushButton("submit")
        self.add_btn = QPushButton("add")
        self.delete_btn = QPushButton("delete")
        self.clear_btn = QPushButton("clear")
        self.dark_mode = QCheckBox("dark mode")

        self.table = QTableWidget()

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        #layout design
        self_master_layout = QHBoxLayout()
        self.col1 = QVBoxLayout()
        self.col2 = QVBoxLayout()

        self.sub_row1 = QHBoxLayout()
        self.sub_row2 = QHBoxLayout()
        self.sub_row3 = QHBoxLayout()
        self.sub_row4 = QHBoxLayout()

        self.sub_row1.addWidget(QLabel("Date:"))
        self.sub_row1.addWidget(self.date_box)

        self.sub_row2.addWidget(QLabel("calories"))
        self.sub_row2.addWidget(self.kal_box)

        self.sub_row3.addWidget(QLabel("KM:"))
        self.sub_row3.addWidget(self.distance_box)

        self.sub_row4.addWidget(QLabel("Description"))
        self.sub_row4.addWidget(self.description)




        
