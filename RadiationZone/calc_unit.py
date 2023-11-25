from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calc_unite(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(770, 584)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 20, 711, 541))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 30, 681, 261))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 340, 260, 40))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.radiation_converter = QtWidgets.QPushButton(self.widget)
        self.radiation_converter.setGeometry(QtCore.QRect(20, 400, 320, 31))
        self.radiation_converter.setStyleSheet("QPushButton{\n"
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
        self.radiation_converter.setIcon(icon)
        self.radiation_converter.setObjectName("radiation_converter")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(370, 340, 300, 40))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.calc_alpa_beta_gamma = QtWidgets.QPushButton(self.widget)
        self.calc_alpa_beta_gamma.setGeometry(QtCore.QRect(370, 400, 320, 31))
        self.calc_alpa_beta_gamma.setStyleSheet("QPushButton{\n"
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
        self.calc_alpa_beta_gamma.setIcon(icon)
        self.calc_alpa_beta_gamma.setObjectName("calc_alpa_beta_gamma")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Альфа, бета и гамма излучения - это различные типы радиоактивного излучения. \n"
"\n"
"Альфа-излучение - это поток частиц альфа, состоящих из двух \n"
"\n"
"протонов и двух нейтронов. Бета-излучение - это поток электронов или позитронов. \n"
"\n"
"Гамма-излучение - это высокочастотные электромагнитные волны. Каждый тип \n"
"\n"
"излучения имеет свои особенности, включая способность проникать через различные \n"
"\n"
"материалы и воздействовать на живые организмы."))
        self.label_2.setText(_translate("Dialog", "Конвертер разных ед. измерения\n"
"                      радиации:"))
        self.radiation_converter.setText(_translate("Dialog", "Открыть:"))
        self.label_3.setText(_translate("Dialog", "Вычисления \"альфа\", \"бета\", \"гамма\" - \n"
"                           излучений:"))
        self.calc_alpa_beta_gamma.setText(_translate("Dialog", "Открыть:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Calc_unite()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
