from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys
import wave
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import struct
import pylab as pl



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Звуковая волна")
        MainWindow.resize(644, 544)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 1024))
        self.label.setText("!!!!!!")
        pixmap = QtGui.QPixmap()
        self.label.setPixmap(pixmap)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 644, 21))
        self.menubar.setObjectName("menubar")
        self.menu1 = QtWidgets.QMenu(self.menubar)
        self.menu1.setObjectName("menu1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.menu1.addAction(self.action)
        self.menu1.addAction(self.action_2)
        self.menu1.addAction(self.action_3)
        self.menubar.addAction(self.menu1.menuAction())


        self.menu2 = QtWidgets.QMenu(self.menubar)
        self.menu2.setObjectName("menu2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        # self.action_5 = QtWidgets.QAction(MainWindow)
        # self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")

        self.menu2.addAction(self.action_4)
        # self.menu2.addAction(self.action_5)
        self.menu2.addAction(self.action_6)
        self.menubar.addAction(self.menu2.menuAction())

        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.pushButton_3.clicked.connect(QtWidgets.qApp.quit)
        # self.pushButton.clicked.connect(self.on_clicked)
        # self.pushButton_2.clicked.connect(self.clear)

        # self.action.triggered.connect(self.on_clicked)
        # self.action_2.triggered.connect(self.clear)
        # self.action_3.triggered.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Звуковая волна"))
        self.pushButton.setText(_translate("MainWindow", "Открыть"))
        self.pushButton_2.setText(_translate("MainWindow", "Очистить форму"))
        self.pushButton_3.setText(_translate("MainWindow", "Закрыть"))
        self.menu1.setTitle(_translate("MainWindow", "Файл"))
        self.action.setText(_translate("MainWindow", "Открыть"))
        self.action_2.setText(_translate("MainWindow", "Очистить форму"))
        self.action_3.setText(_translate("MainWindow", "Закрыть"))

        self.menu2.setTitle(_translate("MainWindow", "Действие"))
        self.action_4.setText(_translate("MainWindow", "Перевести в моно"))
        # self.action_5.setText(_translate("MainWindow", "Перевести в стерео"))
        self.action_6.setText(_translate("MainWindow", "Построить звуковую волну"))

