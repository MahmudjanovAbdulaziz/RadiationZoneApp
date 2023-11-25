from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_extra_calls(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(545, 415)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 521, 391))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 260, 31))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.call_MCHS = QtWidgets.QPushButton(self.widget)
        self.call_MCHS.setGeometry(QtCore.QRect(21, 50, 250, 21))
        self.call_MCHS.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.call_MCHS.setIcon(icon)
        self.call_MCHS.setObjectName("call_MCHS")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 150, 31))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.call_MCHS_2 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_2.setGeometry(QtCore.QRect(280, 50, 220, 21))
        self.call_MCHS_2.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_2.setIcon(icon)
        self.call_MCHS_2.setObjectName("call_MCHS_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(79, 79, 140, 31))
        self.label_4.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_4.setObjectName("label_4")
        self.call_MCHS_3 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_3.setGeometry(QtCore.QRect(20, 120, 250, 21))
        self.call_MCHS_3.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_3.setIcon(icon)
        self.call_MCHS_3.setObjectName("call_MCHS_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(319, 79, 150, 31))
        self.label_5.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_5.setObjectName("label_5")
        self.call_MCHS_4 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_4.setGeometry(QtCore.QRect(280, 120, 220, 21))
        self.call_MCHS_4.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_4.setIcon(icon)
        self.call_MCHS_4.setObjectName("call_MCHS_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(30, 154, 460, 40))
        self.label_6.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_6.setObjectName("label_6")
        self.call_MCHS_5 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_5.setGeometry(QtCore.QRect(20, 208, 480, 21))
        self.call_MCHS_5.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_5.setIcon(icon)
        self.call_MCHS_5.setObjectName("call_MCHS_5")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(70, 237, 390, 30))
        self.label_7.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_7.setObjectName("label_7")
        self.call_MCHS_6 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_6.setGeometry(QtCore.QRect(20, 274, 480, 21))
        self.call_MCHS_6.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_6.setIcon(icon)
        self.call_MCHS_6.setObjectName("call_MCHS_6")
        self.call_MCHS_7 = QtWidgets.QPushButton(self.widget)
        self.call_MCHS_7.setGeometry(QtCore.QRect(20, 350, 480, 21))
        self.call_MCHS_7.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: none;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 20);\n"
"}\n"
"QPushButton::hover{\n"
"font: italic 12pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton::pressed{\n"
"font: italic 13pt \"Arial\";\n"
"background-color: rgba(33, 255, 241, 20);\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}")
        self.call_MCHS_7.setIcon(icon)
        self.call_MCHS_7.setObjectName("call_MCHS_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(40, 318, 480, 30))
        self.label_8.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.call_MCHS.clicked.connect(self.call101)
        self.call_MCHS_2.clicked.connect(self.call102)
        self.call_MCHS_3.clicked.connect(self.call103)
        self.call_MCHS_4.clicked.connect(self.call104)
        self.call_MCHS_5.clicked.connect(self.call112)
        self.call_MCHS_6.clicked.connect(self.call122)
        self.call_MCHS_7.clicked.connect(self.call191)




    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Министерства внутренних дел:"))
        self.call_MCHS.setText(_translate("Dialog", "Открыть 101"))
        self.label_3.setText(_translate("Dialog", "Служба спасения:"))
        self.call_MCHS_2.setText(_translate("Dialog", "Открыть 102"))
        self.label_4.setText(_translate("Dialog", "Скорая помощь:"))
        self.call_MCHS_3.setText(_translate("Dialog", "Открыть 103"))
        self.label_5.setText(_translate("Dialog", "Пожарная служба:"))
        self.call_MCHS_4.setText(_translate("Dialog", "Открыть 104"))
        self.label_6.setText(_translate("Dialog", "Единый номер экстренных служб (включает МВД, Службу \n"
"             спасения, скорую помощь и пожарную службу):"))
        self.call_MCHS_5.setText(_translate("Dialog", "Открыть 112"))
        self.label_7.setText(_translate("Dialog", "Служба безопасности дорожного движения (ГАИ)"))
        self.call_MCHS_6.setText(_translate("Dialog", "Открыть 122"))
        self.call_MCHS_7.setText(_translate("Dialog", "Открыть 191"))
        self.label_8.setText(_translate("Dialog", "Государственная служба национальной безопасности (ГСНБ)"))

    def call101(self):
        url = "https://web.whatsapp.com/send?phone=101"
        webbrowser.open_new_tab(url)

    def call102(self):
        url = "https://web.whatsapp.com/send?phone=102"
        webbrowser.open_new_tab(url)

    def call103(self):
        url = "https://web.whatsapp.com/send?phone=103"
        webbrowser.open_new_tab(url)

    def call104(self):
        url = "https://web.whatsapp.com/send?phone=104"
        webbrowser.open_new_tab(url)

    def call112(self):
        url = "https://web.whatsapp.com/send?phone=112"
        webbrowser.open_new_tab(url)

    def call122(self):
        url = "https://web.whatsapp.com/send?phone=122"
        webbrowser.open_new_tab(url)

    def call191(self):
        url = "https://web.whatsapp.com/send?phone=191"
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_extra_calls()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
