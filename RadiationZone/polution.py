from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Polution(object):
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
        self.label.setGeometry(QtCore.QRect(420, 40, 251, 21))
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
        self.conclusion_1.setGeometry(QtCore.QRect(80, 540, 141, 21))
        self.conclusion_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.conclusion_1.setText("")
        self.conclusion_1.setObjectName("conclusion_1")
        self.conclusion_2 = QtWidgets.QLabel(self.frame)
        self.conclusion_2.setGeometry(QtCore.QRect(430, 540, 201, 21))
        self.conclusion_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.conclusion_2.setText("")
        self.conclusion_2.setObjectName("conclusion_2")
        self.polution_not_interest = QtWidgets.QComboBox(self.frame)
        self.polution_not_interest.setGeometry(QtCore.QRect(50, 80, 271, 21))
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
        self.polution_with_interest = QtWidgets.QComboBox(self.frame)
        self.polution_with_interest.setGeometry(QtCore.QRect(720, 80, 300, 21))
        self.polution_with_interest.setStyleSheet("QComboBox {\n"
"background-color: rgba(255, 255, 255, 20);\n"
"font: italic 12pt \"Arial\";\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgba(255, 255, 255, 50);\n"
"background-color: rgba(255, 255, 255, 20);\n"
"width: 20px;\n"
"height: 20px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"font-size: 16px;\n"
"height: 30px;\n"
"    background-color: rgb(166, 227, 255);\n"
"}")
        self.polution_with_interest.setObjectName("polution_with_interest")
        self.polution_with_interest.addItem("")
        self.polution_with_interest.addItem("")
        self.polution_with_interest.addItem("")
        self.polution_with_interest.addItem("")
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
"}")
        self.inp_line_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_1.setClearButtonEnabled(True)
        self.inp_line_1.setObjectName("inp_line_1")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(60, 40, 251, 21))
        self.label_9.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(760, 40, 241, 21))
        self.label_11.setStyleSheet("font: italic 12pt \"Arial\";\n"
"background-color: none;\n"
"border: none;")
        self.label_11.setObjectName("label_11")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(642, 540, 281, 21))
        self.label_8.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.label_8.setObjectName("label_8")
        self.lab_otv_1 = QtWidgets.QLabel(self.frame)
        self.lab_otv_1.setGeometry(QtCore.QRect(930, 540, 71, 21))
        self.lab_otv_1.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_1.setText("")
        self.lab_otv_1.setObjectName("lab_otv_1")
        self.lab_otv_2 = QtWidgets.QLabel(self.frame)
        self.lab_otv_2.setGeometry(QtCore.QRect(1009, 540, 71, 21))
        self.lab_otv_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.lab_otv_2.setText("")
        self.lab_otv_2.setObjectName("lab_otv_2")
        self.trees_live_2 = QtWidgets.QLabel(self.frame)
        self.trees_live_2.setGeometry(QtCore.QRect(220, 540, 201, 21))
        self.trees_live_2.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.trees_live_2.setObjectName("trees_live_2")
        self.img_png = QtWidgets.QLabel(self.frame)
        self.img_png.setGeometry(QtCore.QRect(1020, 580, 50, 40))
        self.img_png.setStyleSheet("font: 12pt \"Arial\";\n"
"border: none;\n"
"border-radius: none;\n"
"background-color: none;")
        self.img_png.setText("")
        # self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        self.img_png.setObjectName("img_png")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        self.polution_not_interest.activated.connect(self.change_polution_1)
        self.polution_with_interest.activated.connect(self.change_pollution_2)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вычеслить загрязнения"))
        self.label.setText(_translate("Dialog", "Вычисления загрязнения."))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.polution_not_interest.setItemText(0, _translate("Dialog", "-------------------------------------------------"))
        self.polution_not_interest.setItemText(1, _translate("Dialog", "Вычислить загрязнения воздуха:"))
        self.polution_not_interest.setItemText(2, _translate("Dialog", "Вычислить загрязнения почвы:"))
        self.polution_not_interest.setItemText(3, _translate("Dialog", "Вычислить загрязнения воды:"))
        self.polution_with_interest.setItemText(0, _translate("Dialog", "------------------------------------------------------"))
        self.polution_with_interest.setItemText(1, _translate("Dialog", "Вычислить загрязнения воздуха в %"))
        self.polution_with_interest.setItemText(2, _translate("Dialog", "Вычислить загрязнения почвы в %"))
        self.polution_with_interest.setItemText(3, _translate("Dialog", "Вычислить загрязнения воды в %"))
        self.label_9.setText(_translate("Dialog", "Без процентном соотношении:"))
        self.label_11.setText(_translate("Dialog", "В процентном соотношении:"))
        self.label_8.setText(_translate("Dialog", "веть при вычислении ответ равняется:"))
        self.trees_live_2.setText(_translate("Dialog", "в этой местности является"))

    def change_pollution_2(self):
        text_2 = self.polution_with_interest.currentText()
        if text_2 == 'Вычислить загрязнения воздуха в %':
            self.air_pollution_2()
        elif text_2 == 'Вычислить загрязнения почвы в %':
            self.soil_pollution_2()
        elif text_2 == 'Вычислить загрязнения воды в %':
            self.water_pollution_2()
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



    def water_pollution_2(self):
        self.text_label_1.setText('Концентрация загрезнителя:')
        self.text_label_2.setText('Допустимый Концентрация загрезнителя:')
        self.inp_line_3.hide()
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.btn_give_otv.clicked.connect(self.water_pollution_2_otv)

    def water_pollution_2_otv(self):
        water_kol_pollution = float(self.inp_line_2.text())
        water_max_colution = float(self.inp_line_1.text())
        water_colluction_otv = (water_kol_pollution / water_max_colution) * 100
        self.conclusion_1.setText('Вода')
        self.lab_otv_1.setText(str(water_colluction_otv))
        self.lab_otv_2.setText('%')
        if water_colluction_otv <= 80:
            self.conclusion_2.setText('отличная состояния воды')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif water_colluction_otv >= 80 and water_colluction_otv <= 120:
            self.conclusion_2.setText('нормальным состояния воды')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохое сосотояния воды')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))

    def soil_pollution_2(self):
        self.text_label_1.setText('Количество загрязнения в почве:')
        self.text_label_2.setText('Допустимый уровень загрязнения:')
        self.inp_line_3.hide()
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.btn_give_otv.clicked.connect(self.soil_pollution_2_otv)


    def soil_pollution_2_otv(self):
        soil_kol_pollution = float(self.inp_line_2.text())
        soil_max_colution = float(self.inp_line_1.text())
        soil_colluction_otv = (soil_kol_pollution / soil_max_colution) * 100
        self.conclusion_1.setText('Почва')
        self.lab_otv_1.setText(str(soil_colluction_otv))
        self.lab_otv_2.setText('%')
        if soil_colluction_otv <= 80:
            self.conclusion_2.setText('отличная состояния почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif soil_colluction_otv >= 80 and soil_colluction_otv <= 120:
            self.conclusion_2.setText('нормальным состояния почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохое сосотояния почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))


    def air_pollution_2(self):
        self.text_label_1.setText('Количество загрязнителя в воздухе:')
        self.text_label_2.setText('Допустимая концентрация загрязнения:')
        self.inp_line_3.hide()
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.btn_give_otv.clicked.connect(self.air_pollution_2_otv)



    def air_pollution_2_otv(self):
        air_kol_pollution = float(self.inp_line_2.text())
        air_max_colution = float(self.inp_line_1.text())
        air_colluction_otv = (air_kol_pollution / air_max_colution) * 100
        self.conclusion_1.setText('Воздух')
        self.lab_otv_1.setText(str(air_colluction_otv))
        self.lab_otv_2.setText('%')
        if air_colluction_otv <= 80:
            self.conclusion_2.setText('отличная состояния воздуха')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif air_colluction_otv >= 80 and air_colluction_otv <= 120:
            self.conclusion_2.setText('нормальным состояния воздуха')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохое сосотояния воздуха')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))




    # Второе вычисление с процентами


    def change_polution_1(self):
        text = self.polution_not_interest.currentText()
        if text == 'Вычислить загрязнения воздуха:':
            self.air_pollution_1()
        elif text == 'Вычислить загрязнения почвы:':
            self.soil_pollution_1()
        elif text == 'Вычислить загрязнения воды:':
            self.water_pollution_1()
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




    def water_pollution_1(self):
        self.text_label_1.setText('M - Масса загрязнителя')
        self.text_label_2.setText('V - объем воды')
        self.inp_line_3.hide()
        self.inp_line_4.hide()
        self.inp_line_5.hide()
        self.text_label_3.setText('')
        self.text_label_4.setText('')
        self.text_label_5.setText('')
        self.btn_give_otv.clicked.connect(self.water_pollution_1_otv)

    def water_pollution_1_otv(self):
        M = float(self.inp_line_2.text())
        V = float(self.inp_line_1.text())
        C_Otv = M / V
        self.conclusion_1.setText('Вода')
        self.lab_otv_1.setText(str(C_Otv))
        self.lab_otv_2.setText('(мг/л)')
        if C_Otv <= 0.3:
            self.conclusion_2.setText('отличный выбор для питья')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif C_Otv >= 0.3 and C_Otv <= 1:
            self.conclusion_2.setText('нормальным для питья')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('вредным для питья')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))



    # вычисления загрезненности почвы 1
    def soil_pollution_1(self):
        self.text_label_1.setText('Концентрация загрязнителя в исследуемом образце почвы')
        self.text_label_2.setText('Концентрация загрязнителя в образце почвы')
        self.text_label_3.setText('Вес образца почвы, взятого для анализа, выраженный(г)')
        self.text_label_4.setText('Плотность почвы, выраженная в граммах на (г/см³)')
        self.text_label_5.setText('Коэффициент перевода единиц измерения.')
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.inp_line_5.show()
        self.btn_give_otv.clicked.connect(self.soil_pollution_1_otv)


    def soil_pollution_1_otv(self):
        B = float(self.inp_line_2.text())
        A = float(self.inp_line_1.text())
        D = float(self.inp_line_3.text())
        E = float(self.inp_line_4.text())
        F = float(self.inp_line_5.text())
        C_otv = (A - B) * D / E * F
        self.conclusion_1.setText('Почва за год')
        self.lab_otv_1.setText(str(C_otv))
        self.lab_otv_2.setText('мг/кг')
        if C_otv <= 45:
            self.conclusion_2.setText('хорошим для почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif C_otv >= 45 and C_otv <= 63:
            self.conclusion_2.setText('нормальным для почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохим для почвы')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))



    # нахождения состава воздуха 1 без процентном составе
    def air_pollution_1(self):
        self.text_label_1.setText('I-Hight - Верхний придел индекса для заданного диапазонна:')
        self.text_label_2.setText('I-Low - Нижний придел индекса для заданного диапазонна:')
        self.text_label_3.setText('C-Hight - Верхний придел концентрации:')
        self.text_label_4.setText('C-Low - Нижний придел концентрации:')
        self.text_label_5.setText('C - Концентрация загрязнения:')
        self.inp_line_3.show()
        self.inp_line_4.show()
        self.inp_line_5.show()
        self.btn_give_otv.clicked.connect(self.air_pollution_1_otv)

    def air_pollution_1_otv(self):
        i_hight = float(self.inp_line_1.text())
        i_low = float(self.inp_line_2.text())
        c_hight = float(self.inp_line_3.text())
        c_low = float(self.inp_line_4.text())
        c = float(self.inp_line_5.text())
        AQI = (i_hight - i_low) / (c_hight - c_low) * (c - c_low) + i_low
        self.conclusion_1.setText('Воздух')
        self.lab_otv_1.setText(str(AQI))
        self.lab_otv_2.setText('(μg/m³)')
        if AQI <= 80:
            self.conclusion_2.setText('хорошим для дыхания')
            self.img_png.setPixmap(QtGui.QPixmap("Images/зеленный.png"))
        elif AQI >= 80 and AQI <= 120:
            self.conclusion_2.setText('нормальным для дыхания')
            self.img_png.setPixmap(QtGui.QPixmap("Images/желтый.png"))
        else:
            self.conclusion_2.setText('плохим для дыхания')
            self.img_png.setPixmap(QtGui.QPixmap("Images/красный.png"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Polution()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
