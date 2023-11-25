from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_radaition_in_water(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(764, 574)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 30, 711, 511))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 50, 671, 280))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.searche_radaition_water_and = QtWidgets.QPushButton(self.widget)
        self.searche_radaition_water_and.setGeometry(QtCore.QRect(200, 420, 320, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.searche_radaition_water_and.setFont(font)
        self.searche_radaition_water_and.setStyleSheet("QPushButton{\n"
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
        self.searche_radaition_water_and.setIcon(icon)
        self.searche_radaition_water_and.setObjectName("searche_radaition_water_and")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(280, 360, 150, 30))
        self.label_11.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Радиация может быть обнаружена в земле, воде и почве. \n"
"\n"
"В земле и почве радиоактивные элементы могут быть естественным образом или быть \n"
"следствием человеческой деятельности, такой как ядерные испытания или \n"
"аварии на атомных электростанциях. Радиоактивные вещества могут также \n"
"находиться в воде, особенно в подземных источниках. \n"
"\n"
"Измерение радиации в этих средах проводится при помощи специальных приборов, \n"
"таких как радиометры и дозиметры. \n"
"\n"
"Определенные уровни радиации в земле, воде и почве могут быть \n"
"безопасными, но в случае превышения допустимых норм, необходимо \n"
"предпринимать меры для защиты здоровья людей и окружающей среды."))
        self.searche_radaition_water_and.setText(_translate("Dialog", "Открыть:"))
        self.label_11.setText(_translate("Dialog", "Найти радиацию:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_radaition_in_water()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
