from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Unite_calculate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 432)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 460, 411))
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
        self.combobox.addItem("")
        self.combobox.addItem("")
        self.inp_line_1 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_1.setGeometry(QtCore.QRect(20, 50, 420, 20))
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
        self.btn_give_otv = QtWidgets.QPushButton(self.widget)
        self.btn_give_otv.setGeometry(QtCore.QRect(10, 360, 440, 30))
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
        self.text_lab_2 = QtWidgets.QLabel(self.widget)
        self.text_lab_2.setGeometry(QtCore.QRect(30, 150, 120, 21))
        self.text_lab_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_2.setObjectName("text_lab_2")
        self.text_lab_3 = QtWidgets.QLabel(self.widget)
        self.text_lab_3.setGeometry(QtCore.QRect(30, 200, 120, 21))
        self.text_lab_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_3.setObjectName("text_lab_3")
        self.text_lab_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_4.setGeometry(QtCore.QRect(30, 250, 120, 21))
        self.text_lab_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_4.setObjectName("text_lab_4")
        self.text_lab_5 = QtWidgets.QLabel(self.widget)
        self.text_lab_5.setGeometry(QtCore.QRect(30, 300, 120, 21))
        self.text_lab_5.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_5.setObjectName("text_lab_5")
        self.text_lab_otv_1 = QtWidgets.QLabel(self.widget)
        self.text_lab_otv_1.setGeometry(QtCore.QRect(160, 100, 150, 21))
        self.text_lab_otv_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_1.setText("")
        self.text_lab_otv_1.setObjectName("text_lab_otv_1")
        self.text_lab_otv_2 = QtWidgets.QLabel(self.widget)
        self.text_lab_otv_2.setGeometry(QtCore.QRect(160, 150, 150, 21))
        self.text_lab_otv_2.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_2.setText("")
        self.text_lab_otv_2.setObjectName("text_lab_otv_2")
        self.text_lab_otv_8 = QtWidgets.QLabel(self.widget)
        self.text_lab_otv_8.setGeometry(QtCore.QRect(160, 210, 150, 21))
        self.text_lab_otv_8.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_8.setText("")
        self.text_lab_otv_8.setObjectName("text_lab_otv_8")
        self.text_lab_otv_3 = QtWidgets.QLabel(self.widget)
        self.text_lab_otv_3.setGeometry(QtCore.QRect(160, 200, 150, 21))
        self.text_lab_otv_3.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_3.setText("")
        self.text_lab_otv_3.setObjectName("text_lab_otv_3")
        self.text_lab_otv_4 = QtWidgets.QLabel(self.widget)
        self.text_lab_otv_4.setGeometry(QtCore.QRect(160, 250, 150, 21))
        self.text_lab_otv_4.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_4.setText("")
        self.text_lab_otv_4.setObjectName("text_lab_otv_4")
        self.text_lab_1 = QtWidgets.QLabel(Dialog)
        self.text_lab_1.setGeometry(QtCore.QRect(40, 110, 120, 21))
        self.text_lab_1.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_1.setObjectName("text_lab_1")
        self.text_lab_otv_5 = QtWidgets.QLabel(Dialog)
        self.text_lab_otv_5.setGeometry(QtCore.QRect(170, 310, 150, 21))
        self.text_lab_otv_5.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.text_lab_otv_5.setText("")
        self.text_lab_otv_5.setObjectName("text_lab_otv_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.combobox.activated.connect(self.choice)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.combobox.setItemText(0, _translate("Dialog", "..."))
        self.combobox.setItemText(1, _translate("Dialog", "Сиверт (Sv)"))
        self.combobox.setItemText(2, _translate("Dialog", "Грей (Gy)"))
        self.combobox.setItemText(3, _translate("Dialog", "Рентген(R)"))
        self.combobox.setItemText(4, _translate("Dialog", "Беккелер(Bq)"))
        self.combobox.setItemText(5, _translate("Dialog", "Кюри(Ci)"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.text_lab_2.setText(_translate("Dialog", "Грей(Gy)"))
        self.text_lab_3.setText(_translate("Dialog", "Ренген(R)"))
        self.text_lab_4.setText(_translate("Dialog", "Беккерель(Bq)"))
        self.text_lab_5.setText(_translate("Dialog", "Кюри (Ci)"))
        self.text_lab_1.setText(_translate("Dialog", "Сиверт(Sv)"))

    def choice(self):
        text = self.combobox.currentText()
        if text == 'Сиверт (Sv)':
            self.ConvertSivert()
        elif text == 'Грей (Gy)':
            self.ConvertGrey()
        elif text == 'Рентген(R)':
            self.ConvertRentgen()
        elif text == 'Беккелер(Bq)':
            self.ConvertBEkkeler()
        elif text == 'Кюри(Ci)':
            self.ConvertKuri()
        else:
            self.text_lab_otv_1.setText('')
            self.text_lab_otv_2.setText('')
            self.text_lab_otv_3.setText('')
            self.text_lab_otv_4.setText('')
            self.text_lab_otv_5.setText('')

    def ConvertSivert(self):
        self.btn_give_otv.clicked.connect(self.btn_sivert_calc_1)
        self.text_lab_otv_1.setText('')
        self.text_lab_otv_2.setText('')
        self.text_lab_otv_3.setText('')
        self.text_lab_otv_4.setText('')
        self.text_lab_otv_5.setText('')
        self.text_lab_5.show()
        self.text_lab_1.show()
        self.text_lab_2.show()
        self.text_lab_3.show()
        self.text_lab_4.show()
        self.text_lab_5.show()


    def btn_sivert_calc_1(self):
        self.inp_1 = float(self.inp_line_1.text())
        convertSivert = self.inp_1 * 1
        convertgrey = self.inp_1 * 1
        convertRentgen = self.inp_1 * 100000
        convertBekeler = self.inp_1 * 1000
        convertKuri = self.inp_1 * 100

        self.text_lab_otv_1.setText(str(convertSivert))
        self.text_lab_otv_2.setText(str(convertgrey))
        self.text_lab_otv_3.setText(str(convertRentgen))
        self.text_lab_otv_4.setText(str(convertBekeler))
        self.text_lab_otv_5.setText(str(convertKuri))


    def ConvertGrey(self):
        self.text_lab_1.show()
        self.text_lab_2.show()
        self.text_lab_3.show()
        self.text_lab_4.show()
        self.text_lab_5.show()
        self.btn_give_otv.clicked.connect(self.btn_sivert_calc_2)
        self.text_lab_5.hide()
        self.text_lab_otv_1.setText('')
        self.text_lab_otv_2.setText('')
        self.text_lab_otv_3.setText('')
        self.text_lab_otv_4.setText('')
        self.text_lab_otv_5.setText('')




    def btn_sivert_calc_2(self):
        self.inp_2 = float(self.inp_line_1.text())
        convertSivert = self.inp_2 * 1
        convertgrey = self.inp_2 * 1
        convertRentgen = self.inp_2 * 100
        convertBekeler = self.inp_2 *  3.7e10

        self.text_lab_otv_1.setText(str(convertSivert))
        self.text_lab_otv_2.setText(str(convertgrey))
        self.text_lab_otv_3.setText(str(convertRentgen))
        self.text_lab_otv_4.setText(str(convertBekeler))
        self.text_lab_otv_5.setText('')

    def ConvertRentgen(self):
        self.btn_give_otv.clicked.connect(self.btn_sivert_calc_3)
        self.text_lab_otv_1.setText('')
        self.text_lab_otv_2.setText('')
        self.text_lab_otv_3.setText('')
        self.text_lab_otv_4.setText('')
        self.text_lab_otv_5.setText('')
        self.text_lab_5.show()
        self.text_lab_otv_5.show()
        self.text_lab_1.show()
        self.text_lab_2.show()
        self.text_lab_3.show()
        self.text_lab_4.show()
        self.text_lab_5.show()



    def btn_sivert_calc_3(self):
        self.inp_3 = float(self.inp_line_1.text())
        convertSivert = self.inp_3 * 0.00876
        convertgrey = self.inp_3 / 100
        convertRentgen = self.inp_3 * 1
        convertBekeler = self.inp_3 / 0.00877
        convertKuri = self.inp_3 * 3.7 * 10**10

        self.text_lab_otv_1.setText(str(convertSivert))
        self.text_lab_otv_2.setText(str(convertgrey))
        self.text_lab_otv_3.setText(str(convertRentgen))
        self.text_lab_otv_4.setText(str(convertBekeler))
        self.text_lab_otv_5.setText(str(convertKuri))
    def ConvertBEkkeler(self):
        self.btn_give_otv.clicked.connect(self.btn_sivert_calc_4)
        self.text_lab_otv_1.setText('')
        self.text_lab_otv_2.setText('')
        self.text_lab_otv_3.setText('')
        self.text_lab_otv_4.setText('')
        self.text_lab_otv_5.setText('')
        self.text_lab_5.show()
        self.text_lab_1.show()
        self.text_lab_2.show()
        self.text_lab_3.show()
        self.text_lab_4.show()
        self.text_lab_5.show()

    def btn_sivert_calc_4(self):
        self.inp_4 = float(self.inp_line_1.text())
        convertSivert = self.inp_4 / 1000
        convertgrey = self.inp_4  * 3.7e10
        convertRentgen = self.inp_4 * 1 * 0.00876 / (4 * 3.14 * 1 ** 2)
        convertBekeler = self.inp_4 * 1
        convertKuri = self.inp_4 * 0.0000277778

        self.text_lab_otv_1.setText(str(convertSivert))
        self.text_lab_otv_2.setText(str(convertgrey))
        self.text_lab_otv_3.setText(str(convertRentgen))
        self.text_lab_otv_4.setText(str(convertBekeler))
        self.text_lab_otv_5.setText(str(convertKuri))
    def ConvertKuri(self):
        self.btn_give_otv.clicked.connect(self.btn_sivert_calc_5)
        self.text_lab_otv_1.setText('')
        self.text_lab_otv_2.setText('')
        self.text_lab_otv_3.setText('')
        self.text_lab_otv_4.setText('')
        self.text_lab_otv_5.setText('')
        self.text_lab_5.show()
        self.text_lab_1.show()
        self.text_lab_2.show()
        self.text_lab_3.show()
        self.text_lab_4.show()
        self.text_lab_5.show()

    def btn_sivert_calc_5(self):
        self.inp_5 = float(self.inp_line_1.text())
        convertSivert = self.inp_5  * 0.00024 / 3600
        convertgrey = (self.inp_5 * 0.008) * 3600
        convertRentgen = self.inp_5 * 37000000
        convertBekeler = self.inp_5 * 3.7e10
        convertKuri = self.inp_5 * 1

        self.text_lab_otv_1.setText(str(convertSivert))
        self.text_lab_otv_2.setText(str(convertgrey))
        self.text_lab_otv_3.setText(str(convertRentgen))
        self.text_lab_otv_4.setText(str(convertBekeler))
        self.text_lab_otv_5.setText(str(convertKuri))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Unite_calculate()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
