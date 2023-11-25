from PyQt5 import QtCore, QtGui, QtWidgets
import math

class Ui_hide_radiation(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1150, 687)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(29, 30, 1091, 631))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.inp_line_2 = QtWidgets.QLineEdit(self.frame)
        self.inp_line_2.setGeometry(QtCore.QRect(450, 180, 581, 20))
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
                                      "}")
        self.inp_line_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_2.setClearButtonEnabled(True)
        self.inp_line_2.setObjectName("inp_line_2")
        self.inp_line_3 = QtWidgets.QLineEdit(self.frame)
        self.inp_line_3.setGeometry(QtCore.QRect(450, 230, 581, 20))
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
                                      "}")
        self.inp_line_3.setClearButtonEnabled(True)
        self.inp_line_3.setObjectName("inp_line_3")
        self.inp_line_4 = QtWidgets.QLineEdit(self.frame)
        self.inp_line_4.setGeometry(QtCore.QRect(450, 280, 581, 20))
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
                                      "}")
        self.inp_line_4.setClearButtonEnabled(True)
        self.inp_line_4.setObjectName("inp_line_4")
        self.inp_line_5 = QtWidgets.QLineEdit(self.frame)
        self.inp_line_5.setGeometry(QtCore.QRect(450, 330, 581, 20))
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
                                      "}")
        self.inp_line_5.setClearButtonEnabled(True)
        self.inp_line_5.setObjectName("inp_line_5")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(480, 40, 520, 21))
        self.label.setStyleSheet("font: italic 14pt \"Arial\";\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setObjectName("label")
        self.text_label_2 = QtWidgets.QLabel(self.frame)
        self.text_label_2.setGeometry(QtCore.QRect(50, 180, 361, 21))
        self.text_label_2.setStyleSheet("font: 10pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.text_label_2.setText("")
        self.text_label_2.setObjectName("text_label_2")
        self.text_label_3 = QtWidgets.QLabel(self.frame)
        self.text_label_3.setGeometry(QtCore.QRect(50, 230, 361, 20))
        self.text_label_3.setStyleSheet("font: 10pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.text_label_3.setText("")
        self.text_label_3.setObjectName("text_label_3")
        self.text_label_4 = QtWidgets.QLabel(self.frame)
        self.text_label_4.setGeometry(QtCore.QRect(50, 280, 361, 21))
        self.text_label_4.setStyleSheet("font: 10pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.text_label_4.setText("")
        self.text_label_4.setObjectName("text_label_4")
        self.text_label_5 = QtWidgets.QLabel(self.frame)
        self.text_label_5.setGeometry(QtCore.QRect(50, 330, 361, 31))
        self.text_label_5.setStyleSheet("font: 10pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.text_label_5.setText("")
        self.text_label_5.setObjectName("text_label_5")
        self.btn_give_otv = QtWidgets.QPushButton(self.frame)
        self.btn_give_otv.setGeometry(QtCore.QRect(780, 380, 231, 31))
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
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 540, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_6.setObjectName("label_6")
        self.conclusion_1 = QtWidgets.QLabel(self.frame)
        self.conclusion_1.setGeometry(QtCore.QRect(80, 540, 60, 21))
        self.conclusion_1.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.conclusion_1.setText("")
        self.conclusion_1.setObjectName("conclusion_1")
        self.conclusion_2 = QtWidgets.QLabel(self.frame)
        self.conclusion_2.setGeometry(QtCore.QRect(360, 540, 130, 21))
        self.conclusion_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.conclusion_2.setText("")
        self.conclusion_2.setObjectName("conclusion_2")
        self.polution_not_interest = QtWidgets.QComboBox(self.frame)
        self.polution_not_interest.setGeometry(QtCore.QRect(40, 80, 390, 21))
        self.polution_not_interest.setStyleSheet("QComboBox {\n"
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
        self.polution_not_interest.setObjectName("polution_not_interest")
        self.polution_not_interest.addItem("")
        self.polution_not_interest.addItem("")
        self.polution_not_interest.addItem("")
        self.polution_not_interest.addItem("")
        self.text_label_1 = QtWidgets.QLabel(self.frame)
        self.text_label_1.setGeometry(QtCore.QRect(50, 140, 361, 21))
        self.text_label_1.setStyleSheet("font: 10pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.text_label_1.setText("")
        self.text_label_1.setObjectName("text_label_1")
        self.inp_line_1 = QtWidgets.QLineEdit(self.frame)
        self.inp_line_1.setGeometry(QtCore.QRect(450, 140, 581, 20))
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
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(200, 40, 90, 21))
        self.label_9.setStyleSheet("font: italic 12pt \"Arial\";\n"
                                   "background-color: none;\n"
                                   "border: none;")
        self.label_9.setObjectName("label_9")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(490, 540, 281, 21))
        self.label_8.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_8.setObjectName("label_8")
        self.lab_otv_1 = QtWidgets.QLabel(self.frame)
        self.lab_otv_1.setGeometry(QtCore.QRect(780, 540, 71, 21))
        self.lab_otv_1.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "border: none;\n"
                                     "border-radius: none;\n"
                                     "background-color: none;")
        self.lab_otv_1.setText("")
        self.lab_otv_1.setObjectName("lab_otv_1")
        self.lab_otv_2 = QtWidgets.QLabel(self.frame)
        self.lab_otv_2.setGeometry(QtCore.QRect(860, 540, 71, 21))
        self.lab_otv_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "border: none;\n"
                                     "border-radius: none;\n"
                                     "background-color: none;")
        self.lab_otv_2.setText("")
        self.lab_otv_2.setObjectName("lab_otv_2")
        self.trees_live_2 = QtWidgets.QLabel(self.frame)
        self.trees_live_2.setGeometry(QtCore.QRect(150, 540, 201, 21))
        self.trees_live_2.setStyleSheet("font: 12pt \"Arial\";\n"
                                        "border: none;\n"
                                        "border-radius: none;\n"
                                        "background-color: none;")
        self.trees_live_2.setObjectName("trees_live_2")
        self.img_png = QtWidgets.QLabel(self.frame)
        self.img_png.setGeometry(QtCore.QRect(1030, 580, 50, 40))
        self.img_png.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.img_png.setText("")
        self.img_png.setPixmap(QtGui.QPixmap("../зеленный.png"))
        self.img_png.setObjectName("img_png")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.polution_not_interest.activated.connect(self.change_polution_1)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вычеслить загрязнения"))
        self.label.setText(_translate("Dialog", "Вычисления радиации  в воде, воздухе а также в почве:"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.polution_not_interest.setItemText(0, _translate("Dialog", "..."))
        self.polution_not_interest.setItemText(1, _translate("Dialog", "Вычеслить радиацию в воздухе:"))
        self.polution_not_interest.setItemText(2, _translate("Dialog", "Вычислить радиацию в почве:"))
        self.polution_not_interest.setItemText(3, _translate("Dialog", "Вычислить радиацию в воде:"))
        self.label_9.setText(_translate("Dialog", "Выбрать:"))
        self.label_8.setText(_translate("Dialog", "веть при вычислении ответ равняется:"))
        self.trees_live_2.setText(_translate("Dialog", "в этой местности является"))

    def change_polution_1(self):
        text = self.polution_not_interest.currentText()
        if text == 'Вычеслить радиацию в воздухе:':
            self.air_radiation()
        elif text == 'Вычислить радиацию в почве:':
            self.soil_radiation()
        elif text == 'Вычислить радиацию в воде:':
            self.water_radiation()
        else:
            self.text_label_1.setText('')
            self.text_label_2.setText('')
            self.text_label_3.setText('')
            self.text_label_4.setText('')
            self.text_label_5.setText('')
            self.conclusion_1.setText('')
            self.conclusion_2.setText('')
            self.lab_otv_1.setText('')
            self.lab_otv_2.setText('')
            self.img_png.clear()
            self.inp_line_1.show()
            self.inp_line_2.show()
            self.inp_line_3.show()
            self.inp_line_4.show()
            self.inp_line_5.show()

    def air_radiation(self):
        self.text_label_1.setText('Aктивность источника радиации(Бк)')
        self.text_label_2.setText('Kоэффициент поглощения воздуха(около 0,6 см²/г)')
        self.text_label_3.setText('Pасстояние от источника радиации до точки измерения, (м)')
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.text_label_4.setText('')
        self.text_label_5.setText('')
        self.conclusion_1.setText('')
        self.conclusion_2.setText('')
        self.lab_otv_1.setText('')
        self.lab_otv_2.setText('')
        self.img_png.clear()

        self.btn_give_otv.clicked.connect(self.calc_air_radaition)

    def calc_air_radaition(self):
        A = float(self.inp_line_1.text())
        k = float(self.inp_line_2.text())
        r = float(self.inp_line_3.text())

        D_otv = A / (k * r**2)
        self.conclusion_1.setText('Воздух')
        self.lab_otv_1.setText(str(D_otv))
        self.lab_otv_2.setText('(Gy)')

        if D_otv <= 1:
            self.conclusion_2.setText('хорошим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif D_otv >= 1 and D_otv <= 7:
            self.conclusion_2.setText('нормальным')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))

    def soil_radiation(self):
        self.text_label_1.setText('Aктивность урана-238 (единица измерения - Бк/кг);')
        self.text_label_2.setText('Kонцентрация урана-238 в почве (Бк/кг)')
        self.text_label_3.setText('Kоэффициент, геометрического учета и расстояние до него:')
        self.text_label_4.setText('Коэффициент, формы источника:')
        self.text_label_5.setText('Расстояние от точки до источника излучения (м)')
        self.conclusion_1.setText('')
        self.conclusion_2.setText('')
        self.lab_otv_1.setText('')
        self.lab_otv_2.setText('')
        self.img_png.clear()
        self.inp_line_1.show()
        self.inp_line_2.show()
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.inp_line_5.show()

        self.btn_give_otv.clicked.connect(self.calc_soil_radaition)

    def calc_soil_radaition(self):
        A = float(self.inp_line_1.text())
        c = float(self.inp_line_2.text())
        F = float(self.inp_line_3.text())
        f = float(self.inp_line_3.text())
        r = float(self.inp_line_3.text())
        D_otv = A * c * f * F / r ** 2

        self.lab_otv_1.setText(str(D_otv))
        self.lab_otv_2.setText('(Gy)')
        self.conclusion_1.setText('Почва')

        if D_otv <= 1:
            self.conclusion_2.setText('хорошим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif D_otv >= 1 and D_otv <= 7:
            self.conclusion_2.setText('нормальным')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))



    def water_radiation(self):
        self.text_label_1.setText('Mасса частицы')
        self.text_label_2.setText('Постоянная Больцмана;')
        self.text_label_3.setText('Температура идеального газа;')
        self.text_label_4.setText('Скорость частицы')
        self.conclusion_1.setText('')
        self.conclusion_2.setText('')
        self.lab_otv_1.setText('')
        self.lab_otv_2.setText('')
        self.img_png.clear()
        self.inp_line_1.show()
        self.inp_line_2.show()
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.inp_line_5.hide()

        self.btn_give_otv.clicked.connect(self.calc_water_radaition)

    def calc_water_radaition(self):
        m = float(self.inp_line_1.text())
        k = float(self.inp_line_2.text())
        T = float(self.inp_line_3.text())
        v = float(self.inp_line_3.text())

        pi = 3.14159265358979323846
        F_v_otv = 4 * pi * ((m / (2 * pi * k * T))**(3/2) * v**2*math.exp(-m*v**2/(2*k*T)))

        self.lab_otv_1.setText(str(F_v_otv))
        self.lab_otv_2.setText('(f/s)')
        self.conclusion_1.setText('Вода')

        if F_v_otv <= 1:
            self.conclusion_2.setText('хорошим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif F_v_otv >= 1 and F_v_otv <= 7:
            self.conclusion_2.setText('нормальным')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохим')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_hide_radiation()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
