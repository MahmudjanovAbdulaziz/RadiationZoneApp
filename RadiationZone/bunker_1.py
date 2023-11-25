from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bunker_1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(365, 198)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 340, 170))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; ")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 28, 270, 50))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(30, 100, 280, 21))
        self.comboBox.setStyleSheet("QComboBox {\n"
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
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "В базе данных на данный момент \n"
"            укрытия отсуствуют!"))
        self.comboBox.setItemText(0, _translate("Dialog", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_bunker_1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
