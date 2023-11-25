from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class chenge_New_Local(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(446, 328)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(22, 224, 110, 1), stop:0.427447 rgba(127, 224, 22, 1), stop:1 rgba(22, 224, 120, 1));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 40, 311, 20))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: italic 13pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"background-color:none;\n"
"border: none;\n"
"")
        self.label.setObjectName("label")
        self.city_input = QtWidgets.QLineEdit(Dialog)
        self.city_input.setGeometry(QtCore.QRect(30, 80, 391, 23))
        self.city_input.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(249, 19, 219);\n"
"font: italic 12pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}")
        self.city_input.setObjectName("Batken_input_2")
        self.send_btn = QtWidgets.QPushButton(Dialog)
        self.send_btn.setGeometry(QtCore.QRect(30, 220, 391, 31))
        self.send_btn.setStyleSheet("QPushButton{\n"
"font: italic 11pt \"Arial\";\n"
"background-color: rgba(255, 255, 255, 20);\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color: rgba(128, 249, 255, 60);\n"
"font: italic 13pt \"Arial\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_btn.setIcon(icon)
        self.send_btn.setObjectName("btn_butken")
        self.radiation_line_inp = QtWidgets.QLineEdit(Dialog)
        self.radiation_line_inp.setGeometry(QtCore.QRect(30, 160, 391, 23))
        self.radiation_line_inp.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(249, 19, 219);\n"
"font: italic 12pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"border: 1px solid rgba(255, 255, 255, 50);\n"
"border-radius: 7px;\n"
"}")
        self.radiation_line_inp.setObjectName("Batken_input_3")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 311, 20))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: italic 13pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"background-color:none;\n"
"border: none;\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.send_btn.clicked.connect(self.send)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ввод данных"))
        self.label.setText(_translate("Dialog", "Введите название города или района:"))
        self.send_btn.setText(_translate("Dialog", "Применить"))
        self.label_2.setText(_translate("Dialog", "        Кол-во радиации в МкР/ч:"))

    def send(self):
        city = self.city_input.text()
        radiation = self.radiation_line_inp.text()

        with open('DataBases/local.txt', 'w') as l:
            l.write(city)

        with open('DataBases/radiation_unit.txt', 'w') as r:
            r.write(radiation)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = chenge_New_Local()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
