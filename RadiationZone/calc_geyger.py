from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_geyger(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 686)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 460, 661))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.inp_line_1 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_1.setGeometry(QtCore.QRect(20, 90, 420, 20))
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
        self.text_lab_1.setGeometry(QtCore.QRect(50, 50, 360, 21))
        self.text_lab_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_1.setObjectName("text_lab_1")
        self.inp_line_2 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_2.setGeometry(QtCore.QRect(20, 170, 420, 20))
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
        self.inp_line_3.setGeometry(QtCore.QRect(20, 250, 420, 20))
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
        self.inp_line_4.setGeometry(QtCore.QRect(20, 330, 420, 20))
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
        self.inp_line_5 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_5.setGeometry(QtCore.QRect(20, 410, 420, 20))
        self.inp_line_5.setStyleSheet("QLineEdit{\n"
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
        self.inp_line_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_5.setClearButtonEnabled(True)
        self.inp_line_5.setObjectName("inp_line_5")
        self.btn_give_otv = QtWidgets.QPushButton(self.widget)
        self.btn_give_otv.setGeometry(QtCore.QRect(220, 540, 220, 30))
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
        self.text_lab_3.setGeometry(QtCore.QRect(30, 210, 410, 21))
        self.text_lab_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_3.setObjectName("text_lab_3")
        self.text_lab_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_4.setGeometry(QtCore.QRect(32, 290, 400, 21))
        self.text_lab_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_4.setObjectName("text_lab_4")
        self.text_lab_5 = QtWidgets.QLabel(self.widget)
        self.text_lab_5.setGeometry(QtCore.QRect(40, 370, 370, 21))
        self.text_lab_5.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_5.setObjectName("text_lab_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 617, 61, 20))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.label_6.setObjectName("label_6")
        self.trees_live_4 = QtWidgets.QLabel(self.widget)
        self.trees_live_4.setGeometry(QtCore.QRect(70, 617, 160, 20))
        self.trees_live_4.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_4.setObjectName("trees_live_4")
        self.text_calc = QtWidgets.QLabel(self.widget)
        self.text_calc.setGeometry(QtCore.QRect(150, 16, 140, 20))
        self.text_calc.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_calc.setObjectName("text_calc")
        self.text_lab_7 = QtWidgets.QLabel(self.widget)
        self.text_lab_7.setGeometry(QtCore.QRect(110, 450, 240, 21))
        self.text_lab_7.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_7.setObjectName("text_lab_7")
        self.inp_line_6 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_6.setGeometry(QtCore.QRect(20, 490, 420, 20))
        self.inp_line_6.setStyleSheet("QLineEdit{\n"
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
        self.inp_line_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_6.setClearButtonEnabled(True)
        self.inp_line_6.setObjectName("inp_line_6")
        self.lab_otv_1 = QtWidgets.QLabel(self.widget)
        self.lab_otv_1.setGeometry(QtCore.QRect(230, 620, 90, 20))
        self.lab_otv_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_1.setText("")
        self.lab_otv_1.setObjectName("lab_otv_1")
        self.lab_otv_2 = QtWidgets.QLabel(self.widget)
        self.lab_otv_2.setGeometry(QtCore.QRect(330, 620, 90, 21))
        self.lab_otv_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_2.setText("")
        self.lab_otv_2.setObjectName("lab_otv_2")
        self.img_png = QtWidgets.QLabel(self.widget)
        self.img_png.setGeometry(QtCore.QRect(390, 610, 71, 40))
        self.img_png.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.img_png.setText("")
        self.text_lab_2 = QtWidgets.QLabel(Dialog)
        self.text_lab_2.setGeometry(QtCore.QRect(40, 140, 410, 21))
        self.text_lab_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_2.setObjectName("text_lab_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.inp_line_6.hide()

        self.btn_give_otv.clicked.connect(self.calculate)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text_lab_1.setText(_translate("Dialog", "Эквивалентная доза в радиации (в Сивертах):"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.text_lab_3.setText(_translate("Dialog", "Коэффициент, учитывающий мощность счетчика:"))
        self.text_lab_4.setText(_translate("Dialog", "Количество импульсов, зарег. за время измерения:"))
        self.text_lab_5.setText(_translate("Dialog", "Время измерения (в секундах):"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.trees_live_4.setText(_translate("Dialog", "Радиация равняется:"))
        self.text_calc.setText(_translate("Dialog", "Счетчик Гейгера"))
        # self.text_lab_7.setText(_translate("Dialog", "Время измерения (в секундах):"))
        self.text_lab_2.setText(_translate("Dialog", "Коэффициент, зависящий от типа излучения (Р/ч):"))

    def calculate(self):
        c = float(self.inp_line_1.text())
        k = float(self.inp_line_2.text())
        p = float(self.inp_line_3.text())
        b = float(self.inp_line_4.text())
        t = float(self.inp_line_5.text())

        D = c / k * (p - b) / t
        self.lab_otv_1.setText(str(D))
        self.lab_otv_2.setText('Сиверт')
        if D < 1:
            self.img_png.setPixmap(QtGui.QPixmap("Images\зеленный.png"))
        elif D > 1 and D < 2:
            self.img_png.setPixmap(QtGui.QPixmap("Images\желтый.png"))
        else:
            self.img_png.setPixmap(QtGui.QPixmap("Images\красный.png"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_geyger()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
