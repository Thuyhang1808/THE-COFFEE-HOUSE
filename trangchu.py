from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 860)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1561, 51))
        self.frame.setStyleSheet("QFrame { \n"
"    background-color: rgba(255, 226, 255, 1); /* Màu nền trắng, trong suốt 90% */\n"
"    padding: 16px;\n"
"}\n"
"#label { \n"
"    background-color: rgba(255, 226, 255);\n"
"    font-size: 29px;\n"
"    color: #ff3c4f;\n"
"}\n"
"#label_2 {\n"
"    font-size: 23px;\n"
"    font-weight: bold;\n"
"    color: #ff547c;\n"
"    text-align: center;\n"
"}\n"
"#pushButton_11{\n"
"    background-color: rgba(255, 226, 255);\n"
"   color: #4858c3;\n"
" border-radius: 15px;\n"
" font-size: 21px;\n"
"}\n"
"#pushButton_11:hover {\n"
"color: #b42238}\n"
"#pushButton_10{\n"
"    background-color: rgba(255, 226, 255);\n"
"   color: #4858c3;\n"
" border-radius: 15px;\n"
" font-size: 21px;\n"
"}\n"
"#pushButton_10:hover {\n"
"color: #b42238}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setGeometry(QtCore.QRect(-10, -10, 91, 71))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 0, 191, 61))
        self.label_2.setObjectName("label_2")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_10.setGeometry(QtCore.QRect(1350, 10, 131, 31))
        self.pushButton_10.setFlat(True)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.frame)
        self.pushButton_11.setGeometry(QtCore.QRect(1260, 10, 81, 31))
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(True)
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2.raise_()
        self.label.raise_()
        self.pushButton_10.raise_()
        self.pushButton_11.raise_()
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 110, 920, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("#lineEdit {\n"
"    font-size: 14px;\n"
"    color: #7e7e7e;\n"
"background-color: #ffffff;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 110, 50, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("#pushButton {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 9px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton :hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 50, 971, 61))
        self.widget.setStyleSheet("QWidget {  \n"
"    background-color: rgba(245, 255, 255,1); /* Màu nền trắng, trong suốt 90% */\n"
"    padding: 14px;\n"
"}\n"
"#pushButton_5 {\n"
"    background-color: #f5f5f5; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a5aab1; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_5:hover {\n"
"    background-color: #ffffff;\n"
"}\n"
"#pushButton_4 {\n"
"    background-color: #f5f5f5; /* Màu nền */\n"
"    color:#ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a5aab1; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_4:hover {\n"
"    background-color: #ffffff;\n"
"}\n"
"#pushButton_3 {\n"
"    background-color: #f5f5f5; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a5aab1; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_3:hover {\n"
"    background-color: #ffffff;\n"
"}\n"
"#pushButton_2 {\n"
"    background-color: #f5f5f5; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a5aab1; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_2:hover {\n"
"    background-color: #ffffff;\n"
"}\n"
"#pushButton_6 {\n"
"    background-color: #f5f5f5; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a5aab1; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_6:hover {\n"
"    background-color: #ffffff;\n"
"}")
        self.widget.setObjectName("widget")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 91, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 10, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 10, 93, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 10, 81, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(430, 10, 101, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(970, 50, 591, 751))
        self.frame_4.setStyleSheet("#frame_4 {  \n"
"    background-color: rgba(226, 255, 253,1); /* Màu nền trắng, trong suốt 90% */\n"
"    padding: 14px;\n"
"}\n"
"#frame_4 {\n"
"    border: none;\n"
"    border-left: 4px solid #7e7e7e;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("#lineEdit_2 {\n"
"    border-color: rgb(255, 219, 255);\n"
"    font-size: 16px;\n"
"  background-color: #ffffff;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #acc2ff;\n"
"}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("#pushButton_9 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 9px;\n"
"    font-size: 16px;\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_9 :hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 80, 581, 41))
        self.lineEdit_4.setStyleSheet("  background-color: #ffffff;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #acc2ff;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(310, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("  background-color: #ffffff;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #acc2ff;")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 160, 581, 351))
        self.tableWidget.setStyleSheet("  background-color: #ffffff;\n"
"color: rgb(0, 0, 0);\n"
" border: 1px solid #a5aab1;")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_4)
        self.label_10.setGeometry(QtCore.QRect(160, 530, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_12.setGeometry(QtCore.QRect(205, 578, 31, 29))
        self.pushButton_12.setStyleSheet("#pushButton_12 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"border-radius: 20px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_12:hover {\n"
"    background-color: #bfbfbf;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_13.setGeometry(QtCore.QRect(440, 580, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("#pushButton_13 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"border-radius: 20px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_13:hover {\n"
"    background-color: #bfbfbf;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(322, 580, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet("#pushButton_14 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"border-radius: 20px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_14:hover {\n"
"    background-color: #bfbfbf;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(310, 530, 171, 31))
        self.lineEdit_7.setStyleSheet("  background-color: #ffffff;\n"
"color: rgb(0, 0, 0);\n"
"border: 1px solid #acc2ff;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_15 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_15.setGeometry(QtCore.QRect(82, 580, 71, 28))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet("#pushButton_15 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"border-radius: 20px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_15:hover {\n"
"    background-color: #bfbfbf;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_15.setFlat(False)
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_16.setGeometry(QtCore.QRect(250, 577, 31, 29))
        self.pushButton_16.setStyleSheet("#pushButton_16 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 5px;\n"
"    font-size: 16px;\n"
"border-radius: 20px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_16:hover {\n"
"    background-color: #bfbfbf;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_17.setGeometry(QtCore.QRect(60, 640, 111, 61))
        self.pushButton_17.setStyleSheet("#pushButton_17 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"border-radius: 15px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_17:hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_18.setGeometry(QtCore.QRect(190, 640, 111, 61))
        self.pushButton_18.setStyleSheet("#pushButton_18 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"border-radius: 15px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_18:hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_19.setGeometry(QtCore.QRect(320, 640, 101, 61))
        self.pushButton_19.setStyleSheet("#pushButton_19 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"border-radius: 15px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_19:hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_20.setGeometry(QtCore.QRect(440, 640, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setStyleSheet("#pushButton_20 {\n"
"    background-color: #ffedff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"border-radius: 15px; /* Bo góc */\n"
"    border: 1px solid #a31831; /* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_20:hover {\n"
"    background-color: #ffffff;\n"
" border: 1px solid #38a3a5;\n"
"}")
        self.pushButton_20.setObjectName("pushButton_20")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 150, 971, 651))
        self.scrollArea.setStyleSheet("QScrollArea{ \n"
"    background-color: rgba(255, 255, 255,1); /* Màu nền trắng, trong suốt 90% */\n"
"    padding: 14px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 941, 621))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.groupBox = QtWidgets.QGroupBox(parent=self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1600, 860))
        self.groupBox.setStyleSheet("QGroupBox {  \n"
"    background-color: rgba(255, 243, 253,1); /* Màu nền trắng, trong suốt 90% */\n"
"   padding: 14px; \n"
"}")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_23 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_23.setGeometry(QtCore.QRect(700, 20, 211, 241))
        self.pushButton_23.setStyleSheet("\n"
"#pushButton_23 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_23:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_23.setText("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_25 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_25.setGeometry(QtCore.QRect(470, 20, 211, 241))
        self.pushButton_25.setStyleSheet("\n"
"#pushButton_25 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_25:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(474, 24, 203, 161))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/4.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.pushButton_26 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_26.setGeometry(QtCore.QRect(730, 180, 151, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setStyleSheet("#pushButton_26 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_26:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(-250, 910, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_27 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_27.setGeometry(QtCore.QRect(700, 310, 211, 241))
        self.pushButton_27.setStyleSheet("\n"
"#pushButton_27 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_27:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(14, 24, 203, 161))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setLineWidth(1)
        self.label_3.setText("")
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(-270, 590, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(50, 510, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(704, 24, 203, 161))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/6.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(-280, 560, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("#pushButton_7 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_7:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_7.setAutoRepeat(False)
        self.pushButton_7.setAutoDefault(False)
        self.pushButton_7.setDefault(False)
        self.pushButton_7.setFlat(False)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_24 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_24.setGeometry(QtCore.QRect(510, 180, 140, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setStyleSheet("#pushButton_24 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_24:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_32 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_32.setGeometry(QtCore.QRect(110, 850, 151, 211))
        self.pushButton_32.setStyleSheet("\n"
"#pushButton_28 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_28:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton_27\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>690</x>\n"
"     <y>10</y>\n"
"     <width>151</width>\n"
"     <height>211</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">\n"
"#pushButton_27 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_27:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 20, 211, 241))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("#pushButton_8 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_8:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_8.setText("")
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setFlat(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(520, 220, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.pushButton_21 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_21.setGeometry(QtCore.QRect(-270, 860, 141, 43))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setStyleSheet("#pushButton_21 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_21:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_21.setObjectName("pushButton_21")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(243, 24, 203, 161))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/5.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setObjectName("label_7")
        self.pushButton_28 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_28.setGeometry(QtCore.QRect(240, 20, 211, 241))
        self.pushButton_28.setStyleSheet("\n"
"#pushButton_28 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_28:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton_27\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>690</x>\n"
"     <y>10</y>\n"
"     <width>151</width>\n"
"     <height>211</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">\n"
"#pushButton_27 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_27:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.pushButton_28.setText("")
        self.pushButton_28.setObjectName("pushButton_28")
        self.pushButton_22 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_22.setGeometry(QtCore.QRect(-150, 840, 158, 191))
        self.pushButton_22.setStyleSheet("\n"
"#pushButton_22 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_22:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_29 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_29.setGeometry(QtCore.QRect(470, 310, 211, 241))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setStyleSheet("\n"
"#pushButton_29 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_29:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}")
        self.pushButton_29.setText("")
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_30.setGeometry(QtCore.QRect(240, 310, 211, 241))
        self.pushButton_30.setStyleSheet("\n"
"#pushButton_30 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_30:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton_29\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>470</x>\n"
"     <y>310</y>\n"
"     <width>211</width>\n"
"     <height>241</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">\n"
"#pushButton_29 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_29:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_31.setGeometry(QtCore.QRect(10, 310, 211, 241))
        self.pushButton_31.setStyleSheet("\n"
"#pushButton_31 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_31:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
"<ui version=\"4.0\">\n"
" <widget name=\"__qt_fake_top_level\">\n"
"  <widget class=\"QPushButton\" name=\"pushButton_29\">\n"
"   <property name=\"geometry\">\n"
"    <rect>\n"
"     <x>470</x>\n"
"     <y>310</y>\n"
"     <width>211</width>\n"
"     <height>241</height>\n"
"    </rect>\n"
"   </property>\n"
"   <property name=\"styleSheet\">\n"
"    <string notr=\"true\">\n"
"#pushButton_29 {\n"
"    background-color: #ffffff; /* Màu nền */\n"
"    color: #ff2c5d; /* Màu chữ */\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"    border-left: 1px solid #c1c1c1; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #c1c1c1;\n"
"    border-right: 2px solid #9e9e9e;\n"
"    border-bottom: 2px solid #9e9e9e;\n"
";/* Viền màu đỏ hồng */\n"
"}\n"
"\n"
"#pushButton_29:hover {\n"
"border-left: 1px solid #ff6011; /* Chỉ có viền trái */\n"
"    border-top: 1px solid #ff6011;\n"
"    border-right: 3px solid #ff6011;\n"
"    border-bottom: 3px solid #ff6011;\n"
" background-color: #ffffff; \n"
"}</string>\n"
"   </property>\n"
"   <property name=\"text\">\n"
"    <string/>\n"
"   </property>\n"
"  </widget>\n"
" </widget>\n"
" <resources/>\n"
"</ui>\n"
"")
        self.pushButton_31.setText("")
        self.pushButton_31.setObjectName("pushButton_31")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(702, 312, 206, 161))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/7.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(472, 312, 206, 161))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/8.jpg"))
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(241, 312, 206, 161))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/10.jpg"))
        self.label_14.setScaledContents(True)
        self.label_14.setWordWrap(False)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(12, 312, 206, 161))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(r"C:\Users\THUYHANG-PC\Documents\BTL Lập trình Python\image\menu/11.jpg"))
        self.label_15.setScaledContents(True)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.pushButton_33 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_33.setGeometry(QtCore.QRect(731, 474, 135, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setStyleSheet("#pushButton_33{\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_33:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_34.setGeometry(QtCore.QRect(500, 470, 161, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_34.setFont(font)
        self.pushButton_34.setStyleSheet("#pushButton_34{\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_34:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_35.setGeometry(QtCore.QRect(270, 470, 151, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("#pushButton_35 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_35:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_35.setObjectName("pushButton_35")
        self.pushButton_36 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_36.setGeometry(QtCore.QRect(20, 470, 181, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("#pushButton_36 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_36:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_36.setObjectName("pushButton_36")
        self.pushButton_37 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_37.setGeometry(QtCore.QRect(40, 180, 140, 35))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("#pushButton_37 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_37:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.pushButton_38 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_38.setGeometry(QtCore.QRect(271, 162, 140, 61))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("#pushButton_38 {\n"
"    background-color: #ffffff;\n"
"    color: #ff2c5d;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    font-size: 16px;\n"
"}\n"
"\n"
"#pushButton_38:hover {\n"
"   color: #d0cbff;\n"
"}")
        self.pushButton_38.setObjectName("pushButton_38")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(280, 510, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(520, 510, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(50, 220, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(280, 220, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_20.setGeometry(QtCore.QRect(750, 220, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_21.setGeometry(QtCore.QRect(740, 510, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_21.setObjectName("label_21")
        self.pushButton_28.raise_()
        self.label_7.raise_()
        self.pushButton_31.raise_()
        self.pushButton_8.raise_()
        self.pushButton_23.raise_()
        self.pushButton_25.raise_()
        self.label_5.raise_()
        self.pushButton_26.raise_()
        self.label_6.raise_()
        self.pushButton_27.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.pushButton_7.raise_()
        self.pushButton_24.raise_()
        self.pushButton_32.raise_()
        self.label_11.raise_()
        self.pushButton_21.raise_()
        self.pushButton_22.raise_()
        self.label_3.raise_()
        self.pushButton_29.raise_()
        self.pushButton_30.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.pushButton_33.raise_()
        self.pushButton_34.raise_()
        self.pushButton_35.raise_()
        self.pushButton_36.raise_()
        self.pushButton_37.raise_()
        self.pushButton_38.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.raise_()
        self.frame_4.raise_()
        self.frame.raise_()
        self.widget.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1600, 26))
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
        self.label.setText(_translate("MainWindow", "🏡"))
        self.label_2.setText(_translate("MainWindow", "Coffee house"))
        self.pushButton_10.setText(_translate("MainWindow", "🚀Đăng xuất"))
        self.pushButton_11.setText(_translate("MainWindow", "📦Kho"))
        self.lineEdit.setText(_translate("MainWindow", "Nhập mã/Tên món..."))
        self.pushButton.setText(_translate("MainWindow", "🔍"))
        self.pushButton_3.setText(_translate("MainWindow", "📋Tất cả"))
        self.pushButton_4.setText(_translate("MainWindow", "🥤Special Tea"))
        self.pushButton_5.setText(_translate("MainWindow", "☕Coffee"))
        self.pushButton_2.setText(_translate("MainWindow", "🍰Bánh"))
        self.pushButton_6.setText(_translate("MainWindow", "🍮Topping"))
        self.lineEdit_2.setText(_translate("MainWindow", "Mã khuyến mại"))
        self.pushButton_9.setText(_translate("MainWindow", "🔍"))
        self.lineEdit_4.setText(_translate("MainWindow", "Ghi chú yêu cầu khách hàng...."))
        self.lineEdit_3.setText(_translate("MainWindow", "Mã đơn hàng"))
        self.label_10.setText(_translate("MainWindow", "Tổng thành tiền:"))
        self.pushButton_12.setText(_translate("MainWindow", "<<"))
        self.pushButton_13.setText(_translate("MainWindow", "Xóa"))
        self.pushButton_14.setText(_translate("MainWindow", "Sửa "))
        self.pushButton_15.setText(_translate("MainWindow", "Thêm"))
        self.pushButton_16.setText(_translate("MainWindow", ">>"))
        self.pushButton_17.setText(_translate("MainWindow", "In hóa đơn"))
        self.pushButton_18.setText(_translate("MainWindow", "Lưu hóa đơn"))
        self.pushButton_19.setText(_translate("MainWindow", "Thông báo"))
        self.pushButton_20.setText(_translate("MainWindow", "Thanh toán"))
        self.pushButton_26.setText(_translate("MainWindow", "PhinDi Kem Sữa"))
        self.label_6.setText(_translate("MainWindow", "Giá : 45,000 VNĐ"))
        self.label_4.setText(_translate("MainWindow", "Giá : 55,000 VNĐ"))
        self.label_8.setText(_translate("MainWindow", "Giá : 55,000 VNĐ"))
        self.pushButton_7.setText(_translate("MainWindow", "PhinDi Cassia"))
        self.pushButton_24.setText(_translate("MainWindow", "PhinDi Choco"))
        self.label_11.setText(_translate("MainWindow", "Giá : 45,000 VNĐ"))
        self.pushButton_21.setText(_translate("MainWindow", "PhinDi Choco"))
        self.pushButton_33.setText(_translate("MainWindow", "Latte"))
        self.pushButton_34.setText(_translate("MainWindow", "Freeze Trà Xanh"))
        self.pushButton_35.setText(_translate("MainWindow", "Freeze Sô-cô-la"))
        self.pushButton_36.setText(_translate("MainWindow", "Classic Phin Freeze"))
        self.pushButton_37.setText(_translate("MainWindow", "PhinDi Cassia"))
        self.pushButton_38.setText(_translate("MainWindow", "PhinDi\n"
"Hạnh Nhân"))
        self.label_16.setText(_translate("MainWindow", "Giá : 55,000 VNĐ"))
        self.label_17.setText(_translate("MainWindow", "Giá : 55,000 VNĐ"))
        self.label_18.setText(_translate("MainWindow", "Giá : 55,000 VNĐ"))
        self.label_19.setText(_translate("MainWindow", "Giá : 45,000 VNĐ"))
        self.label_20.setText(_translate("MainWindow", "Giá : 45,000 VNĐ"))
        self.label_21.setText(_translate("MainWindow", "Giá : 99,000 VNĐ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
