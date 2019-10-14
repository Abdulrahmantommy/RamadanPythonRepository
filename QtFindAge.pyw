
from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from dateutil.relativedelta import relativedelta
import datetime

class FindAge(QMainWindow):
    def __init__(self):
        super(FindAge, self).__init__()
        self.create_window()

    def create_window(self):
        self.setWindowTitle("Age Finder")
        self.setGeometry(100, 100, 500, 300)
        self.setWindowIcon(QtGui.QIcon("C:\\Users\\Ramadan Metwally\\Desktop\\MonicaIcon.jpg"))
        self.setStyleSheet("background-color: #ccffcc")
        btnExit=QPushButton("Exit", self)
        btnExit.resize(80, 80)
        btnExit.move(418, 218)
        btnExit.clicked.connect(self.leave_pro)
        btnExit.setStyleSheet("background-color: #ffffcc; color: #ff0000")
        btnExit.setFont(QtGui.QFont("arial", 14, 100))

        lblTitle=QLabel(self)
        lblTitle.setText("CALCULATE AGE FROM DATE OF BIRTH")
        lblTitle.setFont(QtGui.QFont("Calibri", 18, 100))
        lblTitle.resize(496, 40)
        lblTitle.move(2, 2)
        lblTitle.setStyleSheet("background: #800000; color: #ffffff; padding-left: 50px")

        lblname = QLabel("Enter name", self)
        lblname.resize(150, 30)
        lblname.move(2, 50)

        self.entname=QLineEdit(self)
        self.entname.resize(300, 30)
        self.entname.move(2, 82)
        self.entname.setPlaceholderText("Enter your name here")

        lblyear = QLabel("Enter year", self)
        lblyear.resize(150, 30)
        lblyear.move(2, 120)

        self.entyear=QLineEdit(self)
        self.entyear.resize(150, 30)
        self.entyear.setPlaceholderText("Enter year of birth")
        self.entyear.move(2, 152)

        lblmonth=QLabel("Enter month", self)
        lblmonth.resize(150, 30)
        lblmonth.move(176, 120)

        self.entmonth=QLineEdit(self)
        self.entmonth.resize(150, 30)
        self.entmonth.setPlaceholderText("Enter month of birth")
        self.entmonth.move(176, 152)

        lblday = QLabel("Enter day", self)
        lblday.resize(150, 30)
        lblday.move(348, 120)

        self.entday=QLineEdit(self)
        self.entday.resize(150, 30)
        self.entday.setPlaceholderText("Enter day of birth")
        self.entday.move(348, 152)

        self.lblResult=QLabel("Calculation result will appear here", self)
        self.lblResult.resize(496, 30)
        self.lblResult.move(2, 185)
        self.lblResult.setStyleSheet("color: black; padding-left: 5px")
        self.lblResult.setFont(QtGui.QFont("Calibri", 12, 100))

        btnCalculate = QPushButton("Calculate", self)
        btnCalculate.resize(150, 80)
        btnCalculate.move(2, 218)
        btnCalculate.setFont(QtGui.QFont("Calibri", 14, 100))
        btnCalculate.clicked.connect(self.calculate_age)

        btnClear = QPushButton("Clear", self)
        btnClear.resize(150, 80)
        btnClear.move(176, 218)
        btnClear.setFont(QtGui.QFont("Calibri", 14, 100))
        btnClear.clicked.connect(self.clear_entries)

        labels = [lblname, lblyear, lblmonth, lblday]
        for lbl in labels:
            lbl.setStyleSheet("background-color:#006600; color: white; padding-left: 5px")
            lbl.setFont(QtGui.QFont("Calibri", 14, 100))

        entries = [self.entname, self.entyear, self.entmonth, self.entday]
        for ent in entries:
            ent.setStyleSheet("background-color:#ffffff; color:#006600; padding-left: 5px")
            ent.setFont(QtGui.QFont("Calibri", 12, 100))
                         
        self.show()

    def leave_pro(self):
        choice = QMessageBox.question(self, "Quit!",
                                      "Do you want to end this session?", QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
        if choice == QMessageBox.Yes:
            print("See you later.")
            sys.exit()
        else:
            print("Welcome back honey!")

    def calculate_age(self):
        username = self.entname.text()
        syear = self.entyear.text()
        smonth = self.entmonth.text()
        sday = self.entday.text()
        try:
            TODAY = datetime.date.today()
            birthday = datetime.date(int(syear), int(smonth), int(sday))
            if birthday > TODAY:
                QMessageBox.warning(self, "Error!", "Birth date must be a date before or equal to today!")
                return                
            age = relativedelta(TODAY, birthday)
        except Exception as e:
            print(e)
            QMessageBox.warning(self, "Error!", "Please enter valid values for birth date!")
            return
        else:
            self.lblResult.setText("{}'s age is {} years, {} months and {} days.".format(username, age.years, age.months, age.days))
            QMessageBox.information(self, "Result", "{}'s age is {} years, {} months and {} days.".format(username, age.years, age.months, age.days))

    def clear_entries(self):
        self.entname.setText("")
        self.entyear.setText("")
        self.entmonth.setText("")
        self.entday.setText("")
        self.lblResult.setText("Calculation result will appear here")


def main():
    app = QApplication(sys.argv)
    win = FindAge()
    sys.exit(app.exec_())

main()
                           
                        
