from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser


class Ui_global_calls(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(776, 566)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 731, 521))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(20, 20, 690, 291))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(79, 370, 230, 31))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_2.setObjectName("label_2")
        self.call_MCHS = QtWidgets.QPushButton(self.widget)
        self.call_MCHS.setGeometry(QtCore.QRect(26, 430, 320, 21))
        self.call_MCHS.setStyleSheet("QPushButton{\n"
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
        self.call_MCHS.setIcon(icon)
        self.call_MCHS.setObjectName("call_MCHS")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(470, 370, 170, 31))
        self.label_3.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_3.setObjectName("label_3")
        self.extra_calls = QtWidgets.QPushButton(self.widget)
        self.extra_calls.setGeometry(QtCore.QRect(386, 430, 320, 21))
        self.extra_calls.setStyleSheet("QPushButton{\n"
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
        self.extra_calls.setIcon(icon)
        self.extra_calls.setObjectName("extra_calls")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.call_MCHS.clicked.connect(self.openMCHS)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Глобальные связи это место где вы можете зайти ватсап номер или так же через\n"
" ватсап выбрать одну из служб экстренной помощи. \n"
"Узнаем что такое МЧС:\n"
"\n"
"МЧС означает Министерство по чрезвычайным ситуациям. Это государственный \n"
"орган, который отвечает за координацию действий по предотвращению и ликвидации \n"
"чрезвычайных ситуаций.  \n"
"\n"
"Узнаем что такое Экстренные звонки:\n"
"\n"
"Экстренные звонки - это звонки, которые совершаются для вызова экстренных \n"
"служб в случае возникновения чрезвычайных ситуаций, требующих немедленного \n"
"вмешательства. К таким службам могут относиться полиция, скорая медицинская \n"
"помощь, пожарная служба, спасательные службы и другие. "))
        self.label_2.setText(_translate("Dialog", "Центр безопастности МЧС"))
        self.call_MCHS.setText(_translate("Dialog", "Открыть"))
        self.label_3.setText(_translate("Dialog", "Экстренные звонки:"))
        self.extra_calls.setText(_translate("Dialog", "Открыть"))

    def openMCHS(self):
        url = "https://web.whatsapp.com/send?phone=996556112000"
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_global_calls()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
