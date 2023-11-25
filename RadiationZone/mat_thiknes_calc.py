from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mat_thiknes_calculate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 644)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 460, 621))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.inp_line_1 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_1.setGeometry(QtCore.QRect(20, 110, 420, 20))
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
        self.text_lab_1.setGeometry(QtCore.QRect(20, 70, 430, 21))
        self.text_lab_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_1.setObjectName("text_lab_1")
        self.inp_line_2 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_2.setGeometry(QtCore.QRect(20, 190, 420, 20))
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
        self.inp_line_3.setGeometry(QtCore.QRect(20, 270, 420, 20))
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
        self.inp_line_4.setGeometry(QtCore.QRect(20, 350, 420, 20))
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
        self.inp_line_5.setGeometry(QtCore.QRect(20, 430, 420, 20))
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
        self.btn_give_otv.setGeometry(QtCore.QRect(220, 490, 220, 30))
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
        self.text_lab_3.setGeometry(QtCore.QRect(150, 230, 170, 21))
        self.text_lab_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_3.setObjectName("text_lab_3")
        self.text_lab_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_4.setGeometry(QtCore.QRect(30, 310, 400, 21))
        self.text_lab_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_4.setObjectName("text_lab_4")
        self.text_lab_5 = QtWidgets.QLabel(self.widget)
        self.text_lab_5.setGeometry(QtCore.QRect(100, 390, 260, 21))
        self.text_lab_5.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_5.setObjectName("text_lab_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 560, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.label_6.setObjectName("label_6")
        self.trees_live_2 = QtWidgets.QLabel(self.widget)
        self.trees_live_2.setGeometry(QtCore.QRect(70, 560, 130, 21))
        self.trees_live_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_2.setObjectName("trees_live_2")
        self.conclusion_1 = QtWidgets.QLabel(self.widget)
        self.conclusion_1.setGeometry(QtCore.QRect(200, 560, 110, 21))
        self.conclusion_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.conclusion_1.setText("")
        self.conclusion_1.setObjectName("conclusion_1")
        self.text_lab_7 = QtWidgets.QLabel(self.widget)
        self.text_lab_7.setGeometry(QtCore.QRect(14, 20, 440, 20))
        self.text_lab_7.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_7.setObjectName("text_lab_7")
        self.conclusion_2 = QtWidgets.QLabel(self.widget)
        self.conclusion_2.setGeometry(QtCore.QRect(320, 560, 40, 21))
        self.conclusion_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.conclusion_2.setObjectName("conclusion_2")
        self.text_lab_2 = QtWidgets.QLabel(Dialog)
        self.text_lab_2.setGeometry(QtCore.QRect(180, 160, 120, 21))
        self.text_lab_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_2.setObjectName("text_lab_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_give_otv.clicked.connect(self.calculate)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.text_lab_1.setText(_translate("Dialog", "Линейного коэффициента ослабления материала  (μ)"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.text_lab_3.setText(_translate("Dialog", "Энерговыделение (Q)"))
        self.text_lab_4.setText(_translate("Dialog", "Длине пробега (β) для защищаемого типа  (МэВ/г)"))
        self.text_lab_5.setText(_translate("Dialog", "Отношения энергии фотона (E)"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.trees_live_2.setText(_translate("Dialog", "Ответ равняется:"))
        self.text_lab_7.setText(_translate("Dialog", "Расчет толщины материала для защиты от радиации"))
        self.conclusion_2.setText(_translate("Dialog", "(см)"))
        self.text_lab_2.setText(_translate("Dialog", "Плотность (ρ)"))

    def calculate(self):
        h = float(self.inp_line_1.text())
        p = float(self.inp_line_2.text())
        q = float(self.inp_line_3.text())
        b = float(self.inp_line_4.text())
        e = float(self.inp_line_5.text())
        otv = 1.2 * (h/p) * (q / b)**(1/2) * (e / p)**(1/2)
        self.conclusion_1.setText(str(otv))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_mat_thiknes_calculate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
