import sys
import time
import socket
import hashlib
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from des2 import *
from methods.SettingsPanel import *
from methods.ConnectThreadMonitor import *
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random

login = ''
pas = ''
mail = ''
def Auth():
    app = QtWidgets.QApplication(sys.argv)
    Auth = QtWidgets.QMainWindow()
    ui = AuthWindow()
    ui.setupUi(Auth)
    Auth.show()
    sys.exit(app.exec_())
#Інтерфейс програми і обробник подій всередині нього
class Ui_Registration(QtWidgets.QMainWindow):
    def setupUi(self, Registration):
        Registration.setObjectName("Registration")
        Registration.resize(621, 438)
        self.centralwidget = QtWidgets.QWidget(Registration)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hashedval = ''
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, 0, 831, 31))
        self.frame_3.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"

"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 140, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(220, 80, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Muli ExtraLight")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(210, 300, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 195, 200, 31))
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password) 
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")


        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(210, 250, 200, 31)) 
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setClearButtonEnabled(True)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 360, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")

        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.clicked.connect(lambda: self.back_button(Registration))
        self.pushButton.clicked.connect(lambda: self.save_and_open_window(Registration))
        self.lineEdit_3.returnPressed.connect(lambda: self.save_and_open_window(Registration))
        self.lineEdit_2.returnPressed.connect(lambda: self.save_and_open_window(Registration))
        self.lineEdit_4.returnPressed.connect(lambda: self.save_and_open_window(Registration))
        Registration.setCentralWidget(self.centralwidget)
        self.retranslateUi(Registration)
        QtCore.QMetaObject.connectSlotsByName(Registration)
        Registration.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Registration.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Registration.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        Registration.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton_2.clicked.connect(lambda:self.AuthFunc(Registration))
        self.dragPos = QtCore.QPoint()
        
        def mousePressEvent(event):
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPos = event.globalPos() - Registration.frameGeometry().topLeft()
                event.accept()

        def mouseMoveEvent(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                Registration.move(event.globalPos() - self.dragPos)
                event.accept()

        self.frame_3.mousePressEvent = mousePressEvent
        self.frame_3.mouseMoveEvent = mouseMoveEvent
    
    def retranslateUi(self, Registration):
        _translate = QtCore.QCoreApplication.translate
        Registration.setWindowTitle(_translate("Registration", "Registration"))
        self.pushButton_3.setText(_translate("Registration", "X"))
        self.pushButton_5.setText(_translate("Registration", "_"))
        self.label.setText(_translate("Registration", "Регістрація"))
        self.pushButton.setText(_translate("Registration", "Зареєструватися"))
        self.pushButton_2.setText(_translate("Registration", "У мене є аккаунт"))
        self.lineEdit_2.setPlaceholderText("Введіть логін")
        self.lineEdit_3.setPlaceholderText("Введіть пароль")
        self.lineEdit_4.setPlaceholderText("Введіть пошту")
        self.lineEdit_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
        self.lineEdit_3.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
        self.lineEdit_4.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
    
    def back_button(self, Reg):
        Reg.close()
    
    def save_data(self):
        with open('DataUsers.txt', 'a', encoding="UTF-8") as f1:
            f1.write(f"{self.lineEdit_2.text()},{self.hashedval},{self.lineEdit_4.text()}\n")
            print('1')
    # Функція перевіряє та записує дані в DataUsers.txt, якщо вони були введені правильно тоді програма перекидує
    # користувача на інше вікно де він має підтвердити логін та пароль
    def save_and_open_window(self, Registration):
        # Отримання даних з форми
        login = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        email = self.lineEdit_4.text()
        # Перевірка, чи поля не є пустими
        logins = []
        emails = []
        with open("DataUsers.txt", "r", encoding = "UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                fields = line.strip().split(",")
                logins.append(fields[0])
                emails.append(fields[2])
        if not login or not password or not email:
            QtWidgets.QMessageBox.warning(None, "Помилка", "Будь ласка, заповніть усі поля")
            return
        elif login in logins:
            QMessageBox.warning(None, "Помилка", "Такий логін вже існує")
            return
        elif email in emails:
            QMessageBox.warning(None, "Помилка", "Така електронна пошта вже існує")
            return
        elif not (email.endswith("@gmail.com") or email.endswith("@ukr.net") or email.endswith("@kep.nung.edu.ua")):
            QMessageBox.warning(None, "Помилка", "Неправильний формат вводу пошти, домени @gmail.com @ukr.net @kep.nung.edu.ua")
            return
        
        else:
            # Збереження даних в файл
            self.VerifyFunc(Registration)

    def back_button(self, Reg):
        Reg.close()

    def AuthFunc(self, Registration):#метод який відкриває вікно аутентифікації
        Registration.close()
        self.auth_value=QtWidgets.QMainWindow()
        self.open_authwindow=AuthWindow()
        self.open_authwindow.setupUi(self.auth_value)
        self.auth_value.show()

    def VerifyFunc(self, Registration):
        global login, mail, pas
        login = self.lineEdit_2.text()
        mail = self.lineEdit_4.text()
        pas =  self.hashedval = hashlib.sha256(self.lineEdit_3.text().encode()).hexdigest()
        Registration.close()
        self.auth_value = QtWidgets.QMainWindow()
        self.open_authwindow = Ui_VerifyWindow()
        self.open_authwindow.lineEdit_value = login  # Передача значення з lineEdit
        self.open_authwindow.setupUi(self.auth_value)
        self.auth_value.show()

class Ui_VerifyWindow(QtWidgets.QMainWindow):
    def setupUi(self, VerifyWindow):
        VerifyWindow.setObjectName("VerifyWindow")
        VerifyWindow.resize(461, 185)
        self.centralwidget = QtWidgets.QWidget(VerifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 621, 441))
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-1, 0, 831, 31))
        self.frame_3.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(420, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 40, 601, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(250, 100, 170, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.lineEditVerifyCode = QtWidgets.QLineEdit(self.frame)
        self.lineEditVerifyCode.setGeometry(QtCore.QRect(20, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEditVerifyCode.setFont(font)
        self.lineEditVerifyCode.setStyleSheet("QLineEdit{\n"
                                               "    border-radius: 7px;\n"
                                               "}")
        self.lineEditVerifyCode.setText("")
        self.lineEditVerifyCode.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEditVerifyCode.setPlaceholderText("")
        self.lineEditVerifyCode.setClearButtonEnabled(True)
        self.lineEditVerifyCode.setObjectName("lineEditVerifyCode")
        self.lineEditVerifyCode.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
        VerifyWindow.setCentralWidget(self.centralwidget)

        self.pushButton_3.clicked.connect(lambda: self.back_button(VerifyWindow))
        self.retranslateUi(VerifyWindow)
        QtCore.QMetaObject.connectSlotsByName(VerifyWindow)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        QtCore.QMetaObject.connectSlotsByName(VerifyWindow)
        QtCore.QMetaObject.connectSlotsByName(VerifyWindow)
        VerifyWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        VerifyWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        VerifyWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        VerifyWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.dragPos = QtCore.QPoint()
        @QtCore.pyqtSlot()
        def mousePressEvent(self, event):
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPos = event.globalPos() - self.window().frameGeometry().topLeft()
                event.accept()

        @QtCore.pyqtSlot()
        def mouseMoveEvent(self, event):
            if event.buttons() == QtCore.Qt.LeftButton:
                self.window().move(event.globalPos() - self.dragPos)
                event.accept()


        def send_verification_email(recipient_email, verification_code):
            message = Mail(
                from_email='verifycodeki2001@gmail.com',
                to_emails=recipient_email,
                subject='Verification Code',
                plain_text_content=f'Your verification code is: {verification_code}'
            )

            try:
                sg = SendGridAPIClient(api_key='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')
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(str(e))

            # Usage

        random_number = random.randint(1000000, 9999999)
        verification_code = str(random_number)
        print(mail)
        recipient_email = mail
        send_verification_email(recipient_email, verification_code)
        print(verification_code)
        self.code = verification_code
        self.frame_3.mousePressEvent = mousePressEvent
        self.frame_3.mouseMoveEvent = mouseMoveEvent
        self.pushButton.clicked.connect(lambda: self.check(VerifyWindow))
    
    def retranslateUi(self, VerifyWindow):
        _translate = QtCore.QCoreApplication.translate
        VerifyWindow.setWindowTitle(_translate("VerifyWindow", "VerifyWindow"))
        self.pushButton_3.setText(_translate("VerifyWindow", "X"))
        self.pushButton_5.setText(_translate("VerifyWindow", "_"))
        self.label.setText(_translate("VerifyWindow", "На вашу пошту було надіслано код, введіть його"))
        self.pushButton.setText(_translate("VerifyWindow", "Зареєструватися"))
   
    def check(self, VerifyWindow):
        if self.code == self.lineEditVerifyCode.text():
            with open('DataUsers.txt', 'a', encoding="UTF-8") as f1:
                f1.write(f"{login},{pas},{mail}\n")
            VerifyWindow.close()
            Auth = QtWidgets.QMainWindow()
            ui = AuthWindow()
            ui.setupUi(Auth)
            Auth.show()
            QtWidgets.QMessageBox.information(None, "Інформація", "Обліковий запис успішно створено")
            return
        else:
            print("неправильний код!")
 
    def back_button(self, Reg):
        Reg.close()

class AuthWindow(QtWidgets.QWidget):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.resize(596, 394)
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, -10, 621, 441))
        self.frame.setStyleSheet("QFrame{\n"
"    border-radius: 7px;\n"
"    background-color: #1B1D23;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(-230, 10, 831, 31))
        self.frame_3.setStyleSheet("QFrame{\n"
"    border-bottom-left-radius: 0px;\n"
"    border-bottom-right-radius: 0px;\n"
"    background-color: #2C313C;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setGeometry(QtCore.QRect(790, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setGeometry(QtCore.QRect(750, 0, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border: none;\n"
"    border-top-right-radius: 7px;\n"
"    background-color: #2C313C;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #45494D;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    color: #EA2F4E;\n"
"}")
        self.pushButton_5.setDefault(False)
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setClearButtonEnabled(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(170, 60, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Muli ExtraLight")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(220, 250, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 320, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    color: white;\n"
"    border-radius: 7px;\n"
"    background-color: #595F76;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #50566E;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #434965;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(210, 190, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 7px;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setClearButtonEnabled(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3.clicked.connect(lambda: self.back_button(AuthWindow))
        self.pushButton_2.clicked.connect(lambda:self.RegFunc(AuthWindow))
        self.pushButton.clicked.connect(lambda: self.checkData(AuthWindow))
        self.lineEdit_3.returnPressed.connect(lambda: self.checkData(AuthWindow))
        self.lineEdit_2.returnPressed.connect(lambda: self.checkData(AuthWindow))

        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)
        AuthWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        AuthWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        AuthWindow.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        AuthWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.dragPos = QtCore.QPoint()

        def mousePressEvent(event):
            if event.button() == QtCore.Qt.LeftButton:
                self.dragPos = event.globalPos() - AuthWindow.frameGeometry().topLeft()
                event.accept()

        def mouseMoveEvent(event):
            if event.buttons() == QtCore.Qt.LeftButton:
                AuthWindow.move(event.globalPos() - self.dragPos)
                event.accept()

        self.frame_3.mousePressEvent = mousePressEvent
        self.frame_3.mouseMoveEvent = mouseMoveEvent
        
    
    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "AuthWindow"))
        self.pushButton_3.setText(_translate("AuthWindow", "X"))
        self.pushButton_5.setText(_translate("AuthWindow", "_"))
        self.label.setText(_translate("AuthWindow", "Вхід в систему"))
        self.pushButton.setText(_translate("AuthWindow", "Увійти"))
        self.pushButton_2.setText(_translate("AuthWindow", "У мене немає аккаунта"))
        self.lineEdit_2.setPlaceholderText("Введіть логін")
        self.lineEdit_3.setPlaceholderText("Введіть пароль")
        self.lineEdit_2.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
        self.lineEdit_3.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[A-Za-z0-9!@#$%^&*()_+=\-\\\|}{'\";:.,<>?/~` ]+")))
    
    def back_button(self, AuthWindow):
        AuthWindow.close()

    def RegFunc(self, AuthWindow):
        AuthWindow.close()
        self.reg_value=QtWidgets.QMainWindow()
        self.open_regwindow=Ui_Registration()
        self.open_regwindow.setupUi(self.reg_value)
        self.reg_value.show()

    def checkData(self, AuthWindow):
        logins = []
        passwords = []
        login = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        with open("DataUsers.txt", "r", encoding = "UTF-8") as file:
            lines = file.readlines()
            for line in lines:
                fields = line.strip().split(",")
                logins.append(fields[0])
                passwords.append(fields[1])
        if not login or not password:
            QtWidgets.QMessageBox.warning(None, "Помилка", "Будь ласка, заповніть усі поля")
            return
        hashedval_pass1 = hashlib.sha256(password.encode()).hexdigest()
        if hashedval_pass1 in passwords:
            if login in logins and hashedval_pass1 == passwords[logins.index(login)]:
                QtWidgets.QMessageBox.information(None, "Інформація", f"Ласкаво просимо {login}")
                success_enter=login
                with open('Username.txt','w', encoding="cp1251") as ft:
                    ft.write(success_enter)
                file.close()
                self.open_Main_Window(AuthWindow)
            else:
                QtWidgets.QMessageBox.warning(None, "Помилка", "Неправильний логін або пароль")
                return
        else:
            QtWidgets.QMessageBox.warning(None, "Помилка", "Неправильний логін або пароль")
            return
    
    def open_Main_Window(self, AuthWindow):
        AuthWindow.close()
        client = Client()
        client.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Client(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Дані з конфіга(симетричний ключ отримуємо в відповідь від сервера)
        self.nick = None
        self.ip = None
        self.port = None
        self.smile_type = "Tst"
        self.connect_status = False

        #Об'єкт класу для обробки підключень та сигналів
        self.connect_monitor = message_monitor()
        self.connect_monitor.mysignal.connect(self.signal_handler)

        # відключаєм стандартні рамки програми
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Обробники основних кнопок + кнопок з панелі
        self.ui.pushButton.clicked.connect(self.send_message)
        #self.ui.pushButton_2.clicked.connect(self.connect_to_server)
        self.ui.pushButton_3.clicked.connect(lambda: self.close())
        self.ui.pushButton_4.clicked.connect(lambda: self.ui.listWidget.clear())
        self.ui.pushButton_5.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton_7.clicked.connect(self.setting_panel)

        
        time.sleep(2)
        self.connect_to_server()
    #Рух безрамкового вікна
    def center(self):
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def on_item_click(self,item):
        self.ui.selected_item_text=self.ui.listWidget_2.currentItem().text()
        print(self.ui.selected_item_text)
    
    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
    # Відкрити вікно налаштувань
    def setting_panel(self):
        setting_win = SettingPanel(self, self.connect_monitor.mysignal)
        setting_win.show()
    # Обновленні конфігів клієнту
    def update_config(self):
        """
        Використовується для постійного обновлення значень, без перезапуску програми
        """
        # Якщо конфіг створено
        if os.path.exists(os.path.join("data", "config.json")):
            with open(os.path.join("data", "config.json")) as file:
                data = json.load(file)
                #self.nick = "data['nick']"
                self.ip = data['server_ip']
                self.port = int(data['server_port'])
            f = open('Username.txt', 'r', encoding='UTF-8').read() 
            self.nick=f          
            print("Новий логін=",f)
    # Обробник сигналів з потоку
    def signal_handler(self,value: list):
        if value[0] == "update_config":
            self.update_config()
        elif value[0]=="SERVER_OK":
            self.connect_status = True
            print("succesfully conected")
        else:
            if self.ui.listWidget_2.currentItem().text()=="Ростік" and value[0]=="ROST":
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"Ростіку від {value[1]}:\n{value[-1]}")
                self.ui.listWidget.addItem(item)
                print(value)
            elif self.ui.listWidget_2.currentItem().text()=="Загальний" and value[0] == "ENCRYPT_MESSAGE":
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)

                if value[2] != None:
                    size = QtCore.QSize(45, 45)
                    icon = QtGui.QIcon(os.path.join("icons", f"smile{value[2]}.png"))
                    self.ui.listWidget.setIconSize(size)
                    item.setIcon(icon)
        
                item.setText(f"З Загального{value[1]}:\n{value[-1]}")
                self.ui.listWidget.addItem(item)
                print(value)
            elif self.ui.listWidget_2.currentItem().text()=="Толік" and value[0] =="Tolik":
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"Толіку від {value[1]}:\n{value[-1]}")
                self.ui.listWidget.addItem(item)
                print(value)
            elif self.ui.listWidget_2.currentItem().text()=="Юра" and value[0]=="Yura":
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeft)
                item.setText(f"Юрі від {value[1]}:\n{value[-1]}")
                self.ui.listWidget.addItem(item)
                print(value)
    # Отправить сообщение на сервер
    def send_message(self):
        if self.connect_status:
            message_text = self.ui.lineEdit.text()
            smile_num = self.smile_type
            if self.ui.listWidget_2.currentItem().text()=="Ростік":
                print(self.ui.listWidget_2.currentItem().text(),"2222")
                payload=['ROST',self.nick,smile_num,message_text.encode()]
                print(payload)
                self.connect_monitor.send_encrypt(payload)
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignRight)
                item.setText(f"{self.nick} (ВИ)- Ростіку:\n{message_text}")
                size = QtCore.QSize(45, 45)
                self.ui.listWidget.addItem(item)
            elif self.ui.listWidget_2.currentItem().text()=="Юра":
                print(self.ui.listWidget_2.currentItem().text(),"2222")
                payload=['Yura',self.nick,smile_num,message_text.encode()]
                print(payload)
                self.connect_monitor.send_encrypt(payload)
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignRight)
                item.setText(f"{self.nick} (ВИ)- Юрі:\n{message_text}")
                size = QtCore.QSize(45, 45)
                self.ui.listWidget.addItem(item)
            elif self.ui.listWidget_2.currentItem().text()=="Толік":
                print(self.ui.listWidget_2.currentItem().text(),"2222")
                payload=['Tolik',self.nick,smile_num,message_text.encode()]
                print(payload)
                self.connect_monitor.send_encrypt(payload)
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignRight)
                item.setText(f"{self.nick} (ВИ)- Толіку:\n{message_text}")
                size = QtCore.QSize(45, 45)
                self.ui.listWidget.addItem(item)
            #Якщо поле з текстом не пусте, шифруємо повідомлення та передаємо серверу
            elif len(message_text) > 0:
                payload = ['ENCRYPT_MESSAGE', self.nick, smile_num, message_text.encode()]
                print(payload)
                self.connect_monitor.send_encrypt(payload)

                # Додаємо своє повідомлення в ListWidget
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignRight)
                size = QtCore.QSize(45, 45)

                if smile_num != None:
                    icon = QtGui.QIcon(os.path.join("icons", f"smile{smile_num}.png"))
                    self.ui.listWidget.setIconSize(size)
                    item.setIcon(icon)
                item.setText(f"{self.nick} (ВИ):\n{message_text}")
                self.ui.listWidget.addItem(item)

        else:
            message = "Перевірте з'єднання з сервером"
            QtWidgets.QMessageBox.about(self, "Повідомлення", message)
    # Підключаємося до загального серверу
    def connect_to_server(self):
        self.update_config()    #Поновлюємо дані користувачі

        if self.nick != None:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.ip, self.port))

                #Запускаємо моніторинг вхідних повідомлень
                self.connect_monitor.server_socket = self.client
                self.connect_monitor.start()

                #Блокуємо кнопки
                self.btn_locker(self.ui.pushButton_2, True)
                self.btn_locker(self.ui.pushButton_7, True)

            except Exception as err:
                message = "Помилка з'єднання з сервером.\nПеревірте правильність ввводу даних"
                QtWidgets.QMessageBox.about(self, "Повідомлення", message)
        else:   #Якщо користувач не заповнив дані
            message = "Для початку заповните дані в вкладці 'Настройки'"
            QtWidgets.QMessageBox.about(self, "Повідомлення", message)
    # Блокувач кнопок
    def btn_locker(self, btn: object, lock_status: bool) -> None:
        default_style = """
        QPushButton{
            color: white;
            border-radius: 7px;
            background-color: #595F76;
        }
        QPushButton:hover{
            background-color: #50566E;
        }      
        QPushButton:pressed{
            background-color: #434965;
        }
        """

        lock_style = """
        color: #9EA2AB;
        border-radius: 7px;
        background-color: #2C313C;
        """

        if lock_style:
            btn.setDisabled(True)
            btn.setStyleSheet(lock_style)
        else:
            btn.setDisabled(False)
            btn.setStyleSheet(default_style)
    #Обробник події на вихід з клієнту
    def closeEvent(self, value: QtGui.QCloseEvent) -> None:
        try:
            payload = ['EXIT', f'{self.nick}', 'вийшов з чату!'.encode()]
            self.connect_monitor.send_encrypt(payload) 
            #self.close()
            time.sleep(3) 
            #self.client.close()
            #self.close()
        except Exception as err:
            print(err)

Auth()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Client()
    myapp.show()
    sys.exit(app.exec_())
