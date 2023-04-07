from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog, QWidget, QSizePolicy, QTableWidget, QInputDialog
from PyQt5.QtCore import Qt
import sys


class Ui_MainWindow(QWidget):
    s = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setAutoFillBackground(False)
        #central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #Password Table
        self.PasswordTable = QTableWidget(self.centralwidget)
        self.PasswordTable.setObjectName(u"tableWidget")
        self.PasswordTable.setGeometry(QtCore.QRect(100, 125, 3050, 1450))
        self.PasswordTable.setColumnCount(3)
        self.PasswordTable.alternatingRowColors()

        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.PasswordTable.setHorizontalHeaderItem(2, item)
        self.PasswordTable.hide()
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(1400, 100, 400, 50))
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(1200, 100, 400, 50))
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(1800, 100, 400, 50))
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(2800, 50, 300, 50)
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(200, 50, 300, 50)
        self.Button4.hide()
        self.Button2.hide()
        self.Button3.hide()
        self.Button5.hide()
        self.Button1.setFont(QFont('Times', 15))
        self.Button2.setFont(QFont('Times', 15))
        self.Button3.setFont(QFont('Times', 15))
        self.Button4.setFont(QFont('Times', 15))
        self.Button5.setFont(QFont('Times', 15))
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(100, 200, 100, 100))
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1325, 20, 550, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        font1 = QtGui.QFont()
        font1.setPointSize(10)
        self.label1.setFont(font1)
        self.label.setWordWrap(False)
        self.label1.setObjectName("Label1")
        self.label1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label.setFont(font)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(Qt.AlignCenter)
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
        self.actionFAQ_s.triggered.connect(lambda: self.clicked("You clicked Frequently Asked Questions"))
        self.actionfurther_help.triggered.connect(lambda: self.clicked("You clicked to ask for more help"))
        self.Button1.clicked.connect(self.clicker)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setStatusTip(_translate("MainWindow", "Start Using the Password Manager"))
        item = self.PasswordTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Website"))
        item = self.PasswordTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Username"))
        item = self.PasswordTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Password"))
        self.Button1.setStatusTip(_translate("MainWiindow", "Get Started"))
        self.Button1.setText(_translate("MainWindow", "Get Started"))
        self.Button2.setStatusTip(_translate("MainWindow", "NO"))
        self.Button2.setText(_translate("MainWindow", "NO"))
        self.Button3.setStatusTip(_translate("MainWindow", "YES"))
        self.Button3.setText(_translate("MainWindow", "YES"))
        self.Button4.setStatusTip(_translate("MainWindow", "Add A Password"))
        self.Button4.setText(_translate("MainWindow", "Add A Password"))
        self.Button5.setStatusTip(_translate("MainWindow", "Delete A Password"))
        self.Button5.setText(_translate("MainWindow", "Delete A Password"))
        self.label1.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "Password Manager"))
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

    # going to be deleted in the future
    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def clicker(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button1.hide()
        self.menubar.show()
        self.label.setText("Do you have a password file stored on this computer?")
        self.label.setGeometry(1000, 20, 550, 75)
        self.label.adjustSize()
        self.Button2.show()
        self.Button3.show()
        self.Button3.clicked.connect(self.yes)
        self.Button2.clicked.connect(self.no)

    def yes(self):
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
            self.PasswordTable.setRowCount(len(q) - 1)
            self.PasswordTable.show()
            self.label1.hide()
            self.label.setText("Passwords")
            self.Button2.hide()
            self.Button3.hide()
            self.Button4.show()
            self.Button5.show()
            self.Button4.clicked.connect(self.createPass)
            self.Button5.clicked.connect(self.deletePass)
            pr = open(qr, "r")
            pr.readline()
            for i in range(len(q)-1):
                self.PasswordTable.setItem(self, i, 0, pr.read())
                self.PasswordTable.setItem(self, i, 1, pr.read())
                self.PasswordTable.setItem(self, i, 2, pr.read())
            self.actionCreate_A_Password.triggered.connect(self.createPass)
        else:
            self.label1.setText("Error. Please Select a .txt file made by the program. ")
            self.label1.adjustSize()

    def no(self):
        self.label1.setText("Create A Text File Storing the Passwords")
        self.label1.adjustSize()
        QtTest.QTest.qWait(200)
        fName, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
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
        self.Button2.hide()
        self.Button3.hide()
        self.Button4.show()
        self.Button5.show()
        self.Button4.clicked.connect(self.create)
        self.button5.clicked.connect(self.deletePass())
        self.actionCreate_A_Password.triggered.connect(self.createPass)

    def createPass(self):
        site, d1 = QInputDialog.getText(self, 'Website ', 'Enter the website URL ')
        username, d2 = QInputDialog.getText(self, 'Username', 'Enter the Username, leave blank if none')
        password, d3 = QInputDialog.getText(self, 'Password', 'Enter the Password')
        if d1 and d2 and d3:
            with open(self.s, "a") as f:
                f.write(site + " " + username + " " + password)
                self.updatetable()

    def updatetable(self):
        print("Updating Table")

    def deletePass(self):
        print("Deleting Password")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())
