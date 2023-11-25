from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QCheckBox, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import sqlite3

from PyQt5.QtWidgets import QLineEdit


class Ui_Dialog8(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(719, 706)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 30, 681, 651))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(290, 30, 61, 20))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 14pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 291, 20))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.Name_Issledovatel = QtWidgets.QLineEdit(self.frame)
        self.Name_Issledovatel.setGeometry(QtCore.QRect(50, 130, 571, 20))
        self.Name_Issledovatel.setStyleSheet("QLineEdit {\n"
"    color: rgb(221, 155, 1); \n"
"    font: italic 14pt \"Arial\";\n"
"    border-radius: 5px;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: rgb(139, 69, 19);\n"
"}\n"
"\n"
"\n"
"")
        self.Name_Issledovatel.setPlaceholderText("")
        self.Name_Issledovatel.setObjectName("Name_Issledovatel")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(210, 180, 231, 20))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(250, 280, 141, 20))
        self.label_4.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(50, 340, 571, 20))
        self.password.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255, 30);\n"
"    font: italic 14pt \"Arial\";\n"
"    color: rgb(255, 29, 206);\n"
"}\n"
"QLineEdit::hover{\n"
"    background-color: rgb(255, 255, 255, 50);\n"
"}")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setPlaceholderText("")
        self.password.setObjectName("password")
        self.Id_ = QtWidgets.QLineEdit(self.frame)
        self.Id_.setGeometry(QtCore.QRect(50, 230, 571, 20))
        self.Id_.setMouseTracking(True)
        self.Id_.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(255, 255, 255, 30);\n"
"    font: italic 14pt \"Arial\";\n"
"    color: rgb(255, 29, 206);\n"
"}\n"
"QLineEdit::hover{\n"
"    background-color: rgb(255, 255, 255, 50);\n"
"}")
        self.Id_.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.Id_.setInputMask("")
        self.Id_.setPlaceholderText("")
        self.Id_.setObjectName("Id")
        self.show_password_btn = QtWidgets.QCheckBox(self.frame)
        self.show_password_btn.setGeometry(QtCore.QRect(460, 380, 161, 17))
        self.show_password_btn.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 11pt \"Arial\";\n"
"border: none;")
        self.show_password_btn.setObjectName("show_password_btn")
        self.show_password_text = QtWidgets.QLabel(self.frame)
        self.show_password_text.setGeometry(QtCore.QRect(50, 380, 401, 20))
        self.show_password_text.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.show_password_text.setText("")
        self.show_password_text.setObjectName("show_password_text")
        self.sign_in = QtWidgets.QPushButton(self.frame)
        self.sign_in.setGeometry(QtCore.QRect(380, 430, 241, 21))
        self.sign_in.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: 1px solid  rgba(255, 255, 255, 30);\n"
"font: italic 11pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"border: 1px solid  rgba(255, 255, 255, 40);\n"
"background-color: rgba(255, 255, 255, 30);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QPushButton::pressed{\n"
"border: 1px solid  rgba(255, 255, 255, 50);\n"
"background-color: rgba(120, 255, 251, 40);\n"
"font: italic 13pt \"Arial\";\n"
"}")
        self.sign_in.setObjectName("sign_in")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 590, 301, 16))
        self.label_6.setStyleSheet("QLabel {\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 10pt \"Arial\";\n"
"border: none;\n"
"}\n"
"QLabel::hover {\n"
"    color: rgb(0, 255, 255);\n"
"    text-decoration: underline;\n"
"    cursor: pointer;\n"
"}")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(310, 590, 361, 16))
        self.label_7.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 10pt \"Arial\";\n"
"border: none;\n"
"color: rgb(0, 196, 255);\n"
"text-decoration: underline;\n"
"\n"
"}\n"
"")
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(10, 610, 351, 16))
        self.label_8.setStyleSheet("QLabel {\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 10pt \"Arial\";\n"
"border: none;\n"
"}\n"
"QLabel::hover {\n"
"    color: rgb(0, 255, 255);\n"
"    text-decoration: underline;\n"
"    cursor: pointer;\n"
"}")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(370, 610, 351, 16))
        self.label_9.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 10pt \"Arial\";\n"
"border: none;\n"
"color: rgb(0, 255, 255);\n"
"text-decoration: underline;")
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.sign_in.clicked.connect(self.SignIn)
        self.show_password_btn.stateChanged.connect(self.show_password)
        self.Name_Issledovatel

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign In"))
        self.label.setText(_translate("Dialog", "Вход:"))
        self.label_2.setText(_translate("Dialog", "Введите ваше имя исследователя:"))
        self.label_3.setText(_translate("Dialog", "Введите ID (необязательно):"))
        self.label_4.setText(_translate("Dialog", "Введите пароль:"))
        self.show_password_btn.setText(_translate("Dialog", "Показать пароль:"))
        self.sign_in.setText(_translate("Dialog", "Войти..."))
        self.label_6.setText(_translate("Dialog", "Если вы яаляетесь исследователем и хотите "))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://exampleLink.com\"><span style=\" text-decoration: underline; color:#0000ff;\">получить доступ к спец возможностям исследователя</span></a></p></body></html>"))
        self.label_8.setText(_translate("Dialog", "нажмите на этот текст и перейдите на официальный "))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://example2href.com\"><span style=\" text-decoration: underline; color:#0000ff;\">сайт Radiation Zone и зарегестрируйтесь. </span></a></p></body></html>"))

    def SignIn(self):
        self.count = 0
        self.researcher = self.Name_Issledovatel.text()
        conn1 = sqlite3.connect('SignInDataBases/users.db')
        c1 = conn1.cursor()
        c1.execute("SELECT username FROM users")
        result1 = c1.fetchone()



        conn1.close()
        self.id = self.Id_.text()
        conn2 = sqlite3.connect('SignInDataBases/Id.db')
        c2 = conn2.cursor()
        c2.execute("SELECT password FROM users")
        result2 = c2.fetchone()





        conn2.close()
        self.passwords = self.password.text()
        conn3 = sqlite3.connect('SignInDataBases/password.db')
        c3 = conn3.cursor()
        c3.execute("SELECT password FROM users")
        result3 = c3.fetchone()
        if result1 and result1[0] == self.researcher:
            self.count += 1
        if result3 and result3[0] == self.passwords:
            self.count += 1
        elif result2 and result2[0] == self.id:
            self.count += 1
        # print(self.count)
        conn3.close()

    def show_password(self, state):
        if state == Qt.Checked:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = QtWidgets.QDialog()
#     ui = Ui_Dialog8()
#     ui.setupUi(Dialog)
#     Dialog.show()
#     sys.exit(app.exec_())
