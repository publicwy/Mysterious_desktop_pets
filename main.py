import copy
import os
import time
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5 import QtCore
import ui
import psutil

class PercentThread(QtCore.QThread):
    percent = QtCore.pyqtSignal(str)
    def run(self):
        t = time.time()
        while 1:
            count=os.cpu_count()
            usages = [(psutil.cpu_percent(0.02), time.sleep(0.01))[0] for i in range(count)]
            self.percent.emit(f"cpu占用率：{int(sum(usages) // count)}%")

class NetWorkIO(QtCore.QThread):
    load = QtCore.pyqtSignal(str, str)
    def run(self):
        while 1:
            io_old = psutil.net_io_counters()
            upload_old = io_old.packets_sent
            download_old = io_old.packets_recv
            time.sleep(1.5)
            io_new = psutil.net_io_counters()
            upload_new = io_new.packets_sent
            download_new = io_new.packets_recv
            self.load.emit(f"上行：{self.formatBytes(upload_new - upload_old)} Mbps",
                           f"下行：{self.formatBytes(download_new - download_old)} Mbps")

    def formatBytes(self, byte):
        return f"{byte/1024*8:.2f}"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.actions_list = []
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.centralwidget_.setStyleSheet("border-radius: 10px;")
        self.trayIcon = QSystemTrayIcon()
        self.trayIcon.show()
        self.loadStyle()
        self.cpu_percent = PercentThread()
        self.cpu_percent.percent.connect(lambda per: self.ui.cpu.setText(per))
        self.cpu_percent.start()
        self.network = NetWorkIO()
        self.network.load.connect(lambda up, down: self.ui.network.setText(up + "\n" + down))
        self.network.start()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.reload)
        self.timer.start()

    def reload(self):
        self.ui.mem.setText(f"内存使用率：{int(psutil.virtual_memory().percent)}%")
        self.ui.disk.setText(f"磁盘使用率：{psutil.disk_usage('/').percent}%")
        self.ui.label_2.setText(QtCore.QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss"))

    def contextMenuEvent(self, event):
        self.menu = QMenu()
        self.ChangeTheme = QMenu("改变主题")
        self.ChangeTheme.setIcon(QtGui.QIcon(self.ui.label.pixmap()))
        self.change(self.ChangeTheme)
        self.menu.addMenu(self.ChangeTheme)
        self.menu.show()
        self.menu.popup(QtGui.QCursor.pos())

    def change(self, menu):
        self.actions_list.clear()
        current=self.config["name"]
        for i in os.listdir("Packages"):
            if i == "current.txt": continue
            new_config = self.parseConfig(open(f"Packages\\{i}\\config.prop", encoding="utf8").read())
            self.actions_list.append(QAction(QtGui.QIcon(f"Packages\\{copy.copy(i)}\\pic.png"), copy.copy(new_config["name"])))
            self.actions_list[-1].setCheckable(True)
            if new_config["name"] == current:
                self.actions_list[-1].setChecked(True)
            self.ChangeTheme.addAction(self.actions_list[-1])

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if QtCore.Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)
                QMouseEvent.accept()
        except:
            ...

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False


    def loadStyle(self):
        current = open("Packages\current.txt", encoding="utf-8").read()
        self.config = self.parseConfig(open(f"Packages\\{current}\\config.prop", encoding="utf-8").read())
        self.setStyleSheet("background-color: {};\n"
                                 "font: 125 10pt \"{}\";"
                                 "color: {}".format(self.config["background"], self.config["font-family"], self.config["text-color"]))
        self.ui.label.setPixmap(QtGui.QPixmap(f"Packages/{current}/pic.png"))
        self.ui.cpu_icon.setPixmap(QtGui.QPixmap(f"Packages/{current}/cpu.png"))
        self.ui.mem_icon.setPixmap(QtGui.QPixmap(f"Packages/{current}/memory.png"))
        self.ui.network_icon.setPixmap(QtGui.QPixmap(f"Packages/{current}/network.png"))
        self.ui.disk_icon.setPixmap(QtGui.QPixmap(f"Packages/{current}/disk.png"))
        self.setCursor(QtGui.QCursor(QtGui.QPixmap(f"Packages/{current}/cursor.cur")))
        self.trayIcon.setIcon(QtGui.QIcon(self.ui.label.pixmap()))

    def parseConfig(self, config: str):
        result = {}
        for item in config.split("\n"):
            lst = item.split("=")
            result[lst[0]] = lst[1]
        return result

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()