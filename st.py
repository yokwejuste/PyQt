# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'steve.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 564)
        MainWindow.setStyleSheet(
            "/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 200, 0.1), "
            "stop:1 rgba(150, 0, 73, 0.2));*/\n "
            "background-color: pink;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 20, 201, 71))
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: rgb(138, 226, 52);\n"
                                 "border-radius: 30%;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 51, 21))
        self.label_2.setStyleSheet("border-box: 20%;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 380, 51, 21))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(170, 130, 111, 26))
        self.comboBox.setStyleSheet("display: block;\n"
                                    "background-color: #fff;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 200, 111, 26))
        self.comboBox_2.setStyleSheet("display: block;\n"
                                      "background-color: #fff;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 280, 113, 26))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 370, 113, 26))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(302, 130, 21, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 450, 95, 26))
        self.pushButton.setStyleSheet("border: 70% solid black;\n"
                                      "color: white;\n"
                                      "background-color: blue;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 130, 221, 181))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(340, 380, 221, 111))
        self.lineEdit_3.setObjectName("lineEdit_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Crop Guide Software"))
        self.label.setText(_translate("MainWindow", "CROP GUIDE"))
        self.label_2.setText(_translate("MainWindow", "State"))
        self.label_3.setText(_translate("MainWindow", "Season"))
        self.label_4.setText(_translate("MainWindow", "Budget"))
        self.label_5.setText(_translate("MainWindow", "Acres"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Cameroon"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Ghana"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Nigeria"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Gabon"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Congo"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Guinea"))
        self.comboBox.setItemText(6, _translate("MainWindow", "India"))
        self.comboBox.setItemText(7, _translate("MainWindow", "USA"))
        self.comboBox.setItemText(8, _translate("MainWindow", "Mexico"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Summer"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Winter"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Autumn"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Spring"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))


        def clicked():
            print("clicked")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
