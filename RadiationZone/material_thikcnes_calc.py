from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_material_thiknes(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 577)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 721, 531))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; ")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(23, 20, 680, 291))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 11pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(230, 360, 260, 50))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.calk_radiation_protect = QtWidgets.QPushButton(self.widget)
        self.calk_radiation_protect.setGeometry(QtCore.QRect(190, 430, 350, 31))
        self.calk_radiation_protect.setStyleSheet("QPushButton{\n"
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
        self.calk_radiation_protect.setIcon(icon)
        self.calk_radiation_protect.setObjectName("calk_radiation_protect")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Расчет толщины материала для защиты от радиации зависит от нескольких факторов, \n"
"включая тип источника радиации, энергию излучения, тип материала и его плотность. \n"
"\n"
"Для начала необходимо определить, какой тип радиации нужно защититься: альфа-, бета-, \n"
"гамма-излучение или нейтроны. Каждый тип радиации имеет свои характеристики и \n"
"потребует разного подхода к защите.\n"
"\n"
"Для расчета толщины материала для защиты от гамма-излучения можно использовать \n"
"формулу \"закона экспоненциального ослабления\".\n"
"\n"
"Для защиты от бета-излучения можно использовать материалы с высокой плотностью, \n"
"такие как свинец или алюминий.\n"
"\n"
"Для защиты от альфа-излучения используются материалы с высокой плотностью, \n"
"такие как свинец или торий"))
        self.label_2.setText(_translate("Dialog", "Расчет толщины материала для \n"
"      защиты от радиации!"))
        self.calk_radiation_protect.setText(_translate("Dialog", "Открыть"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_material_thiknes()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
