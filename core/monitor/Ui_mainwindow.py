# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lin\Desktop\Pyquino\core\monitor\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(852, 667)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEditSent = QtWidgets.QTextEdit(self.centralWidget)
        self.textEditSent.setGeometry(QtCore.QRect(260, 220, 471, 171))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEditSent.setFont(font)
        self.textEditSent.setObjectName("textEditSent")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 231, 361))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.comboBoxPort = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxPort.setGeometry(QtCore.QRect(90, 30, 121, 31))
        self.comboBoxPort.setObjectName("comboBoxPort")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 80, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.comboBoxBaud = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBaud.setGeometry(QtCore.QRect(90, 80, 121, 31))
        self.comboBoxBaud.setObjectName("comboBoxBaud")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.comboBoxCheckSum = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxCheckSum.setGeometry(QtCore.QRect(90, 130, 121, 31))
        self.comboBoxCheckSum.setObjectName("comboBoxCheckSum")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.comboBoxBits = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxBits.setGeometry(QtCore.QRect(90, 180, 121, 31))
        self.comboBoxBits.setObjectName("comboBoxBits")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 230, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.comboBoxStopBits = QtWidgets.QComboBox(self.groupBox)
        self.comboBoxStopBits.setGeometry(QtCore.QRect(90, 230, 121, 31))
        self.comboBoxStopBits.setObjectName("comboBoxStopBits")
        self.pushButtonOpenSerial = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonOpenSerial.setGeometry(QtCore.QRect(10, 280, 201, 31))
        self.pushButtonOpenSerial.setObjectName("pushButtonOpenSerial")
        self.textEditReceived = QtWidgets.QTextEdit(self.centralWidget)
        self.textEditReceived.setGeometry(QtCore.QRect(260, 30, 541, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditReceived.sizePolicy().hasHeightForWidth())
        self.textEditReceived.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEditReceived.setFont(font)
        self.textEditReceived.setReadOnly(True)
        self.textEditReceived.setObjectName("textEditReceived")
        self.pushButtonSendData = QtWidgets.QPushButton(self.centralWidget)
        self.pushButtonSendData.setGeometry(QtCore.QRect(740, 220, 61, 171))
        self.pushButtonSendData.setObjectName("pushButtonSendData")
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 852, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuMointor = QtWidgets.QMenu(self.menuBar)
        self.menuMointor.setObjectName("menuMointor")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSend = QtWidgets.QAction(MainWindow)
        self.actionSend.setObjectName("actionSend")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionVrep = QtWidgets.QAction(MainWindow)
        self.actionVrep.setObjectName("actionVrep")
        self.actionOpenGL = QtWidgets.QAction(MainWindow)
        self.actionOpenGL.setObjectName("actionOpenGL")
        self.actionControl = QtWidgets.QAction(MainWindow)
        self.actionControl.setObjectName("actionControl")
        self.menuFile.addAction(self.actionSend)
        self.menuFile.addAction(self.actionExit)
        self.menuMointor.addAction(self.actionVrep)
        self.menuMointor.addAction(self.actionOpenGL)
        self.menuMointor.addAction(self.actionControl)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuMointor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEditSent.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'PMingLiU\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "com setting"))
        self.label_2.setText(_translate("MainWindow", "com"))
        self.label.setText(_translate("MainWindow", "baurd"))
        self.label_3.setText(_translate("MainWindow", "first"))
        self.label_4.setText(_translate("MainWindow", "data"))
        self.label_5.setText(_translate("MainWindow", "stop"))
        self.pushButtonOpenSerial.setText(_translate("MainWindow", "open"))
        self.pushButtonSendData.setText(_translate("MainWindow", "send"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMointor.setTitle(_translate("MainWindow", "Mointor"))
        self.actionSend.setText(_translate("MainWindow", "send Gcode"))
        self.actionExit.setText(_translate("MainWindow", "exit"))
        self.actionVrep.setText(_translate("MainWindow", "Vrep"))
        self.actionOpenGL.setText(_translate("MainWindow", "OpenGL"))
        self.actionControl.setText(_translate("MainWindow", "Control"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

