from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

conn = sqlite3.connect('SignInDataBases/users.db')
c = conn.cursor()
c.execute("SELECT username FROM users")
result = c.fetchone()

class Ui_Dialog9(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(781, 600)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 30, 721, 531))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"font: italic 12pt \"Arial\";")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 400, 631, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setStyleSheet("QLabel{\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-raidius: 7px;\n"
"font: italic 12t \"Arial\";\n"
"}\n"
"\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.new_location_chenche = QtWidgets.QPushButton(self.layoutWidget)
        self.new_location_chenche.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 11pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgba(255, 255, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 50);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(140, 250, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 60);\n"
"border-radius: 7 px;\n"
"font: italic 13pt \"Arial\";\n"
"}")
        self.new_location_chenche.setObjectName("open_RadiationZone")
        self.verticalLayout_4.addWidget(self.new_location_chenche)
        self.layoutWidget1 = QtWidgets.QWidget(self.frame)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 90, 631, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("QLabel{\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-raidius: 7px;\n"
"font: italic 12t \"Arial\";\n"
"}\n"
"\n"
"")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.change_radiation = QtWidgets.QPushButton(self.layoutWidget1)
        self.change_radiation.setEnabled(True)
        self.change_radiation.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 11pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgba(255, 255, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 50);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(140, 250, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 60);\n"
"border-radius: 7 px;\n"
"font: italic 13pt \"Arial\";\n"
"}")
        self.change_radiation.setObjectName("change_radiation")
        self.verticalLayout.addWidget(self.change_radiation)
        self.layoutWidget2 = QtWidgets.QWidget(self.frame)
        self.layoutWidget2.setGeometry(QtCore.QRect(50, 190, 631, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setStyleSheet("QLabel{\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-raidius: 7px;\n"
"font: italic 12t \"Arial\";\n"
"}\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.open_weather = QtWidgets.QPushButton(self.layoutWidget2)
        self.open_weather.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 11pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgba(255, 255, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 50);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(140, 250, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 60);\n"
"border-radius: 7 px;\n"
"font: italic 13pt \"Arial\";\n"
"}")
        self.open_weather.setObjectName("open_weather")
        self.verticalLayout_2.addWidget(self.open_weather)
        self.layoutWidget3 = QtWidgets.QWidget(self.frame)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 290, 631, 91))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_3.setStyleSheet("QLabel{\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-raidius: 7px;\n"
"font: italic 12t \"Arial\";\n"
"}\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.call_MCHS = QtWidgets.QPushButton(self.layoutWidget3)
        self.call_MCHS.setStyleSheet("QPushButton{\n"
"background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 11pt \"Arial\";\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgba(255, 255, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 50);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QPushButton::pressed{\n"
"background-color:rgba(140, 250, 255, 30) ;\n"
"border: 1 pt solid rgba(255, 255, 255, 60);\n"
"border-radius: 7 px;\n"
"font: italic 13pt \"Arial\";\n"
"}")
        self.call_MCHS.setObjectName("call_MCHS")
        self.verticalLayout_3.addWidget(self.call_MCHS)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(80, 30, 281, 31))
        self.label_5.setStyleSheet("background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.researches_name = QtWidgets.QLabel(self.frame)
        self.researches_name.setGeometry(QtCore.QRect(360, 30, 281, 31))
        self.researches_name.setStyleSheet("background-color: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 40);\n"
"border-radius: 7 px;\n"
"font: italic 12pt \"Arial\";")
        self.researches_name.setText("")
        self.researches_name.setObjectName("researches_name")

        self.result = result

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.researches_name.setText(self.result[0])

        self.open_weather.clicked.connect(self.open_weather_prognoz)
        self.call_MCHS.clicked.connect(self.open_mchs)





    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Administrator"))
        self.label_4.setText(_translate("Dialog", "                                                               Ввести данные..."))
        self.new_location_chenche.setText(_translate("Dialog", "Открыть"))
        self.label.setText(_translate("Dialog", "                                                     Поменять значение радиации:"))
        self.change_radiation.setText(_translate("Dialog", "Открыть"))
        self.label_2.setText(_translate("Dialog", "                                                    Открыть прогноз погоды:"))
        self.open_weather.setText(_translate("Dialog", "Открыть"))
        self.label_3.setText(_translate("Dialog", "                                                                 Позвонить МЧС:"))
        self.call_MCHS.setText(_translate("Dialog", "Открыть"))
        self.label_5.setText(_translate("Dialog", "Добро пожаловать исследователь:"))

    def open_mchs(self):
        mchs_url = QUrl('https://web.whatsapp.com/send?phone=996556112000')
        QDesktopServices.openUrl(mchs_url)

    def open_weather_prognoz(self):
        wether_url = QUrl('https://ru.meteotrend.com/')
        QDesktopServices.openUrl(wether_url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog9()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
