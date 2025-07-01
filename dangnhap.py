from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 860)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.backgroundLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.backgroundLabel.setGeometry(QtCore.QRect(-10, -10, 1600, 860))
        font = QtGui.QFont()
        font.setFamily("MS Reference Specialty")
        self.backgroundLabel.setFont(font)
        self.backgroundLabel.setText("")
        self.backgroundLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.backgroundLabel.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/1.jpg"))
        self.backgroundLabel.setScaledContents(True)
        self.backgroundLabel.setWordWrap(True)
        self.backgroundLabel.setIndent(-1)
        self.backgroundLabel.setObjectName("backgroundLabel")
        self.loginFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.loginFrame.setGeometry(QtCore.QRect(850, 190, 351, 411))
        self.loginFrame.setStyleSheet("#loginFrame {\n"
"    background-color: rgba(255, 255, 255, 1); /* Màu nền trắng, trong suốt 90% */\n"
"    border-radius: 15px; /* Bo góc */\n"
"    padding: 20px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color: black;\n"                                      
"    border: 1px solid #ccc;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-size: 14px;\n"
"background-color: white;\n"
"}\n"
"QLineEdit:hover {\n"
"    background-color: #eff1ff;\n"
"}\n"
"#loginButton {\n"
"    background-color: #007bff;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#loginButton:hover {\n"
"    background-color: #0056b3;\n"
"}\n"
"\n"
"/* Nút Đăng ký */\n"
"#registerButton {\n"
"   background-color: #ffffff;\n"
"    color: #00aaff;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#registerButton:hover {\n"
"    color: #cc5500;\n"
"}\n"
"\n"
"/* Nút Quên mật khẩu */\n"
"#forgotPasswordButton {\n"
"    background-color: #ffffff;\n"
"    color: #ffaa00;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"#forgotPasswordButton:hover {\n"
"    color: #cc5500;\n"
"}\n"
"\n"
"#titleLabel {\n"
"    font-size: 25px;\n"
"    font-weight: bold;\n"
"    color: #ff547c;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#usernameLabel {\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"\n"
"#passwordLabel {\n"
"    background-color: #ffffff;\n"
"    font-size: 14px;\n"
"    color: #333;\n"
"}\n"
"")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.loginFrame.setObjectName("loginFrame")
        self.titleLabel = QtWidgets.QLabel(parent=self.loginFrame)
        self.titleLabel.setGeometry(QtCore.QRect(90, 30, 171, 21))
        self.titleLabel.setObjectName("titleLabel")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.loginFrame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 100, 281, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.loginFrame)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 160, 281, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.loginButton = QtWidgets.QPushButton(parent=self.loginFrame)
        self.loginButton.setGeometry(QtCore.QRect(30, 240, 281, 51))
        self.loginButton.setObjectName("loginButton")
        self.registerButton = QtWidgets.QPushButton(parent=self.loginFrame)
        self.registerButton.setGeometry(QtCore.QRect(120, 310, 91, 41))
        self.registerButton.setObjectName("registerButton")
        self.forgotPasswordButton = QtWidgets.QPushButton(parent=self.loginFrame)
        self.forgotPasswordButton.setGeometry(QtCore.QRect(100, 340, 141, 51))
        self.forgotPasswordButton.setStyleSheet("")
        self.forgotPasswordButton.setObjectName("forgotPasswordButton")
        self.usernameLabel = QtWidgets.QLabel(parent=self.loginFrame)
        self.usernameLabel.setGeometry(QtCore.QRect(40, 90, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setToolTipDuration(16)
        self.usernameLabel.setObjectName("usernameLabel")
        self.passwordLabel = QtWidgets.QLabel(parent=self.loginFrame)
        self.passwordLabel.setGeometry(QtCore.QRect(40, 150, 61, 16))
        self.passwordLabel.setObjectName("passwordLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1017, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Coffee house"))
        self.loginButton.setText(_translate("MainWindow", "Đăng nhập"))
        self.registerButton.setText(_translate("MainWindow", "Đăng ký"))
        self.forgotPasswordButton.setText(_translate("MainWindow", "Quên mật khẩu ?"))
        self.usernameLabel.setText(_translate("MainWindow", "Tài khoản"))
        self.passwordLabel.setText(_translate("MainWindow", "Mật khẩu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
