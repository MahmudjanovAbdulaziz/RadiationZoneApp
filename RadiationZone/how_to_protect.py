from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_how_to_protect(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 640)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 460, 611))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 591))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Укрытие: в случае ядерной войны или аварии на \n"
"атомной станции, укрытие может предоставить \n"
"защиту от радиации. Укрытие должно быть \n"
"расположено под землей или защищено толстыми \n"
"стенами, чтобы минимизировать воздействие \n"
"радиации.\n"
"\n"
"Изоляция: в некоторых случаях, например, при \n"
"медицинском облучении, можно использовать \n"
"защитную одежду или другие материалы, чтобы \n"
"изолировать тело от радиации.\n"
"\n"
"Дистанцирование: чем дальше от источника радиации, \n"
"тем меньше радиации вы получите. Поэтому, если \n"
"возможно, важно оставаться на безопасном \n"
"расстоянии от источника радиации.\n"
"\n"
"Применение противорадиационных лекарств: эти \n"
"лекарства могут помочь защитить организм от \n"
"радиации или помочь восстановить ткани, которые \n"
"были повреждены излучением.\n"
"\n"
"Использование фильтров и абсорберов: фильтры и \n"
"абсорберы могут помочь уменьшить уровень \n"
"радиации в воздухе или воде, что позволит \n"
"уменьшить риск радиационного воздействия.\n"
"\n"
"Использование дозиметров: дозиметры помогают \n"
"измерить уровень радиации "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_how_to_protect()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
