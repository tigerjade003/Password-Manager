from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtWidgets import QFileDialog, QMainWindow, QWidget, QSizePolicy, QLineEdit, QInputDialog
from PyQt5.QtCore import Qt, QDir
import tkinter as tk
import sys


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        root = tk.Tk()
        sc_wi = root.winfo_screenwidth()
        sc_he = root.winfo_screenheight()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(1500, 100, 170, 23))
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(1200, 100, 170, 23))
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(1800, 100, 170, 23))
        self.Button2.hide()
        self.Button3.hide()
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
        self.actionCreate_A_Password.triggered.connect(lambda: self.clicked("You clicked Create A Pasword"))
        self.actionFAQ_s.triggered.connect(lambda: self.clicked("You clicked Frequently Asked Questions"))
        self.actionfurther_help.triggered.connect(lambda: self.clicked("You clicked to ask for more help"))
        self.Button1.clicked.connect(self.clicker)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Button1.setStatusTip(_translate("MainWindow", "Start Using the Password Manager"))
        self.Button1.setText(_translate("MainWindow", "Get Started"))
        self.Button2.setStatusTip(_translate("MainWindow", "NO"))
        self.Button2.setText(_translate("MainWindow", "NO"))
        self.Button3.setStatusTip(_translate("MainWindow", "YES"))
        self.Button3.setText(_translate("MainWindow", "YES"))
        self.label1.setText(_translate("MainWindow", " "))
        self.label.setText(_translate("MainWindow", "Password Manager"))
        self.menuPassword_Creator.setTitle(_translate("MainWindow", "Password"))
        self.menuHelp.setStatusTip(_translate("MainWindow", "Help"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.Password.setText(_translate("MainWindow", "Create A Password"))
        self.Password.setStatusTip(_translate("MainWindow", "Create A New Password to Store"))
        self.Password.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionCreate_A_Password.setText(_translate("MainWindow", "Create A Password"))
        self.actionCreate_A_Password.setStatusTip(_translate("MainWindow", "Create A New  Password"))
        self.actionCreate_A_Password.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionFAQ_s.setText(_translate("MainWindow", "FAQ\'s"))
        self.actionFAQ_s.setStatusTip(_translate("MainWindow", "Frequently asked questions"))
        self.actionfurther_help.setText(_translate("MainWindow", "Help"))
        self.actionfurther_help.setStatusTip(_translate("MainWindow", "Find help"))
        self.actionfurther_help.setShortcut(_translate("MainWindow", "Ctrl+H"))

    def clicked(self, text):
        self.label.setText(text)
        self.label.adjustSize()

    def clicker(self):
        _translate = QtCore.QCoreApplication.translate
        self.Button1.hide()
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
        fName = QFileDialog.getOpenFileName(self, "Open Text File", "", "All Files(*) ;; Text Files(*.txt)")
        s = fName[0]
        if s.endswith(".txt"):
            i = 0
            while i < 5:
                self.label1.setText("Loading Password Manager.")
                self.label1.adjustSize()
                QtTest.QTest.qWait(200)
                self.label1.setText("Loading Password Manager..")
                self.label1.adjustSize()
                QtTest.QTest.qWait(200)
                self.label1.setText("Loading Password Manager...")
                self.label1.adjustSize()
                QtTest.QTest.qWait(200)
                i += 1
            self.label1.setText("Loaded Password Manager. ")
            self.label1.adjustSize()
        else:
            self.label1.setText("Error. Please Select a .txt File.")
            self.label1.adjustSize()

    def no(self):
        self.label1.setText("Create A Text File Storing the Passwords")
        self.label1.adjustSize()
        QtTest.QTest.qWait(200)
        name = QtWidgets.QInputDialog.getText(self, 'Input Text File Name', 'Enter your Text File Name:')[0]




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())
