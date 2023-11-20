import os
import re
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from methods.windows.settings import *

# Вікно з настройками клієнту
class SettingPanel(QtWidgets.QWidget):
    def __init__(self, parent=None, signal=None):
        super().__init__(parent, QtCore.Qt.Window)
        self.setting = Ui_Form()
        self.setting.setupUi(self)
        self.setWindowModality(2)
        #Сигнал для повернення в інтерфейс
        self.signal = signal
        #Відключаємо стандартні рамки програми
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()
        #Обробники кнопок
        self.setting.pushButton_7.clicked.connect(lambda: self.close())
        self.setting.pushButton_6.clicked.connect(self.save_config)
        #Підключаємо налаштування якщо вони вже є
        if os.path.exists(os.path.join("data", "config.json")):
            with open(os.path.join("data", "config.json")) as file:
                data = json.load(file)
                self.setting.lineEdit_4.setText(data['nick'])
                self.setting.lineEdit_2.setText(data['server_ip'])
                self.setting.lineEdit_3.setText(data['server_port'])
    # Рух безрамкового вікна
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
    
    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
    #Зберегти налаштування користувача
    def save_config(self):
        nick = self.setting.lineEdit_4.text()
        server_ip = self.setting.lineEdit_2.text()
        server_port = self.setting.lineEdit_3.text()
        regular_ip = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
        #Обновляємо датчики для того щоб користувач бачив які поля правильні
        self.setting.lineEdit_2.setStyleSheet("border-radius: 7px;")
        self.setting.lineEdit_3.setStyleSheet("border-radius: 7px;")
        self.setting.lineEdit_4.setStyleSheet("border-radius: 7px;")
        #Перевіряємо коректність введення користувача
        if len(nick) >= 3 and len(nick) <= 20:
            if not re.match(regular_ip, self.setting.lineEdit_2.text()) is None:
                if server_port.isdecimal() and int(server_port) <= 65535:

                    #Якщо конфіга не існує
                    if not os.path.exists(os.path.join("data", "config.json")):
                        with open(os.path.join("data", "config.json"), "w") as file:
                            data = {"nick": nick, "server_ip": server_ip, "server_port": server_port}
                            json.dump(data, file, indent=6)

                    #Якщо конфіг існує, перезапис
                    else:
                        with open(os.path.join("data", "config.json"), "w") as file:
                            data = {"nick": nick, "server_ip": server_ip, "server_port": server_port}
                            json.dump(data, file, indent=6)

                    #Закриваємо вікно налаштувань
                    self.close()
                    self.signal.emit(['update_config'])

                else:
                    self.setting.lineEdit_3.setStyleSheet("border: 2px solid red; border-radius: 7px;")
                    self.setting.lineEdit_3.setText("Wrong SERVER_PORT")
            else:
                self.setting.lineEdit_2.setStyleSheet("border: 2px solid red; border-radius: 7px;")
                self.setting.lineEdit_2.setText("Wrong SERVER_IP")
        else:
            self.setting.lineEdit_4.setStyleSheet("border: 2px solid red; border-radius: 7px;")
            self.setting.lineEdit_4.setText("Занадто довге, або занадто коротке ім'я")
