from PyQt5 import QtCore, QtGui, QtWidgets
from filters_masks import Ui_filter_masks

class Ui_how_to_protect_tadiation(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(785, 578)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 26, 731, 531))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.radiation_elements = QtWidgets.QPushButton(self.frame)
        self.radiation_elements.setGeometry(QtCore.QRect(20, 350, 220, 23))
        self.radiation_elements.setStyleSheet("QPushButton{\n"
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
        self.radiation_elements.setIcon(icon)
        self.radiation_elements.setObjectName("radiation_elements")
        self.rad_map = QtWidgets.QPushButton(self.frame)
        self.rad_map.setGeometry(QtCore.QRect(250, 350, 240, 23))
        self.rad_map.setStyleSheet("QPushButton{\n"
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
        self.rad_map.setObjectName("rad_map")
        self.rad_protect = QtWidgets.QPushButton(self.frame)
        self.rad_protect.setGeometry(QtCore.QRect(500, 350, 210, 23))
        self.rad_protect.setStyleSheet("QPushButton{\n"
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
        self.rad_protect.setObjectName("rad_protect")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 290, 230, 40))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(300, 290, 160, 41))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(510, 290, 190, 41))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 410, 180, 41))
        self.label_4.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(260, 410, 210, 41))
        self.label_5.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_5.setObjectName("label_5")
        self.filter_and_mask = QtWidgets.QPushButton(self.frame)
        self.filter_and_mask.setGeometry(QtCore.QRect(250, 470, 240, 23))
        self.filter_and_mask.setStyleSheet("QPushButton{\n"
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
        self.filter_and_mask.setObjectName("filter_and_mask")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(520, 410, 170, 41))
        self.label_6.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.you_are_seck = QtWidgets.QPushButton(self.frame)
        self.you_are_seck.setGeometry(QtCore.QRect(500, 470, 210, 23))
        self.you_are_seck.setStyleSheet("QPushButton{\n"
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
        self.you_are_seck.setObjectName("you_are_seck")
        self.how_protect_sun_red = QtWidgets.QPushButton(self.frame)
        self.how_protect_sun_red.setGeometry(QtCore.QRect(20, 470, 220, 23))
        self.how_protect_sun_red.setStyleSheet("QPushButton{\n"
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
        self.how_protect_sun_red.setObjectName("how_protect_sun_red")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 10, 1360, 250))
        self.label_7.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.radiation_elements.setText(_translate("Dialog", "Открыть."))
        self.rad_map.setText(_translate("Dialog", "Открыть."))
        self.rad_protect.setText(_translate("Dialog", "Открыть."))
        self.label.setText(_translate("Dialog", "1) Радиоактивные элементы \n"
"             и их свойства."))
        self.label_2.setText(_translate("Dialog", "2) Карта радиации:"))
        self.label_3.setText(_translate("Dialog", "3) Методы защиты от\n"
"             радиации:"))
        self.label_4.setText(_translate("Dialog", "4)  Kaк защетится от \n"
"  солнечной  радиации?"))
        self.label_5.setText(_translate("Dialog", "5) Типы фильтров и масок \n"
"             для защиты:"))
        self.filter_and_mask.setText(_translate("Dialog", "Открыть."))
        self.label_6.setText(_translate("Dialog", "6) Узнать зыражен ли \n"
"       ты радиацией?"))
        self.you_are_seck.setText(_translate("Dialog", "Открыть."))
        self.how_protect_sun_red.setText(_translate("Dialog", "Открыть."))
        self.label_7.setText(_translate("Dialog", "1) Избегать пребывания в зоне радиационного загрязнения. Если попадание в такую \n"
"зону неизбежно, то необходимо максимально быстро покинуть ее.\n"
"\n"
"2) Использовать средства индивидуальной защиты. Наиболее эффективными \n"
"являются противогазы, защитные костюмы и специальные маски.\n"
"\n"
"3) Питаться правильно. Необходимо употреблять продукты, богатые антиоксидантами, \n"
"такими как фрукты, овощи и зелень. Они помогают организму бороться с \n"
"радикалами и уменьшают вредное воздействие радиации на клетки.\n"
"\n"
"4) Пить много жидкости. При воздействии радиации на организм возможно развитие \n"
"отеков и проблем с почками. я на здоровье и усугубить последствия радиации."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_how_to_protect_tadiation()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
