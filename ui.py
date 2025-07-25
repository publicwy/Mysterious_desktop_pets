# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(295, 140)
        MainWindow.setStyleSheet("background-color: rgb(242, 226, 213);\n"
"font: 125 10pt \"微软雅黑\";")
        self.centralwidget_ = QtWidgets.QWidget(MainWindow)
        self.centralwidget_.setObjectName("centralwidget_")
        self.lay1 = QtWidgets.QHBoxLayout()
        self.lay1.setContentsMargins(0, 0, 0, 0)
        self.lay1.setSpacing(0)
        self.centralwidget = QtWidgets.QWidget()
        self.lay1.addWidget(self.centralwidget)
        self.centralwidget_.setLayout(self.lay1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 111))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Packages/priv/pic.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.cpu = QtWidgets.QLabel(self.centralwidget)
        self.cpu.setGeometry(QtCore.QRect(160, 30, 131, 21))
        self.cpu.setStyleSheet("")
        self.cpu.setObjectName("cpu")
        self.mem = QtWidgets.QLabel(self.centralwidget)
        self.mem.setGeometry(QtCore.QRect(160, 50, 131, 21))
        self.mem.setStyleSheet("")
        self.mem.setObjectName("mem")
        self.network = QtWidgets.QLabel(self.centralwidget)
        self.network.setGeometry(QtCore.QRect(160, 70, 141, 41))
        self.network.setObjectName("network")
        self.disk = QtWidgets.QLabel(self.centralwidget)
        self.disk.setGeometry(QtCore.QRect(160, 110, 141, 21))
        self.disk.setObjectName("disk")
        self.cpu_icon = QtWidgets.QLabel(self.centralwidget)
        self.cpu_icon.setGeometry(QtCore.QRect(130, 30, 21, 21))
        self.cpu_icon.setText("")
        self.cpu_icon.setPixmap(QtGui.QPixmap("Packages/priv/cpu.png"))
        self.cpu_icon.setScaledContents(True)
        self.cpu_icon.setObjectName("cpu_icon")
        self.mem_icon = QtWidgets.QLabel(self.centralwidget)
        self.mem_icon.setGeometry(QtCore.QRect(130, 50, 21, 21))
        self.mem_icon.setText("")
        self.mem_icon.setPixmap(QtGui.QPixmap("Packages/priv/memory.png"))
        self.mem_icon.setScaledContents(True)
        self.mem_icon.setObjectName("mem_icon")
        self.network_icon = QtWidgets.QLabel(self.centralwidget)
        self.network_icon.setGeometry(QtCore.QRect(130, 80, 21, 21))
        self.network_icon.setText("")
        self.network_icon.setPixmap(QtGui.QPixmap("Packages/priv/network.png"))
        self.network_icon.setScaledContents(True)
        self.network_icon.setObjectName("network_icon")
        self.disk_icon = QtWidgets.QLabel(self.centralwidget)
        self.disk_icon.setGeometry(QtCore.QRect(130, 110, 21, 21))
        self.disk_icon.setText("")
        self.disk_icon.setPixmap(QtGui.QPixmap("Packages/priv/disk.png"))
        self.disk_icon.setScaledContents(True)
        self.disk_icon.setObjectName("disk_icon")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 10, 161, 16))
        self.label_2.setStyleSheet("font: 12pt \"微软雅黑\";\n"
"font-style: bold")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget_)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cpu.setText(_translate("MainWindow", "cpu占用率："))
        self.mem.setText(_translate("MainWindow", "内存使用率："))
        self.network.setText(_translate("MainWindow", "上行：999Mbps/s\n"
"下行：999Mbps/s"))
        self.disk.setText(_translate("MainWindow", "磁盘使用量：00%"))
        self.label_2.setText(_translate("MainWindow", "2000-01-01 00:00:00"))
