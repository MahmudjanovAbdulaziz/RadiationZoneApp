from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog10(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(775, 423)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(22, 224, 110, 1), stop:0.427447 rgba(127, 224, 22, 1), stop:1 rgba(22, 224, 120, 1));")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 130, 261, 91))
        self.layoutWidget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                        "font: italic 12pt \"Arial\";\n"
                                        "border: 1px solid rgba(255, 255, 255, 40);\n"
                                        "border-radius: 7px;\n"
                                        "")
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.Talas_input = QtWidgets.QLineEdit(self.layoutWidget)
        self.Talas_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                       "color: rgb(249, 19, 219);\n"
                                       "font: italic 12pt \"Arial\";\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 7px;\n"
                                       "")
        self.Talas_input.setObjectName("Talas_input")
        self.verticalLayout_2.addWidget(self.Talas_input)
        self.btn_talas = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_talas.setStyleSheet("QPushButton{\n"
                                     "background-color: rgba(255, 255, 255, 20);\n"
                                     "border: 1px solid rgba(255, 255, 255, 60);\n"
                                     "border-radius: 7px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(255, 255, 255, 40);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::pressed{\n"
                                     "background-color: rgba(128, 249, 255, 60);\n"
                                     "font: italic 13pt \"Arial\";\n"
                                     "}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_talas.setIcon(icon)
        self.btn_talas.setObjectName("btn_talas")
        self.verticalLayout_2.addWidget(self.btn_talas)
        self.layoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 251, 101))
        self.layoutWidget_2.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "font: italic 12pt \"Arial\";\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 7px;\n"
                                          "")
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.Batken_input = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.Batken_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                        "color: rgb(249, 19, 219);\n"
                                        "font: italic 12pt \"Arial\";\n"
                                        "border: 1px solid rgba(255, 255, 255, 40);\n"
                                        "border-radius: 7px;\n"
                                        "")
        self.Batken_input.setObjectName("Batken_input")
        self.verticalLayout_3.addWidget(self.Batken_input)
        self.btn_butken = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btn_butken.setStyleSheet("QPushButton{\n"
                                      "background-color: rgba(255, 255, 255, 20);\n"
                                      "border: 1px solid rgba(255, 255, 255, 60);\n"
                                      "border-radius: 7px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: rgba(255, 255, 255, 40);\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton::pressed{\n"
                                      "background-color: rgba(128, 249, 255, 60);\n"
                                      "font: italic 13pt \"Arial\";\n"
                                      "}")
        self.btn_butken.setIcon(icon)
        self.btn_butken.setObjectName("btn_butken")
        self.verticalLayout_3.addWidget(self.btn_butken)
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(250, 8, 281, 101))
        self.layoutWidget_3.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "font: italic 12pt \"Arial\";\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 7px;\n"
                                          "")
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.osh_input = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.osh_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                     "color: rgb(249, 19, 219);\n"
                                     "font: italic 12pt \"Arial\";\n"
                                     "border: 1px solid rgba(255, 255, 255, 40);\n"
                                     "border-radius: 7px;\n"
                                     "")
        self.osh_input.setObjectName("osh_input")
        self.verticalLayout_4.addWidget(self.osh_input)
        self.btn_osh = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btn_osh.setStyleSheet("QPushButton{\n"
                                   "background-color: rgba(255, 255, 255, 20);\n"
                                   "border: 1px solid rgba(255, 255, 255, 60);\n"
                                   "border-radius: 7px;\n"
                                   "}\n"
                                   "QPushButton:hover{\n"
                                   "background-color: rgba(255, 255, 255, 40);\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton::pressed{\n"
                                   "background-color: rgba(128, 249, 255, 60);\n"
                                   "font: italic 13pt \"Arial\";\n"
                                   "}")
        self.btn_osh.setIcon(icon)
        self.btn_osh.setObjectName("btn_osh")
        self.verticalLayout_4.addWidget(self.btn_osh)
        self.layoutWidget_5 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_5.setGeometry(QtCore.QRect(530, 130, 241, 91))
        self.layoutWidget_5.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "font: italic 12pt \"Arial\";\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 7px;\n"
                                          "")
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_6.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.Naryn_input = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.Naryn_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                       "color: rgb(249, 19, 219);\n"
                                       "font: italic 12pt \"Arial\";\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 7px;\n"
                                       "")
        self.Naryn_input.setObjectName("Naryn_input")
        self.verticalLayout_6.addWidget(self.Naryn_input)
        self.btn_narun = QtWidgets.QPushButton(self.layoutWidget_5)
        self.btn_narun.setStyleSheet("QPushButton{\n"
                                     "background-color: rgba(255, 255, 255, 20);\n"
                                     "border: 1px solid rgba(255, 255, 255, 60);\n"
                                     "border-radius: 7px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: rgba(255, 255, 255, 40);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton::pressed{\n"
                                     "background-color: rgba(128, 249, 255, 60);\n"
                                     "font: italic 13pt \"Arial\";\n"
                                     "}")
        self.btn_narun.setIcon(icon)
        self.btn_narun.setObjectName("btn_narun")
        self.verticalLayout_6.addWidget(self.btn_narun)
        self.layoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(260, 130, 271, 91))
        self.layoutWidget_6.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "font: italic 12pt \"Arial\";\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 7px;\n"
                                          "")
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_6)
        self.label_7.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.Chuy_input = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.Chuy_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                      "color: rgb(249, 19, 219);\n"
                                      "font: italic 12pt \"Arial\";\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 7px;\n"
                                      "")
        self.Chuy_input.setObjectName("Chuy_input")
        self.verticalLayout_7.addWidget(self.Chuy_input)
        self.btn_chuy = QtWidgets.QPushButton(self.layoutWidget_6)
        self.btn_chuy.setStyleSheet("QPushButton{\n"
                                    "background-color: rgba(255, 255, 255, 20);\n"
                                    "border: 1px solid rgba(255, 255, 255, 60);\n"
                                    "border-radius: 7px;\n"
                                    "}\n"
                                    "QPushButton:hover{\n"
                                    "background-color: rgba(255, 255, 255, 40);\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton::pressed{\n"
                                    "background-color: rgba(128, 249, 255, 60);\n"
                                    "font: italic 13pt \"Arial\";\n"
                                    "}")
        self.btn_chuy.setIcon(icon)
        self.btn_chuy.setObjectName("btn_chuy")
        self.verticalLayout_7.addWidget(self.btn_chuy)
        self.layoutWidget_7 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_7.setGeometry(QtCore.QRect(260, 240, 271, 91))
        self.layoutWidget_7.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                          "font: italic 12pt \"Arial\";\n"
                                          "border: 1px solid rgba(255, 255, 255, 40);\n"
                                          "border-radius: 7px;\n"
                                          "")
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_7)
        self.label_8.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                   "font: italic 14pt \"Arial\";\n"
                                   "border: 1px solid rgba(255, 255, 255, 40);\n"
                                   "border-radius: 7px;\n"
                                   "background-color:none;\n"
                                   "border: none;\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.Issuk_kul_input = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.Issuk_kul_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                           "color: rgb(249, 19, 219);\n"
                                           "font: italic 12pt \"Arial\";\n"
                                           "border: 1px solid rgba(255, 255, 255, 40);\n"
                                           "border-radius: 7px;\n"
                                           "")
        self.Issuk_kul_input.setObjectName("Issuk_kul_input")
        self.verticalLayout_8.addWidget(self.Issuk_kul_input)
        self.btn_issyk_kyl = QtWidgets.QPushButton(self.layoutWidget_7)
        self.btn_issyk_kyl.setStyleSheet("QPushButton{\n"
                                         "background-color: rgba(255, 255, 255, 20);\n"
                                         "border: 1px solid rgba(255, 255, 255, 60);\n"
                                         "border-radius: 7px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "background-color: rgba(255, 255, 255, 40);\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton::pressed{\n"
                                         "background-color: rgba(128, 249, 255, 60);\n"
                                         "font: italic 13pt \"Arial\";\n"
                                         "}")
        self.btn_issyk_kyl.setIcon(icon)
        self.btn_issyk_kyl.setObjectName("btn_issyk_kyl")
        self.verticalLayout_8.addWidget(self.btn_issyk_kyl)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(530, 10, 241, 101))
        self.layoutWidget1.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                         "font: italic 12pt \"Arial\";\n"
                                         "border: 1px solid rgba(255, 255, 255, 40);\n"
                                         "border-radius: 7px;\n"
                                         "")
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                 "font: italic 14pt \"Arial\";\n"
                                 "border: 1px solid rgba(255, 255, 255, 40);\n"
                                 "border-radius: 7px;\n"
                                 "background-color:none;\n"
                                 "border: none;\n"
                                 "")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.djalal_abad_input = QtWidgets.QLineEdit(self.layoutWidget1)
        self.djalal_abad_input.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
                                             "color: rgb(249, 19, 219);\n"
                                             "font: italic 12pt \"Arial\";\n"
                                             "border: 1px solid rgba(255, 255, 255, 40);\n"
                                             "border-radius: 7px;\n"
                                             "")
        self.djalal_abad_input.setObjectName("djalal_abad_input")
        self.verticalLayout.addWidget(self.djalal_abad_input)
        self.btn_djalal_abad = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_djalal_abad.setStyleSheet("QPushButton{\n"
                                           "background-color: rgba(255, 255, 255, 20);\n"
                                           "border: 1px solid rgba(255, 255, 255, 60);\n"
                                           "border-radius: 7px;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "background-color: rgba(255, 255, 255, 40);\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton::pressed{\n"
                                           "background-color: rgba(128, 249, 255, 60);\n"
                                           "font: italic 13pt \"Arial\";\n"
                                           "}")
        self.btn_djalal_abad.setIcon(icon)
        self.btn_djalal_abad.setObjectName("btn_djalal_abad")
        self.verticalLayout.addWidget(self.btn_djalal_abad)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/send.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_butken.setIcon(icon1)
        self.btn_issyk_kyl.setIcon(icon1)
        self.btn_djalal_abad.setIcon(icon1)
        self.btn_osh.setIcon(icon1)
        self.btn_chuy.setIcon(icon1)
        self.btn_narun.setIcon(icon1)
        self.btn_talas.setIcon(icon1)

        self.btn_osh.clicked.connect(self.Osh)
        self.btn_butken.clicked.connect(self.Batken)
        self.btn_chuy.clicked.connect(self.Chuy)
        self.btn_narun.clicked.connect(self.Naryn)
        self.btn_talas.clicked.connect(self.Talas)
        self.btn_djalal_abad.clicked.connect(self.djlala_abad)
        self.btn_issyk_kyl.clicked.connect(self.Issyk_Kyl)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "                    Талас"))
        self.btn_talas.setText(_translate("Dialog", "Заменить"))
        self.label_5.setText(_translate("Dialog", "                    Баткен"))
        self.btn_butken.setText(_translate("Dialog", "Заменить"))
        self.label_4.setText(_translate("Dialog", "                         Ош"))
        self.btn_osh.setText(_translate("Dialog", "Заменить"))
        self.label_6.setText(_translate("Dialog", "                  Нарын"))
        self.btn_narun.setText(_translate("Dialog", "Заменить"))
        self.label_7.setText(_translate("Dialog", "                        Чуй"))
        self.btn_chuy.setText(_translate("Dialog", "Заменить"))
        self.label_8.setText(_translate("Dialog", "                 Иссык-Куль"))
        self.btn_issyk_kyl.setText(_translate("Dialog", "Заменить"))
        self.label.setText(_translate("Dialog", "              Джалал-Абад"))
        self.btn_djalal_abad.setText(_translate("Dialog", "Заменить"))

    def Batken(self):
        batken = self.Batken_input.text()

        with open('DataBases/Batken.txt', "w") as batkent:
            batkent.write(batken)
    def Osh(self):
        osh = self.osh_input.text()

        with open('DataBases/Osh.txt', "w") as oshh:
            oshh.write(osh)
    def djlala_abad(self):
        djalal_abad = self.djalal_abad_input.text()

        with open('DataBases/Djalal_Abad.txt', 'w') as d:
            d.write(djalal_abad)

    def Talas(self):
        talas = self.Talas_input.text()

        with open('DataBases/Talas.txt', 'w') as t:
            t.write(talas)

    def Chuy(self):
        chuy = self.Chuy_input.text()

        with open('DataBases/Chuy.txt', 'w') as ch:
            ch.write(chuy)

    def Naryn(self):
        naryn = self.Naryn_input.text()

        with open('DataBases/Naryn.txt', 'w') as n:
            n.write(naryn)

    def Issyk_Kyl(self):
        Issyk = self.Issuk_kul_input.text()

        with open('DataBases/Isik_Kul.txt', 'w') as Is:
            Is.write(Issyk)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog10()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
