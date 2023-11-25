from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_filter_masks(object):
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
        self.label.setGeometry(QtCore.QRect(19, 20, 441, 411))
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
        self.label.setText(_translate("Dialog", "Маски N95 и N100 - эти маски имеют фильтры, \n"
"которые могут задерживать частицы размером от \n"
"0,3 до 0,5 микрон. Они эффективны при защите от \n"
"радиоактивных частиц, таких как ядерная пыль.\n"
"\n"
"Маски с активированным углем - такие маски имеют \n"
"угольный фильтр, который может поглощать \n"
"некоторые радиоактивные частицы и газы.\n"
"\n"
"Фильтры HEPA - это фильтры, которые могут \n"
"задерживать частицы размером до 0,3 микрона. Они \n"
"могут быть использованы для защиты от \n"
"радиоактивных частиц.\n"
"\n"
"Противогазы - это маски, которые имеют фильтры, \n"
"способные задерживать радиоактивные частицы и \n"
"газы. Они также могут быть эффективны при защите \n"
"от взрывов ядерных бомб.\n"
"\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_filter_masks()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
