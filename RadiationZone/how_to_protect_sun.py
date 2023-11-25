from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_how_to_protect_sun(object):
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
        self.label.setText(_translate("Dialog", "Избегайте нахождения на солнце во время пиковой \n"
"интенсивности солнечных лучей, которые обычно \n"
"приходятся на период с 10 утра до 4 вечера.\n"
"\n"
"Носите защитную одежду, закрывающую большую \n"
"часть тела. Это может быть широкополая шляпа, \n"
"рубашка с длинными рукавами, брюки и т.д.\n"
"\n"
"Используйте солнцезащитный крем с SPF \n"
"(защитным фактором) не менее 30. Наносите крем \n"
"на все открытые участки кожи, не забывая про \n"
"уши, затылок и губы\n"
"\n"
"Носите солнцезащитные очки, которые защитят \n"
"ваши глаза от вредных ультрафиолетовых лучей.\n"
"\n"
"Избегайте нахождения на открытом воздухе на \n"
"длительное время. Если вы не можете избежать \n"
"этого, то старайтесь укрыться в тени.\n"
"\n"
"Пейте достаточно жидкости, чтобы избежать \n"
"обезвоживания, которое может усугубить \n"
"воздействие солнечных лучей.\n"
"\n"
"Если вы ощущаете признаки солнечного удара \n"
"(головокружение, тошноту, слабость), сразу же \n"
"ищите прохладное место и пейте больше жидкости."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_how_to_protect_sun()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
