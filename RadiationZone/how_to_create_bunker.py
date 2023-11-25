from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser

class Ui_how_to_create_bunker(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(776, 590)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(30, 20, 721, 541))
        self.frame.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px; ")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 20, 701, 261))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 10pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 340, 220, 40))
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.bunker_1 = QtWidgets.QPushButton(self.frame)
        self.bunker_1.setGeometry(QtCore.QRect(30, 430, 201, 21))
        self.bunker_1.setStyleSheet("QPushButton{\n"
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
        self.bunker_1.setIcon(icon)
        self.bunker_1.setObjectName("bunker_1")
        self.bunker_2 = QtWidgets.QPushButton(self.frame)
        self.bunker_2.setGeometry(QtCore.QRect(260, 430, 210, 21))
        self.bunker_2.setStyleSheet("QPushButton{\n"
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
        self.bunker_2.setIcon(icon)
        self.bunker_2.setObjectName("bunker_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(280, 340, 170, 40))
        self.label_3.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.bunker_radiation_calk = QtWidgets.QPushButton(self.frame)
        self.bunker_radiation_calk.setGeometry(QtCore.QRect(500, 430, 201, 21))
        self.bunker_radiation_calk.setStyleSheet("QPushButton{\n"
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
        self.bunker_radiation_calk.setIcon(icon)
        self.bunker_radiation_calk.setObjectName("bunker_radiation_calk")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(490, 320, 220, 80))
        self.label_4.setStyleSheet("QLabel{\n"
"background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"border: 1 pt solid rgba(255, 255, 255, 90);\n"
"border-radius: 7 px;\n"
"}")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.bunker_2.clicked.connect(self.openradiation_catastrof)



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Определите оптимальное местоположение. Укрытие должно находиться в месте, где вероятность\n"
" попадания радиоактивных частиц минимальна. Лучше всего выбрать место вдали от \n"
"ядерных объектов, на высоком месте, чтобы избежать попадания радиоактивных частиц, \n"
"которые могут оседать на земле. Также необходимо учитывать, что на расстоянии 10-20 км от \n"
"ядерного взрыва может произойти волна электромагнитного излучения, способная повредить электронику, \n"
"поэтому лучше выбрать место, где есть естественный укрытие, например, пещеру или подвал.\n"
"\n"
"Подготовьте необходимые материалы. Для создания укрытия вам потребуется достаточное количество \n"
"материалов, которые помогут защитить вас от радиации. К таким материалам относятся: плотные \n"
"материалы, такие как бетон, свинец, сталь; материалы с высокой плотностью, например, \n"
"глина, песок, кирпич; материалы для герметизации, такие как ленты для уплотнения, \n"
"силиконовый герметик, монтажная пена.Создайте структуру укрытия. Структуру укрытия можно \n"
"создать из бетона, металла или других плотных материалов. Необходимо создать стенки, \n"
"потолок и пол, которые будут иметь достаточную плотность, чтобы остановить \n"
"радиационные частицы."))
        self.label_2.setText(_translate("Dialog", "Списки укрытий созданных \n"
"        на данный момент:"))
        self.bunker_1.setText(_translate("Dialog", "Открыть"))
        self.bunker_2.setText(_translate("Dialog", "Открыть"))
        self.label_3.setText(_translate("Dialog", "Списки радиационных \n"
"               аварий:"))
        self.bunker_radiation_calk.setText(_translate("Dialog", "Открыть"))
        self.label_4.setText(_translate("Dialog", "Сделайть расчет времени \n"
"при котором можно \n"
"оставаться в укрытии для \n"
"избежания радиации:"))
    def openradiation_catastrof(self):
        url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%80%D0%B0%D0%B4%D0%B8%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85_%D0%B0%D0%B2%D0%B0%D1%80%D0%B8%D0%B9'
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_how_to_create_bunker()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
