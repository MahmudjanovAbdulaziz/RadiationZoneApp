from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Alpha_beta_gamme(object):
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
        self.combobox = QtWidgets.QComboBox(self.widget)
        self.combobox.setGeometry(QtCore.QRect(20, 10, 420, 21))
        self.combobox.setStyleSheet("QComboBox {\n"
"background-color: rgba(255, 255, 255, 20);\n"
"font: italic 12pt \"Arial\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}\n"
"QComboBox::drop-down {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"background-color: rgba(255, 255, 255, 20);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"font-size: 16px;\n"
"height: 30px;\n"
"    background-color: rgb(166, 227, 255);\n"
"}")
        self.combobox.setObjectName("combobox")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.combobox.addItem("")
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
        self.text_lab_1.setGeometry(QtCore.QRect(61, 50, 330, 21))
        self.text_lab_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_1.setText("")
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
        self.btn_give_otv.setGeometry(QtCore.QRect(220, 450, 220, 30))
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
        self.text_lab_3.setGeometry(QtCore.QRect(60, 210, 330, 21))
        self.text_lab_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_3.setText("")
        self.text_lab_3.setObjectName("text_lab_3")
        self.text_lab_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_4.setGeometry(QtCore.QRect(60, 290, 330, 21))
        self.text_lab_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_4.setText("")
        self.text_lab_4.setObjectName("text_lab_4")
        self.text_lab_5 = QtWidgets.QLabel(self.widget)
        self.text_lab_5.setGeometry(QtCore.QRect(60, 370, 330, 21))
        self.text_lab_5.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_5.setText("")
        self.text_lab_5.setObjectName("text_lab_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 540, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.label_6.setObjectName("label_6")
        self.trees_live_2 = QtWidgets.QLabel(self.widget)
        self.trees_live_2.setGeometry(QtCore.QRect(70, 540, 120, 21))
        self.trees_live_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_2.setObjectName("trees_live_2")
        self.conclusion_1 = QtWidgets.QLabel(self.widget)
        self.conclusion_1.setGeometry(QtCore.QRect(180, 540, 60, 21))
        self.conclusion_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.conclusion_1.setText("")
        self.conclusion_1.setObjectName("conclusion_1")
        self.trees_live_3 = QtWidgets.QLabel(self.widget)
        self.trees_live_3.setGeometry(QtCore.QRect(240, 540, 80, 21))
        self.trees_live_3.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_3.setObjectName("trees_live_3")
        self.lab_otv_2 = QtWidgets.QLabel(self.widget)
        self.lab_otv_2.setGeometry(QtCore.QRect(400, 540, 40, 21))
        self.lab_otv_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_2.setText("")
        self.lab_otv_2.setObjectName("lab_otv_2")
        self.lab_otv_1 = QtWidgets.QLabel(self.widget)
        self.lab_otv_1.setGeometry(QtCore.QRect(320, 540, 71, 20))
        self.lab_otv_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_1.setText("")
        self.lab_otv_1.setObjectName("lab_otv_1")
        self.text_lab_2 = QtWidgets.QLabel(Dialog)
        self.text_lab_2.setGeometry(QtCore.QRect(70, 140, 330, 21))
        self.text_lab_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_2.setText("")
        self.text_lab_2.setObjectName("text_lab_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.combobox.activated.connect(self.change_radiation)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.combobox.setItemText(0, _translate("Dialog", "..."))
        self.combobox.setItemText(1, _translate("Dialog", "-Альфа излучение"))
        self.combobox.setItemText(2, _translate("Dialog", "-Бета излучение"))
        self.combobox.setItemText(3, _translate("Dialog", "-Гамма излучение"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.trees_live_2.setText(_translate("Dialog", "Радиация типа:"))
        self.trees_live_3.setText(_translate("Dialog", "равняется"))

    def change_radiation(self):
        text = self.combobox.currentText()
        if text == '-Альфа излучение':
            self.open_alpha()
        elif text == '-Бета излучение':
            self.open_beta()
        elif text == '-Гамма излучение':
            self.open_gamma()
        else:
            self.text_lab_1.setText('')
            self.text_lab_2.setText('')
            self.text_lab_3.setText('')
            self.text_lab_4.setText('')
            self.text_lab_5.setText('')
            self.conclusion_1.setText('')
            self.lab_otv_1.setText('')
            self.lab_otv_2.setText('')
            self.inp_line_1.show()
            self.inp_line_2.show()
            self.inp_line_3.show()
            self.inp_line_4.show()
            self.inp_line_5.show()

    def open_alpha(self):
        self.text_lab_1.setText('Количество зарегестрированных частиц:')
        self.text_lab_2.setText('Коефицент эффективности детектора:')
        self.text_lab_3.setText('Коефицент поправки на поглащения')
        self.text_lab_4.setText('Время измерения:')
        self.text_lab_5.setText('Коефицент поправки образца')
        self.inp_line_1.show()
        self.inp_line_2.show()
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.inp_line_5.show()

        self.btn_give_otv.clicked.connect(self.calc_alpha)

    def calc_alpha(self):
        I = float(self.inp_line_2.text())
        Eff = float(self.inp_line_1.text())
        ACF = float(self.inp_line_3.text())
        T = float(self.inp_line_4.text())
        SF = float(self.inp_line_5.text())

        A = I / (Eff * ACF * T * SF)
        self.conclusion_1.setText('Альфа')
        self.lab_otv_1.setText(str(A))
        self.lab_otv_2.setText('(бек)')

    def open_beta(self):
        self.text_lab_1.setText('Коэфицент учитывающий вид бета частиц:')
        self.text_lab_2.setText('Фактор учитывающий вид бета частиц')
        self.text_lab_3.setText('Время нахождения в зоне')
        self.text_lab_4.setText('Расстояние между источником и обьектом')
        self.text_lab_5.setText('')
        self.inp_line_5.hide()
        self.inp_line_1.show()
        self.inp_line_2.show()
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.btn_give_otv.clicked.connect(self.calc_beta)

    def calc_beta(self):
        K = float(self.inp_line_2.text())
        F = float(self.inp_line_1.text())
        t = float(self.inp_line_3.text())
        R = float(self.inp_line_4.text())
        D = K * F * t / R**2
        self.conclusion_1.setText('Бета')
        self.lab_otv_1.setText(str(D))
        self.lab_otv_2.setText('(бек)')



    def open_gamma(self):
        self.text_lab_1.setText('Флюенс гамма излучения (кВт*с/м^2)')
        self.text_lab_2.setText('Коефицент ослабления гамма излучения (м)')
        self.text_lab_3.setText('')
        self.text_lab_4.setText('')
        self.text_lab_5.setText('')
        self.inp_line_3.hide()
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.btn_give_otv.clicked.connect(self.calc_gamma)

    def calc_gamma(self):
        F = float(self.inp_line_2.text())
        t = float(self.inp_line_1.text())
        D = F * t
        self.conclusion_1.setText('Гамма')
        self.lab_otv_1.setText(str(D))
        self.lab_otv_2.setText('(грей)')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Alpha_beta_gamme()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
