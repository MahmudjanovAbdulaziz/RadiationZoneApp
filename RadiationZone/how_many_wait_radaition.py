from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_how_many_wait(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 645)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 460, 620))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.inp_line_1 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_1.setGeometry(QtCore.QRect(20, 130, 420, 20))
        self.inp_line_1.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"selection-color: rgb(220, 0, 110);\n"
"alternate-background-color: rgb(220, 0, 110);\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QLineEdit::cursor{\n"
"color: rgb(255, 248, 20);\n"
"}\n"
"QPushButton#myButton {\n"
"    border: none; /* удалить рамку кнопки */\n"
"    background-image: url(Images/image.png); /* путь к изображению */\n"
"    background-repeat: no-repeat; /* не повторять фон */\n"
"    background-position: center; /* центрировать изображение */\n"
"}")
        self.inp_line_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_1.setClearButtonEnabled(True)
        self.inp_line_1.setObjectName("inp_line_1")
        self.text_lab_1 = QtWidgets.QLabel(self.widget)
        self.text_lab_1.setGeometry(QtCore.QRect(61, 90, 330, 21))
        self.text_lab_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_1.setText("")
        self.text_lab_1.setObjectName("text_lab_1")
        self.inp_line_2 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_2.setGeometry(QtCore.QRect(20, 210, 420, 20))
        self.inp_line_2.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"selection-color: rgb(220, 0, 110);\n"
"alternate-background-color: rgb(220, 0, 110);\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QLineEdit::cursor{\n"
"color: rgb(255, 248, 20);\n"
"}\n"
"QPushButton#myButton {\n"
"    border: none; /* удалить рамку кнопки */\n"
"    background-image: url(Images/image.png); /* путь к изображению */\n"
"    background-repeat: no-repeat; /* не повторять фон */\n"
"    background-position: center; /* центрировать изображение */\n"
"}")
        self.inp_line_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_2.setClearButtonEnabled(True)
        self.inp_line_2.setObjectName("inp_line_2")
        self.inp_line_3 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_3.setGeometry(QtCore.QRect(20, 290, 420, 20))
        self.inp_line_3.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"selection-color: rgb(220, 0, 110);\n"
"alternate-background-color: rgb(220, 0, 110);\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QLineEdit::cursor{\n"
"color: rgb(255, 248, 20);\n"
"}\n"
"QPushButton#myButton {\n"
"    border: none; /* удалить рамку кнопки */\n"
"    background-image: url(Images/image.png); /* путь к изображению */\n"
"    background-repeat: no-repeat; /* не повторять фон */\n"
"    background-position: center; /* центрировать изображение */\n"
"}")
        self.inp_line_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_3.setClearButtonEnabled(True)
        self.inp_line_3.setObjectName("inp_line_3")
        self.inp_line_4 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_4.setGeometry(QtCore.QRect(20, 370, 420, 20))
        self.inp_line_4.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"selection-color: rgb(220, 0, 110);\n"
"alternate-background-color: rgb(220, 0, 110);\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QLineEdit::cursor{\n"
"color: rgb(255, 248, 20);\n"
"}\n"
"QPushButton#myButton {\n"
"    border: none; /* удалить рамку кнопки */\n"
"    background-image: url(Images/image.png); /* путь к изображению */\n"
"    background-repeat: no-repeat; /* не повторять фон */\n"
"    background-position: center; /* центрировать изображение */\n"
"}")
        self.inp_line_4.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_4.setClearButtonEnabled(True)
        self.inp_line_4.setObjectName("inp_line_4")
        self.btn_give_otv = QtWidgets.QPushButton(self.widget)
        self.btn_give_otv.setGeometry(QtCore.QRect(220, 430, 220, 30))
        self.btn_give_otv.setStyleSheet("QPushButton{\n"
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
        self.btn_give_otv.setObjectName("btn_give_otv")
        self.text_lab_3 = QtWidgets.QLabel(self.widget)
        self.text_lab_3.setGeometry(QtCore.QRect(60, 250, 330, 21))
        self.text_lab_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_3.setText("")
        self.text_lab_3.setObjectName("text_lab_3")
        self.text_lab_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_4.setGeometry(QtCore.QRect(35, 330, 390, 21))
        self.text_lab_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_4.setText("")
        self.text_lab_4.setObjectName("text_lab_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(32, 540, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.label_6.setObjectName("label_6")
        self.trees_live_2 = QtWidgets.QLabel(self.widget)
        self.trees_live_2.setGeometry(QtCore.QRect(90, 540, 310, 21))
        self.trees_live_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_2.setObjectName("trees_live_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(99, 28, 330, 40))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.lab_otv_2 = QtWidgets.QLabel(self.widget)
        self.lab_otv_2.setGeometry(QtCore.QRect(120, 570, 50, 20))
        self.lab_otv_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_2.setObjectName("lab_otv_2")
        self.lab_otv_1 = QtWidgets.QLabel(self.widget)
        self.lab_otv_1.setGeometry(QtCore.QRect(40, 570, 71, 20))
        self.lab_otv_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_1.setText("")
        self.lab_otv_1.setObjectName("lab_otv_1")
        self.text_lab_2 = QtWidgets.QLabel(Dialog)
        self.text_lab_2.setGeometry(QtCore.QRect(70, 180, 330, 21))
        self.text_lab_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_2.setText("")
        self.text_lab_2.setObjectName("text_lab_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.text_lab_1.setText('Доза радиации, измеряемая в (R)')
        self.text_lab_2.setText('Коэффициент экспозиционной дозы')
        self.text_lab_3.setText('Дозовая скорость, измеряемая в (R/мин)')
        self.text_lab_4.setText('Интенсивность излучения, измеряемая в (R/час)')
        self.lab_otv_2.setText('(сек)')



        self.btn_give_otv.clicked.connect(self.calk)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.trees_live_2.setText(_translate("Dialog", "Для постройки укрытия вам понадабится"))
        self.label_2.setText(_translate("Dialog", "Расчет времени в котором человек \n"
"может находится в зоне очуждения!"))
        self.lab_otv_2.setText(_translate("Dialog", "часов"))


    def calk(self):
        D = float(self.inp_line_1.text())
        K = float(self.inp_line_2.text())
        R = float(self.inp_line_3.text())
        I = float(self.inp_line_3.text())

        otv = (D * K) / (R * I)
        self.lab_otv_1.setText(str(otv))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_how_many_wait()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
