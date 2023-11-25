from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialok(object):
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
        self.C_medium_time = QtWidgets.QLineEdit(self.frame)
        self.C_medium_time.setGeometry(QtCore.QRect(430, 100, 581, 20))
        self.C_medium_time.setStyleSheet("QLineEdit{\n"
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
        self.C_medium_time.setObjectName("C_medium_time")
        self.CO_cliker = QtWidgets.QLineEdit(self.frame)
        self.CO_cliker.setGeometry(QtCore.QRect(430, 150, 581, 20))
        self.CO_cliker.setStyleSheet("QLineEdit{\n"
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
        self.CO_cliker.setObjectName("CO_cliker")
        self.K_koeficent = QtWidgets.QLineEdit(self.frame)
        self.K_koeficent.setGeometry(QtCore.QRect(430, 200, 581, 20))
        self.K_koeficent.setStyleSheet("QLineEdit{\n"
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
        self.K_koeficent.setObjectName("K_koeficent")
        self.M_clicker = QtWidgets.QLineEdit(self.frame)
        self.M_clicker.setGeometry(QtCore.QRect(430, 250, 581, 20))
        self.M_clicker.setStyleSheet("QLineEdit{\n"
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
        self.M_clicker.setObjectName("M_clicker")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(380, 30, 491, 31))
        self.label.setStyleSheet("font: italic 14pt \"Arial\";\n"
                                 "background-color: none;\n"
                                 "border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 361, 21))
        self.label_2.setStyleSheet("font: 10pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 301, 20))
        self.label_3.setStyleSheet("font: 10pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(60, 200, 361, 21))
        self.label_4.setStyleSheet("font: 10pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(60, 250, 361, 31))
        self.label_5.setStyleSheet("font: 10pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_5.setObjectName("label_5")
        self.btn_give_otv = QtWidgets.QPushButton(self.frame)
        self.btn_give_otv.setGeometry(QtCore.QRect(780, 300, 231, 31))
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
        self.btn_give_otv.clicked.connect(self.otv_koef_final)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 480, 61, 21))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(120, 480, 111, 21))
        self.label_7.setStyleSheet("font: 12pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_7.setObjectName("label_7")
        self.citys_chek = QtWidgets.QComboBox(self.frame)
        self.citys_chek.setGeometry(QtCore.QRect(50, 350, 231, 21))
        self.citys_chek.setStyleSheet("QComboBox {\n"
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
                                      "background-color: rgb(108, 216, 255)\n"
                                      "}")
        self.citys_chek.setObjectName("citys_chek")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.citys_chek.addItem("")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 310, 171, 21))
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_8.setStyleSheet("font: 14pt \"Arial\";\n"
                                   "border: none;\n"
                                   "border-radius: none;\n"
                                   "background-color: none;")
        self.label_8.setObjectName("label_8")
        self.citi_otv = QtWidgets.QLabel(self.frame)
        self.citi_otv.setGeometry(QtCore.QRect(230, 480, 201, 21))
        self.citi_otv.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "border: none;\n"
                                    "border-radius: none;\n"
                                    "background-color: none;")
        self.citi_otv.setText("")
        self.citi_otv.setObjectName("citi_otv")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(440, 480, 131, 21))
        self.label_10.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "border: none;\n"
                                    "border-radius: none;\n"
                                    "background-color: none;")
        self.label_10.setObjectName("label_10")
        self.people_live = QtWidgets.QLabel(self.frame)
        self.people_live.setGeometry(QtCore.QRect(580, 480, 221, 21))
        self.people_live.setStyleSheet("font: 12pt \"Arial\";\n"
                                       "border: none;\n"
                                       "border-radius: none;\n"
                                       "background-color: none;")
        self.people_live.setText("")
        self.people_live.setObjectName("people_live")
        self.skot_live = QtWidgets.QLabel(self.frame)
        self.skot_live.setGeometry(QtCore.QRect(800, 480, 251, 21))
        self.skot_live.setStyleSheet("font: 12pt \"Arial\";\n"
                                     "border: none;\n"
                                     "border-radius: none;\n"
                                     "background-color: none;")
        self.skot_live.setText("")
        self.skot_live.setObjectName("skot_live")
        self.trees_live = QtWidgets.QLabel(self.frame)
        self.trees_live.setGeometry(QtCore.QRect(150, 510, 361, 21))
        self.trees_live.setStyleSheet("font: 12pt \"Arial\";\n"
                                      "border: none;\n"
                                      "border-radius: none;\n"
                                      "background-color: none;")
        self.trees_live.setText("")
        self.trees_live.setObjectName("trees_live")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(420, 510, 401, 21))
        self.label_14.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "border: none;\n"
                                    "border-radius: none;\n"
                                    "background-color: none;")
        self.label_14.setObjectName("label_14")
        self.otv_radiation = QtWidgets.QLabel(self.frame)
        self.otv_radiation.setGeometry(QtCore.QRect(820, 510, 91, 21))
        self.otv_radiation.setStyleSheet("font: 12pt \"Arial\";\n"
                                         "border: none;\n"
                                         "border-radius: none;\n"
                                         "background-color: none;")
        self.otv_radiation.setText("")
        self.otv_radiation.setObjectName("otv_radiation")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(930, 510, 151, 21))
        self.label_16.setStyleSheet("font: 12pt \"Arial\";\n"
                                    "border: none;\n"
                                    "border-radius: none;\n"
                                    "background-color: none;")
        self.label_16.setObjectName("label_16")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.peoplegood = 'безопастной для людей'
        self.peoplefoot = 'опастной для людей'
        self.scotgood = 'безопастной для рогатого скота'
        self.scotfoot = 'опастной для рогатого скота'
        self.treesgood = 'а также безопастной для растений'
        self.treesfoot = 'а также опасной для растений'


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Вычесление коэффициента радиации за год:"))
        self.label.setText(_translate("Dialog", "Вычисления коэффициента радиации в год:"))
        self.label_2.setText(_translate("Dialog", "C - Среднее значение счетчиказа период времени:"))
        self.label_3.setText(_translate("Dialog", "CO - Показатели счетчика в отсуствии радиации:"))
        self.label_4.setText(_translate("Dialog", "K - коэффициент, зависищий от типа используемого счетчика:"))
        self.label_5.setText(_translate("Dialog", "M - множество зависящий от единиц измерения показаний \n"
                                                  "                                       счетчика:"))
        self.btn_give_otv.setText(_translate("Dialog", "Получить ответ:"))
        self.label_6.setText(_translate("Dialog", "Вывод:"))
        self.label_7.setText(_translate("Dialog", "Атмосфера в"))
        self.citys_chek.setItemText(0, _translate("Dialog", "Баткенская область"))
        self.citys_chek.setItemText(1, _translate("Dialog", "Ошская область"))
        self.citys_chek.setItemText(2, _translate("Dialog", "Джалал-Абадская область"))
        self.citys_chek.setItemText(3, _translate("Dialog", "Талаская область"))
        self.citys_chek.setItemText(4, _translate("Dialog", "Чуйская область"))
        self.citys_chek.setItemText(5, _translate("Dialog", "Нарынская область"))
        self.citys_chek.setItemText(6, _translate("Dialog", "Иссык-Кульская область"))
        self.label_8.setText(_translate("Dialog", "Выберите область:"))
        self.label_10.setText(_translate("Dialog", "равна и является"))
        self.label_14.setText(_translate("Dialog", "веть радиация по статистике за этот год состовляет:"))
        self.label_16.setText(_translate("Dialog", "Зиверта (Зв)"))

    def otv_koef_final(self):
        C_med = float(self.C_medium_time.text())
        Co_click = float(self.CO_cliker.text())
        K_koef = float(self.K_koeficent.text())
        M_click = float(self.M_clicker.text())
        R_finali_otv = (C_med - Co_click) / (K_koef * M_click)
        self.otv_radiation.setText(str(R_finali_otv))
        selected = self.citys_chek.currentText()
        if selected == 'Баткенская область':
            self.citi_otv.setText('Баткенской области')
        elif selected == 'Ошская область':
            self.citi_otv.setText('Ошской области')
        elif selected == 'Джалал-Абадская область':
            self.citi_otv.setText('Джалал-Абадской области')
        elif selected == 'Талаская область':
            self.citi_otv.setText('Талаской области')
        elif selected == 'Чуйская область':
            self.citi_otv.setText('Чуйской области')
        elif selected == 'Нарынская область':
            self.citi_otv.setText('Нарынской области')
        elif selected == 'Иссык-Кульская область':
            self.citi_otv.setText('Иссык-кульской области')
        if float(R_finali_otv) >= 2.4:
            self.people_live.setText(self.peoplefoot)
        elif float(R_finali_otv) <= 2.4:
            self.people_live.setText(self.peoplegood)
        if float(R_finali_otv) >= 0.5:
            self.skot_live.setText(self.scotfoot)
        elif float(R_finali_otv) <= 0.5:
            self.skot_live.setText(self.scotgood)
            pass
        if float(R_finali_otv) >= 0.5:
            self.trees_live.setText(self.treesfoot)
            pass
        elif float(R_finali_otv) <= 0.5:
            self.trees_live.setText(self.treesgood)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialok()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
