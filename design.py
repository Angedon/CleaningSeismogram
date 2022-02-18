# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Gleb1\Downloads\design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(592, 246)
        MainWindow.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #f5f0e1;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.ButtonLoad = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ButtonLoad.sizePolicy().hasHeightForWidth())
        self.ButtonLoad.setSizePolicy(sizePolicy)
        self.ButtonLoad.setMinimumSize(QtCore.QSize(0, 0))
        self.ButtonLoad.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ButtonLoad.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #1e3d59;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.ButtonLoad.setObjectName("ButtonLoad")
        self.verticalLayout.addWidget(self.ButtonLoad)
        self.ButtonBefore = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonBefore.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #1e3d59;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.ButtonBefore.setObjectName("ButtonBefore")
        self.verticalLayout.addWidget(self.ButtonBefore)
        self.ButtonAfter = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonAfter.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #1e3d59;\n"
"    font-family: Rubik;\n"
"    font-size: 16pt;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #888;\n"
"}")
        self.ButtonAfter.setObjectName("ButtonAfter")
        self.verticalLayout.addWidget(self.ButtonAfter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ButtonLoad.setText(_translate("MainWindow", "Load segy file"))
        self.ButtonBefore.setText(_translate("MainWindow", "Seismo trace before CNN"))
        self.ButtonAfter.setText(_translate("MainWindow", "Seismo trace after CNN"))
