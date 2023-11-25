from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_calc_instruments(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(762, 579)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 721, 541))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 21, 681, 340))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 390, 140, 21))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.geyger = QtWidgets.QPushButton(self.widget)
        self.geyger.setGeometry(QtCore.QRect(20, 430, 200, 21))
        self.geyger.setStyleSheet("QPushButton{\n"
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
        self.geyger.setIcon(icon)
        self.geyger.setObjectName("geyger")
        self.dozimetr = QtWidgets.QPushButton(self.widget)
        self.dozimetr.setGeometry(QtCore.QRect(260, 430, 209, 21))
        self.dozimetr.setStyleSheet("QPushButton{\n"
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
        self.dozimetr.setIcon(icon)
        self.dozimetr.setObjectName("dozimetr")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(320, 390, 90, 21))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.spektrometr = QtWidgets.QPushButton(self.widget)
        self.spektrometr.setGeometry(QtCore.QRect(500, 430, 200, 21))
        self.spektrometr.setStyleSheet("QPushButton{\n"
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
        self.spektrometr.setIcon(icon)
        self.spektrometr.setObjectName("spektrometr")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(540, 390, 120, 21))
        self.label_4.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Способ измерения радиации: Как вы видите я привел три счетчика для измерения \n"
"радиации каждый из них имеет свой функционал и вы полноправно способны \n"
"использовать эти счетчики для своих расчетов:\n"
"Коротко о счетчиках:\n"
"\n"
"Гейгер-счетчик: это портативное устройство, которое используется \n"
"для обнаружения и измерения уровня радиации. Гейгер-счетчик \n"
"обнаруживает радиоактивность путем измерения ионизирующей способности воздуха.\n"
"\n"
"Дозиметр: это устройство для измерения дозы радиации. Дозиметр используется \n"
"для определения дозы радиации, которая поглощается человеком в течение \n"
"определенного периода времени.\n"
"\n"
"Спектрометр: это прибор, который позволяет анализировать спектр радиоактивности. \n"
"Спектрометр используется для определения типа радиоактивного материала и \n"
"его концентрации в образце."))
        self.label_2.setText(_translate("Dialog", "Счетчик Гейгера:"))
        self.geyger.setText(_translate("Dialog", "Открыть"))
        self.dozimetr.setText(_translate("Dialog", "Открыть"))
        self.label_3.setText(_translate("Dialog", "Дозиметр:"))
        self.spektrometr.setText(_translate("Dialog", "Открыть"))
        self.label_4.setText(_translate("Dialog", "Спектрометр:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_calc_instruments()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
