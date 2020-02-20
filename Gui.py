# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Uicapstone.ui'
#
# Created by: PyQt5 UI code generator 5.13.0


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyqtgraph as pg
from matplotlib import style
import sys
import threading
import time
from random import random

from PyQt5 import QtCore, QtGui, QtWidgets

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #setup UI#
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 632)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 15, 250, 45))

        #setup font
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        #setup graphics view
        self.graphicsView = pg.PlotWidget(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(20, 70, 1000, 180))
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView_2 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(20, 280, 1000, 180))
        self.graphicsView_2.setObjectName("graphicsView_2")
        

        self.graphicsView_3 = pg.PlotWidget(self.centralwidget)
        self.graphicsView_3.setGeometry(QtCore.QRect(20, 490, 1000, 180))
        self.graphicsView_3.setObjectName("graphicsView_3")

        #setup group box

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1050, 65, 270, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1050, 275, 270, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1050, 485, 270, 100))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(11)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")

        #setup Radio Button

        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(150, 20, 101, 30))
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 55, 101, 30))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 20, 101, 30))
        self.radioButton_3.setObjectName("radioButton_3")

        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_2)
        self.radioButton_4.setGeometry(QtCore.QRect(150, 55, 101, 30))
        self.radioButton_4.setObjectName("radioButton_4")

        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_5.setGeometry(QtCore.QRect(150, 20, 101, 30))
        self.radioButton_5.setObjectName("radioButton_5")

        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_3)
        self.radioButton_6.setGeometry(QtCore.QRect(150, 55, 101, 30))
        self.radioButton_6.setObjectName("radioButton_6")

        #setup view

        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(20, 30, 101, 41))
        self.textEdit.setObjectName("textEdit")

        #setup menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCopy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #pyqtgraph
        self.plot_widget = pg.PlotWidget()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Monitoring Sensor"))
 
        self.groupBox.setTitle(_translate("MainWindow", "Kecepatan"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Arus"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Posisi"))

        self.radioButton.setText(_translate("MainWindow", "Normal"))
        self.radioButton_2.setText(_translate("MainWindow", "Fault"))
        self.radioButton_3.setText(_translate("MainWindow", "Normal"))
        self.radioButton_4.setText(_translate("MainWindow", "Fault"))
        self.radioButton_5.setText(_translate("MainWindow", "Normal"))
        self.radioButton_6.setText(_translate("MainWindow", "Fault"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))

    def data(self):
        self.sensor = pd.read_excel("C:\Users\BagasPC\Desktop\random.xlsx")
        self.xval = self.sensor['time'].tolist()
        self.yval = self.sensor['arus'].tolist()
        self.yval2 = self.sensor['kecepatan'].tolist()
        self.yval3 = self.sensor['posisi'].tolist()
        # self.graphicsView_3.plot(self.xval,self.yval)
        style.use('fivethirtyeight')
    
    def update(self):
        idx=0
        window_size=50
        while True:
            # for i in range(len(self.xval)):
            #     self.xval[i] += 1            
            #for i in range(len(self.yval)):
            #self.yval[i] = self.yval[i]  #np.sin(self.xval[i]) 
            self.graphicsView_3.setXRange(self.xval[idx], self.xval[idx+window_size])
            self.graphicsView_2.setXRange(self.xval[idx], self.xval[idx+window_size])
            self.graphicsView.setXRange(self.xval[idx], self.xval[idx+window_size])
            self.graphicsView_3.plot(self.xval[idx:idx+window_size],self.yval[idx:idx+window_size],clear=True)
            self.graphicsView_2.plot(self.xval[idx:idx+window_size],self.yval2[idx:idx+window_size],clear=True)
            self.graphicsView.plot(self.xval[idx:idx+window_size],self.yval3[idx:idx+window_size],clear=True)
            time.sleep(1)
            idx += 1
            #self.textEdit.setText(str(self.yval[-1]))


    def startThread(self):
        #elf.textEdit.setText(str(self.yval[-1]))
        thr = threading.Thread(target=self.update)
        thr.start()
 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.data()
    ui.startThread()
    MainWindow.show()
    sys.exit(app.exec_())
