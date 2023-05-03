from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QWidget, QSizePolicy, QTableWidget, QInputDialog, QTableWidgetItem
from PyQt5.QtCore import Qt
import os
import sys


class Ui_MainWindow(QWidget):
    s = ""
    done = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PasswordTable = QTableWidget(self.centralwidget)
        self.PasswordTable.setObjectName(u"tableWidget")
        self.PasswordTable.setGeometry(QtCore.QRect(50, 125, 3050, 1450))
        self.PasswordTable.setColumnCount(5)
        self.PasswordTable.setColumnWidth(0, 300)
        self.PasswordTable.setColumnWidth(1, 350)
        self.PasswordTable.setColumnWidth(2, 600)
        self.PasswordTable.setColumnWidth(3, 600)
        self.PasswordTable.setColumnWidth(4, 1150)
        self.PasswordTable.setAlternatingRowColors(True)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(4, item)
        self.PasswordTable.hide()
        self.ButtonMain = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonMain.setGeometry(QtCore.QRect(1400, 100, 400, 50))
        self.ButtonNO = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonNO.setGeometry(QtCore.QRect(1200, 100, 400, 50))
        self.ButtonYES = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonYES.setGeometry(QtCore.QRect(1800, 100, 400, 50))
        self.ButtonAddPass = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAddPass.setGeometry(610, 50, 300, 50)
        self.ButtonDeletePass = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRefreshTable = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDeletePass.setGeometry(10, 50, 300, 50)
        self.ButtonRefreshTable.setGeometry(310, 50, 300, 50)
        self.ButtonDone = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonDone.setGeometry(QtCore.QRect(1400, 250, 400, 50))
        self.ButtonAddPass.hide()
        self.ButtonNO.hide()
        self.ButtonYES.hide()
        self.ButtonDeletePass.hide()
        self.ButtonRefreshTable.hide()
        self.ButtonDone.hide()
        self.ButtonMain.setFont(QFont('Times', 15))
        self.ButtonNO.setFont(QFont('Times', 15))
        self.ButtonYES.setFont(QFont('Times', 15))
        self.ButtonAddPass.setFont(QFont('Times', 15))
        self.ButtonDeletePass.setFont(QFont('Times', 15))
        self.ButtonRefreshTable.setFont(QFont('Times', 15))
        self.ButtonDone.setFont(QFont('Times', 15))
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 200, 100, 100))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1325, 20, 550, 75))
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setGeometry(QtCore.QRect(1000, 120, 550, 75))
        self.label3.hide()
        font = QtGui.QFont()
        font.setPointSize(26)
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.label1.setFont(font1)
        self.label.setWordWrap(False)
        self.label3.setWordWrap(False)
        self.label1.setObjectName("Label1")
        self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
        self.label3.setFont(font)
        self.label3.setWordWrap(False)
        self.label3.setObjectName("label3")
        self.label3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label3.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 377, 22))
        self.menubar.setObjectName("menubar")
        self.menuPassword_Creator = QtWidgets.QMenu(self.menubar)
        self.menuPassword_Creator.setObjectName("menuPassword_Creator")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.Password = QtWidgets.QAction(MainWindow)
        self.Password.setObjectName("Password")
        self.menubar.hide()
        self.actionCreate_A_Password = QtWidgets.QAction(MainWindow)
        self.actionCreate_A_Password.setObjectName("actionCreate_a_Password")
        self.actionFAQ_s = QtWidgets.QAction(MainWindow)
        self.actionFAQ_s.setObjectName("actionFAQ_s")
        self.actionfurther_help = QtWidgets.QAction(MainWindow)
        self.actionfurther_help.setObjectName("actionfurther_help")
        self.menuPassword_Creator.addAction(self.actionCreate_A_Password)
        self.menuHelp.addAction(self.actionFAQ_s)
        self.menuHelp.addAction(self.actionfurther_help)
        self.menubar.addAction(self.menuPassword_Creator.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionFAQ_s.triggered.connect(self.FAQ)
        self.actionfurther_help.triggered.connect(self.help)
        self.ButtonMain.clicked.connect(self.clicker)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.ButtonMain.setStatusTip(_translate("MainWindow", "Start Using the Password Manager"))
        item = self.PasswordTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.PasswordTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Website"))
        item = self.PasswordTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "UserName"))
        item = self.PasswordTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        item = self.PasswordTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Description"))
        self.ButtonMain.setStatusTip(_translate("MainWiindow", "Get Started"))
        self.ButtonMain.setText(_translate("MainWindow", "Get Started"))
        self.ButtonNO.setStatusTip(_translate("MainWindow", "NO"))
        self.ButtonNO.setText(_translate("MainWindow", "NO"))
        self.ButtonYES.setStatusTip(_translate("MainWindow", "YES"))
        self.ButtonYES.setText(_translate("MainWindow", "YES"))
        self.ButtonAddPass.setStatusTip(_translate("MainWindow", "Add A Password"))
        self.ButtonAddPass.setText(_translate("MainWindow", "Add A Password"))
        self.ButtonDeletePass.setStatusTip(_translate("MainWindow", "Delete A Password"))
        self.ButtonDeletePass.setText(_translate("MainWindow", "Delete A Password"))
        self.ButtonRefreshTable.setStatusTip(_translate("MainWindow", "Refresh the Table"))
        self.ButtonRefreshTable.setText(_translate("MainWindow", "Refresh the Table"))
        self.ButtonDone.setText(_translate("MainWindow", "Done? Click ME!"))
        self.label1.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "Password Manager"))
        self.label3.setText(_translate("MainWindow", " "))
        self.menuPassword_Creator.setTitle(_translate("MainWindow", "Password"))
        self.menuHelp.setStatusTip(_translate("MainWindow", "Help"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.Password.setText(_translate("MainWindow", "Create A Password"))
        self.Password.setStatusTip(_translate("MainWindow", "Create A New Password to Store"))
        self.Password.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCreate_A_Password.setText(_translate("MainWindow", "Add A Password"))
        self.actionCreate_A_Password.setStatusTip(_translate("MainWindow", "Add A Password"))
        self.actionCreate_A_Password.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionFAQ_s.setText(_translate("MainWindow", "FAQ\'s"))
        self.actionFAQ_s.setStatusTip(_translate("MainWindow", "Frequently asked questions"))
        self.actionfurther_help.setText(_translate("MainWindow", "Help"))
        self.actionfurther_help.setStatusTip(_translate("MainWindow", "Find help"))
        self.actionfurther_help.setShortcut(_translate("MainWindow", "Ctrl+H"))

    def clicker(self):
        self.ButtonDone.hide()
        _translate = QtCore.QCoreApplication.translate
        self.ButtonMain.hide()
        self.menubar.show()
        self.label.setText("Do you have a password file stored on this computer?")
        self.label.setGeometry(1000, 20, 550, 75)
        self.label.adjustSize()
        self.ButtonNO.show()
        self.ButtonYES.show()
        self.actionCreate_A_Password.triggered.connect(self.before)
        self.ButtonYES.clicked.connect(self.yes)
        self.ButtonNO.clicked.connect(self.no)

    def yes(self):
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText("Please Select the file storing the passwords")
        self.label1.adjustSize()
        QtTest.QTest.qWait(200)
        fName = QFileDialog.getOpenFileName(self, "Open Text File", "", "Text Files(*.txt)")
        qr = fName[0]
        self.s = qr
        f = ""
        try:
            q = open(qr, "r")
            f = q.readline()
        except FileNotFoundError:
            print(
                "The File you have opened has been moved or deleted. Please rerun the program and select another one.")
        if qr.endswith(".txt") and f == 'made by tigerjade003 \n':
            rr = open(qr, "r")
            q = rr.readlines()
            self.PasswordTable.show()
            self.label1.hide()
            self.label.setText("Passwords")
            self.ButtonNO.hide()
            self.ButtonYES.hide()
            self.ButtonAddPass.show()
            self.ButtonDeletePass.show()
            self.ButtonRefreshTable.show()
            self.ButtonAddPass.clicked.connect(self.createPass)
            self.ButtonDeletePass.clicked.connect(self.deletePass)
            self.ButtonRefreshTable.clicked.connect(self.refresh)
            pr = open(qr, "r")
            pr.readline()
            for i in range(len(q) - 1):
                s = pr.readline().strip("\n").split("|||")
                if s != ['']:
                    self.PasswordTable.insertRow(i)
                    self.PasswordTable.setItem(i, 0, QTableWidgetItem(s[0]))
                    self.PasswordTable.setItem(i, 1, QTableWidgetItem(s[1]))
                    self.PasswordTable.setItem(i, 2, QTableWidgetItem(s[2]))
                    self.PasswordTable.setItem(i, 3, QTableWidgetItem(s[3]))
                    self.PasswordTable.setItem(i, 4, QTableWidgetItem(s[4]))
            self.actionCreate_A_Password.triggered.connect(self.createPass)
        else:
            self.label1.setText("Error. Please Select a .txt file made by the program. ")
            self.label1.adjustSize()

    def no(self):
        self.label1.setText("Create A Text File Storing the Passwords")
        self.label1.adjustSize()
        QtTest.QTest.qWait(200)
        fName = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")[0]
        if fName:
            with open(fName, "w") as f:
                f.write("made by tigerjade003 \n")
        self.s = fName
        rr = open(fName, "r")
        q = rr.readlines()
        self.PasswordTable.setRowCount(len(q) - 1)
        self.PasswordTable.show()
        self.label1.hide()
        self.label.setText("Passwords")
        self.ButtonNO.hide()
        self.ButtonYES.hide()
        self.ButtonAddPass.show()
        self.ButtonDeletePass.show()
        self.ButtonRefreshTable.show()
        self.ButtonAddPass.clicked.connect(self.createPass)
        self.ButtonDeletePass.clicked.connect(self.deletePass)
        self.ButtonRefreshTable.clicked.connect(self.refresh)
        pr = open(fName, "r")
        pr.readline()
        for i in range(len(q) - 1):
            s = pr.readline().strip("\n").split("|||")
            self.PasswordTable.insertRow(i)
            self.PasswordTable.setItem(i, 0, QTableWidgetItem(s[0]))
            self.PasswordTable.setItem(i, 1, QTableWidgetItem(s[1]))
            self.PasswordTable.setItem(i, 2, QTableWidgetItem(s[2]))
            self.PasswordTable.setItem(i, 3, QTableWidgetItem(s[3]))
            self.PasswordTable.setItem(i, 4, QTableWidgetItem(s[4]))
        self.actionCreate_A_Password.triggered.connect(self.createPass)

    def createPass(self):
        name = QInputDialog.getText(self, 'Name', 'Enter the Name of the Entry')[0]
        site = ""
        username = ""
        password = ""
        Description = ""
        if name != "":
            site = QInputDialog.getText(self, 'Website', 'Enter the website URL ')[0]
            if site != "":
                username = QInputDialog.getText(self, 'Username', 'Enter the Username, leave blank if ButtonNOne')[0]
                if username != "":
                    password = QInputDialog.getText(self, 'Password', 'Enter the Password')[0]
                    if password != "":
                        Description = QInputDialog.getText(self, 'Description', 'Enter the Description for the Entry')[0]
        with open(self.s, "a") as f:
            if site != "" and username != "" and password != "":
                f.write(name + "|||" + site + "|||" + username + "|||" + password + "|||" + Description)
                f.write("\n")
        self.updatetable()

    def updatetable(self):
        rrr = ""
        with open(self.s, "r") as qq:
            rrr = qq.readlines()
        rr = open(self.s, "r")
        rr.readline()

        self.PasswordTable.setRowCount(len(rrr) - 1)
        for i in range(len(rrr) - 1):
            s = rr.readline().strip("\n").split("|||")
            self.PasswordTable.setItem(i, 0, QTableWidgetItem(s[0]))
            self.PasswordTable.setItem(i, 1, QTableWidgetItem(s[1]))
            self.PasswordTable.setItem(i, 2, QTableWidgetItem(s[2]))
            self.PasswordTable.setItem(i, 3, QTableWidgetItem(s[3]))
            self.PasswordTable.setItem(i, 4, QTableWidgetItem(s[4]))

    def deletePass(self):
        name = QInputDialog.getText(self, 'Delete', 'Enter the Name of the Entry You Want to Delete')[0]
        if name != "":
            with open(self.s, "r") as a:
                with open("123456789012345678901234567890.txt", "w") as b:
                    for line in a:
                        if not line.strip("\n").startswith(name):
                            b.write(line)
            with open(self.s, "w") as a:
                with open("123456789012345678901234567890.txt", "r") as b:
                    for line in b:
                        a.write(line)
            os.remove("123456789012345678901234567890.txt")
            self.refresh()

    def refresh(self):
        rrr = ""
        self.PasswordTable.show()
        self.ButtonRefreshTable.show()
        self.ButtonDeletePass.show()
        self.ButtonAddPass.show()
        self.ButtonMain.hide()
        self.ButtonDone.hide()
        self.label3.hide()
        self.label.setText("Passwords")
        with open(self.s, "r") as qq:
            rrr = qq.readlines()
        rr = open(self.s, "r")
        rr.readline()
        self.PasswordTable.setRowCount(len(rrr) - 1)
        for i in range(len(rrr) - 1):
            s = rr.readline().strip("\n").split("|||")
            self.PasswordTable.setItem(i, 0, QTableWidgetItem(s[0]))
            self.PasswordTable.setItem(i, 1, QTableWidgetItem(s[1]))
            self.PasswordTable.setItem(i, 2, QTableWidgetItem(s[2]))
            self.PasswordTable.setItem(i, 3, QTableWidgetItem(s[3]))
            self.PasswordTable.setItem(i, 4, QTableWidgetItem(s[4]))

    def help(self):
        self.PasswordTable.hide()
        self.ButtonRefreshTable.hide()
        self.ButtonDeletePass.hide()
        self.ButtonAddPass.hide()
        self.ButtonMain.hide()
        self.ButtonNO.hide()
        self.ButtonYES.hide()
        self.ButtonDone.show()
        self.label.setText("Bugs? Fill out this form: https://forms.gle/56Ji4WjngUNE3tTS9")
        self.label3.setText("Need Help? Fill out this form: https://forms.gle/SiKxrCUGnXr4qLuEA")
        self.label3.adjustSize()
        self.label3.show()
        self.label.adjustSize()
        if self.s != "":
            self.ButtonDone.clicked.connect(self.refresh)
        else:
            self.ButtonDone.clicked.connect(self.clicker)

    def FAQ(self):
        self.PasswordTable.hide()
        self.ButtonRefreshTable.hide()
        self.ButtonDeletePass.hide()
        self.ButtonAddPass.hide()
        self.ButtonMain.hide()
        self.ButtonNO.hide()
        self.ButtonYES.hide()
        self.ButtonDone.show()
        self.label.setText("Read the FAQ's here: https://tinyurl.com/PasswordFAQs")
        self.label.adjustSize()
        if self.s != "":
            self.ButtonDone.clicked.connect(self.refresh)
        else:
            self.ButtonDone.clicked.connect(self.clicker)

    def before(self):
        self.label1.setText("You have not chosen or created a password file yet. Please create or choose one first.")
        self.label1.adjustSize()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())
