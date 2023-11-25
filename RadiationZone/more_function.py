from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MoreFunction(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1196, 697)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(35, 31, 1121, 640))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(420, 60, 370, 40))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 260, 19))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(840, 60, 200, 40))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.hoe_to_create_bunker = QtWidgets.QPushButton(self.frame)
        self.hoe_to_create_bunker.setGeometry(QtCore.QRect(400, 130, 370, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.hoe_to_create_bunker.setFont(font)
        self.hoe_to_create_bunker.setStyleSheet("QPushButton{\n"
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
        self.hoe_to_create_bunker.setIcon(icon)
        self.hoe_to_create_bunker.setObjectName("hoe_to_create_bunker")
        self.how_to_protect = QtWidgets.QPushButton(self.frame)
        self.how_to_protect.setGeometry(QtCore.QRect(60, 130, 330, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.how_to_protect.setFont(font)
        self.how_to_protect.setStyleSheet("QPushButton{\n"
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
        self.how_to_protect.setIcon(icon)
        self.how_to_protect.setObjectName("how_to_protect")
        self.global_call = QtWidgets.QPushButton(self.frame)
        self.global_call.setGeometry(QtCore.QRect(780, 130, 300, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.global_call.setFont(font)
        self.global_call.setStyleSheet("QPushButton{\n"
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
        self.global_call.setIcon(icon)
        self.global_call.setObjectName("global_call")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(450, 223, 260, 41))
        self.label_4.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(130, 220, 200, 40))
        self.label_5.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(780, 223, 330, 40))
        self.label_6.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_6.setObjectName("label_6")
        self.thicknes_calculate = QtWidgets.QPushButton(self.frame)
        self.thicknes_calculate.setGeometry(QtCore.QRect(400, 300, 370, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.thicknes_calculate.setFont(font)
        self.thicknes_calculate.setStyleSheet("QPushButton{\n"
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
        self.thicknes_calculate.setIcon(icon)
        self.thicknes_calculate.setObjectName("thicknes_calculate")
        self.dozimetr_calculate = QtWidgets.QPushButton(self.frame)
        self.dozimetr_calculate.setGeometry(QtCore.QRect(60, 300, 330, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.dozimetr_calculate.setFont(font)
        self.dozimetr_calculate.setStyleSheet("QPushButton{\n"
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
        self.dozimetr_calculate.setIcon(icon)
        self.dozimetr_calculate.setObjectName("dozimetr_calculate")
        self.unit_calculate = QtWidgets.QPushButton(self.frame)
        self.unit_calculate.setGeometry(QtCore.QRect(780, 300, 300, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.unit_calculate.setFont(font)
        self.unit_calculate.setStyleSheet("QPushButton{\n"
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
        self.unit_calculate.setIcon(icon)
        self.unit_calculate.setObjectName("unit_calculate")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(840, 400, 210, 40))
        self.label_7.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_7.setObjectName("label_7")
        self.notes = QtWidgets.QPushButton(self.frame)
        self.notes.setGeometry(QtCore.QRect(780, 470, 300, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.notes.setFont(font)
        self.notes.setStyleSheet("QPushButton{\n"
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
        self.notes.setIcon(icon)
        self.notes.setObjectName("notes")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(80, 400, 300, 40))
        self.label_8.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_8.setObjectName("label_8")
        self.hide_eadiation = QtWidgets.QPushButton(self.frame)
        self.hide_eadiation.setGeometry(QtCore.QRect(400, 470, 370, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.hide_eadiation.setFont(font)
        self.hide_eadiation.setStyleSheet("QPushButton{\n"
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
        self.hide_eadiation.setIcon(icon)
        self.hide_eadiation.setObjectName("hide_eadiation")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(474, 400, 240, 40))
        self.label_9.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_9.setObjectName("label_9")
        self.food_calculate = QtWidgets.QPushButton(self.frame)
        self.food_calculate.setGeometry(QtCore.QRect(60, 470, 330, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.food_calculate.setFont(font)
        self.food_calculate.setStyleSheet("QPushButton{\n"
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
        self.food_calculate.setIcon(icon)
        self.food_calculate.setObjectName("food_calculate")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "2) Как создать укрытие от радиации, укрытия \n"
"           зарегестрированные в программе"))
        self.label_2.setText(_translate("Dialog", "1) Как защитится от радиации?"))
        self.label_3.setText(_translate("Dialog", "     3) Глобальные связи, \n"
"   центр безопастности,"))
        self.hoe_to_create_bunker.setText(_translate("Dialog", "Открыть:"))
        self.how_to_protect.setText(_translate("Dialog", "Открыть:"))
        self.global_call.setText(_translate("Dialog", "Открыть:"))
        self.label_4.setText(_translate("Dialog", "5) Расчет толщины материала \n"
"       для зашиты от радиации"))
        self.label_5.setText(_translate("Dialog", "       4) Дозиметр и др. \n"
"приборы для вычислений"))
        self.label_6.setText(_translate("Dialog", "6) Расчет единиц измерения и их разница, \n"
"       расчет разных типов излучения"))
        self.thicknes_calculate.setText(_translate("Dialog", "Открыть:"))
        self.dozimetr_calculate.setText(_translate("Dialog", "Открыть:"))
        self.unit_calculate.setText(_translate("Dialog", "Открыть:"))
        self.label_7.setText(_translate("Dialog", "9) Ввод и хранение данных:"))
        self.notes.setText(_translate("Dialog", "Открыть:"))
        self.label_8.setText(_translate("Dialog", "7) Расчет уровня радиации в пищевых\n"
"                         продуктах:"))
        self.hide_eadiation.setText(_translate("Dialog", "Открыть:"))
        self.label_9.setText(_translate("Dialog", "8) Нахождение радиации в воде в \n"
"    воздухе а также в почве:"))
        self.food_calculate.setText(_translate("Dialog", "Открыть:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_MoreFunction()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
