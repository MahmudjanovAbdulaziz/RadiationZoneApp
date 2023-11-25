from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
from about_as import Ui_Dialog2
from graf import Ui_Dialog4
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog
import sqlite3




class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1247, 775)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(420, -1, 500, 711))
        self.frame.setStyleSheet("background-color: rgb(124, 253, 255);\n"
                                 "border-radius: 100px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(80, 30, 361, 51))
        self.label.setStyleSheet("font: 75 14pt \"Arial\";")
        self.label.setObjectName("label")
        self.input_line = QtWidgets.QLineEdit(self.frame)
        self.input_line.setGeometry(QtCore.QRect(70, 80, 291, 31))
        self.input_line.setStyleSheet("color: rgb(0, 255, 0);\n"
                                      "font: 14pt \"Arial\";\n"
                                      "background-color: rgb(170, 255, 255);\n"
                                      "")
        self.input_line.setObjectName("input_line")
        self.input_line.textChanged.connect(self.radiation_input_)
        self.btn_search = QtWidgets.QPushButton(self.frame)
        self.btn_search.setGeometry(QtCore.QRect(380, 80, 91, 31))
        self.btn_search.setStyleSheet("font: 75 36pt \"Arial\";\n"
                                      "color: rgb(0, 255, 8);")
        self.btn_search.setObjectName("btn_search")
        self.btn_search.clicked.connect(self.searche_radiation)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 41, 20))
        self.label_3.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 210, 81, 20))
        self.label_5.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(50, 240, 51, 20))
        self.label_6.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(50, 270, 121, 20))
        self.label_7.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_7.setObjectName("label_7")
        self.calculate = QtWidgets.QPushButton(self.frame)
        self.calculate.setGeometry(QtCore.QRect(30, 640, 441, 41))
        self.calculate.setStyleSheet("font: 14pt \"Arial\";\n"
                                     "color: rgb(15, 255, 91);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/add_circle_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.calculate.setIcon(icon)
        self.calculate.setObjectName("calculate")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 180, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.azot = QtWidgets.QLabel(self.frame)
        self.azot.setGeometry(QtCore.QRect(100, 181, 47, 20))
        self.azot.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";")
        self.azot.setObjectName("azot")
        self.cislorod = QtWidgets.QLabel(self.frame)
        self.cislorod.setGeometry(QtCore.QRect(130, 210, 47, 16))
        self.cislorod.setStyleSheet("font: italic 10pt \"Arial\";")
        self.cislorod.setObjectName("cislorod")
        self.argon = QtWidgets.QLabel(self.frame)
        self.argon.setGeometry(QtCore.QRect(110, 240, 47, 21))
        self.argon.setStyleSheet("font: italic 10pt \"Arial\";")
        self.argon.setObjectName("argon")
        self.carbon_dioxid = QtWidgets.QLabel(self.frame)
        self.carbon_dioxid.setGeometry(QtCore.QRect(170, 270, 47, 20))
        self.carbon_dioxid.setStyleSheet("font: italic 10pt \"Arial\";")
        self.carbon_dioxid.setObjectName("carbon_dioxid")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(50, 150, 181, 21))
        self.label_8.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_8.setObjectName("label_8")
        self.radiation = QtWidgets.QLabel(self.frame)
        self.radiation.setGeometry(QtCore.QRect(150, 340, 300, 20))
        self.radiation.setStyleSheet("font: italic 10pt \"Arial\";")
        self.radiation.setText("")
        self.radiation.setObjectName("radiation")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(0, 300, 501, 20))
        self.label_10.setObjectName("label_10")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(260, 150, 161, 21))
        self.label_13.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setGeometry(QtCore.QRect(260, 180, 161, 41))
        self.label_14.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(420, 190, 31, 41))
        self.label_15.setStyleSheet("font: italic 10pt \"Arial\";")
        self.label_15.setObjectName("label_15")
        self.btn_admin = QtWidgets.QPushButton(self.frame)
        self.btn_admin.setGeometry(QtCore.QRect(0, 520, 91, 61))
        self.btn_admin.setStyleSheet("")
        self.btn_admin.setText("")
        self.btn_admin.setObjectName("btn_admin")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(50, 340, 91, 21))
        self.label_9.setStyleSheet("font: italic 13pt \"Arial\";")
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(0, 120, 501, 20))
        self.label_11.setObjectName("label_11")

        self.radiation_Koeficent = QtWidgets.QPushButton(self.centralwidget)
        self.radiation_Koeficent.setEnabled(True)
        self.radiation_Koeficent.setGeometry(QtCore.QRect(61, 132, 351, 31))
        self.radiation_Koeficent.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                      "border: 1px solid rgba(255, 255, 255, 40);\n"
                                      "border-radius: 7px;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/publick_off.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiation_Koeficent.setIcon(icon1)
        self.radiation_Koeficent.setObjectName("avary_list")
        self.btn_calculator = QtWidgets.QPushButton(self.centralwidget)
        self.btn_calculator.setGeometry(QtCore.QRect(930, 116, 121, 41))
        self.btn_calculator.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                    "border: 1px solid(255, 255, 255, 40);\n"
                                    "border-radius:7px;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/calculator.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_calculator.setIcon(icon2)
        self.btn_calculator.setObjectName("calendar")
        self.viktorino = QtWidgets.QPushButton(self.centralwidget)
        self.viktorino.setGeometry(QtCore.QRect(930, 164, 121, 41))
        self.viktorino.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                     "border: 1px solid(255, 255, 255, 40);\n"
                                     "border-radius:7px;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/quiz.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viktorino.setIcon(icon3)
        self.viktorino.setObjectName("viktorino")
        self.viktorino.clicked.connect(self.open_whatsapp)
        self.graf = QtWidgets.QPushButton(self.centralwidget)
        self.graf.setGeometry(QtCore.QRect(930, 212, 111, 41))
        self.graf.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                "border: 1px solid(255, 255, 255, 40);\n"
                                "border-radius:7px;")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/monitoring.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.graf.setIcon(icon4)
        self.graf.setObjectName("graf")
        self.about_as = QtWidgets.QPushButton(self.centralwidget)
        self.about_as.setGeometry(QtCore.QRect(930, 260, 71, 41))
        self.about_as.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                        "border: 1px solid(255, 255, 255, 40);\n"
                                        "border-radius:7px;")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/help.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.about_as.setIcon(icon5)
        self.about_as.setObjectName("pushButton_5")
        self.hide_polution = QtWidgets.QPushButton(self.centralwidget)
        self.hide_polution.setEnabled(True)
        self.hide_polution.setGeometry(QtCore.QRect(61, 180, 351, 31))
        self.hide_polution.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                       "border: 1px solid rgba(255, 255, 255, 40);\n"
                                       "border-radius: 7px;")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/group_add_FILL0_wght400_GRAD0_opsz48.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hide_polution.setIcon(icon6)
        self.hide_polution.setObjectName("online_chat")
        self.additional_features = QtWidgets.QPushButton(self.centralwidget)
        self.additional_features.setEnabled(True)
        self.additional_features.setGeometry(QtCore.QRect(61, 228, 351, 31))
        self.additional_features.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                     "border: 1px solid rgba(255, 255, 255, 40);\n"
                                     "border-radius: 7px;")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/support-agent.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.additional_features.setIcon(icon7)
        self.additional_features.setObjectName("mchs_call")
        self.radiation_function = QtWidgets.QPushButton(self.centralwidget)
        self.radiation_function.setEnabled(True)
        self.radiation_function.setGeometry(QtCore.QRect(61, 276, 351, 31))
        self.radiation_function.setStyleSheet("background-color: rgb(255, 255, 255, 30); font: italic 10pt \"Arial\";\n"
                                           "border: 1px solid rgba(255, 255, 255, 40);\n"
                                           "border-radius: 7px;")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/oil.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.radiation_function.setIcon(icon8)
        self.radiation_function.setObjectName("radiation_about")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.radiation_input = ''
        self.osh = '0.17Mk'
        self.bishkek = '25мР/ч'
        self.batken = '0,13mk'
        self.djalal_abad = '0,17mk'
        self.naryn = '0,19mk'
        self.talas = '0.18Mk'
        self.issik_kul = '0.17mk'
        self.chuy = '0.19'
        self.kyrgyzstan = '17-60мР/ч'
        self.else_ = 'Неправильный запрос!'
        self.cyti = '0'
        self.radiation_num = None
        self.calculate.clicked.connect(open_window)
        self.about_as.clicked.connect(open_about_as)
        self.graf.clicked.connect(open_graf)

        # admin open chercters and veriables
        with open("DataBases/batken.txt", 'r') as b:
            Batkent = b.read().strip()
            self.batken = Batkent + 'Mr/H'

        with open("DataBases/Osh.txt", 'r') as o:
            Osh = o.read().strip()
            self.osh = Osh+ 'Mr/H'

        with open("DataBases/Djalal_Abad.txt", 'r') as dj:
            Djalal_Abad = dj.read().strip()
            self.djalal_abad = Djalal_Abad+ 'Mr/H'

        with open("DataBases/Talas.txt", 'r') as t:
            Talas = t.read().strip()
            self.talas = Talas + 'Mr/H'

        with open("DataBases/Chuy.txt", 'r') as ch:
            Chuy = ch.read().strip()
            self.chuy = Chuy+ 'Mr/H'

        with open("DataBases/Naryn.txt", 'r') as n:
            Naryn = n.read().strip()
            self.naryn = Naryn+ 'Mr/H'

        with open("DataBases/Isik_Kul.txt", 'r') as Is:
            Issyk = Is.read().strip()
            self.issik_kul = Issyk+ 'Mr/H'

        with open("DataBases/radiation_unit.txt", 'r') as ru:
            radiation_unite = ru.read().strip()
            self.radiation_num = radiation_unite+ 'Mr/H'

        with open("DataBases/local.txt", 'r') as ll:
            city = ll.read().strip()
            self.cyti = city


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Radiation Zone!!!"))
        self.label.setText(_translate("MainWindow", "Введите название области или города: "))
        self.btn_search.setText(_translate("MainWindow", "→"))
        self.label_3.setText(_translate("MainWindow", "Азот:"))
        self.label_5.setText(_translate("MainWindow", "Кислород:"))
        self.label_6.setText(_translate("MainWindow", "Аргон:"))
        self.label_7.setText(_translate("MainWindow", "Углекислый Газ:"))
        self.calculate.setText(_translate("MainWindow", "Вычеслить самому:"))
        self.azot.setText(_translate("MainWindow", "78%"))
        self.cislorod.setText(_translate("MainWindow", "20%"))
        self.argon.setText(_translate("MainWindow", "0.93%"))
        self.carbon_dioxid.setText(_translate("MainWindow", "0.031%"))
        self.label_8.setText(_translate("MainWindow", "Состав воздуха:"))
        self.label_10.setText(_translate("MainWindow", "----------------------------------------------------------------------------------------------------------------------------"))
        self.label_13.setText(_translate("MainWindow", "Солнечная радиация:"))
        self.label_14.setText(_translate("MainWindow", "Температура при \n"
                                                       "солнечной радиации:"))
        self.label_15.setText(_translate("MainWindow", "80°С"))
        self.label_9.setText(_translate("MainWindow", "Радиация:"))
        self.label_11.setText(_translate("MainWindow", "----------------------------------------------------------------------------------------------------------------------------"))

        self.radiation_Koeficent.setText(_translate("MainWindow", "Вычислить коэфицент радиации:"))
        self.btn_calculator.setText(_translate("MainWindow", "Калькулятор!"))
        self.viktorino.setText(_translate("MainWindow", "Тех поддержка"))
        self.graf.setText(_translate("MainWindow", "Статистика"))
        self.about_as.setText(_translate("MainWindow", "О нас!"))
        self.hide_polution.setText(_translate("MainWindow", "Вычеслить загрязнение:"))
        self.additional_features.setText(_translate("MainWindow", "Спец возможности:"))
        self.radiation_function.setText(_translate("MainWindow", "Дополнительные функции..."))

    def searche_radiation(self):
        global radiation_input
        global Batkent
        if self.radiation_input == self.cyti:
            self.radiation.setText(self.radiation_num)
        elif self.radiation_input == 'Ош':
            self.radiation.setText(self.osh)
        elif self.radiation_input == 'Бишкек':
            self.radiation.setText(self.bishkek)
        elif self.radiation_input == 'Баткен':
            self.radiation.setText(self.batken)
        elif self.radiation_input == 'Джалал-Абад':
            self.radiation.setText(self.djalal_abad)
        elif self.radiation_input == 'Нарын':
            self.radiation.setText(self.naryn)
        elif self.radiation_input == 'Талас':
            self.radiation.setText(self.talas)
        elif self.radiation_input == 'Иссык-Куль':
            self.radiation.setText(self.issik_kul)
        elif self.radiation_input == 'Кыргызстан':
            self.radiation.setText(self.kyrgyzstan)
        elif self.radiation_input == 'Чуй':
            self.radiation.setText(self.chuy)
        else:
            self.radiation.setText(self.else_)


    def radiation_input_(self, text):
        global radiation_input
        self.input_line = text
        self.radiation_input = text

    def open_whatsapp(self):
        # Открываем веб-версию WhatsApp с номером телефона +996552484942
        url = QUrl("https://web.whatsapp.com/send?phone=+996552484942")
        QDesktopServices.openUrl(url)



def open_window():
    pass


def open_graf():
    global Dialog4
    Dialog4 = QtWidgets.QDialog()
    ui = Ui_Dialog4()
    ui.setupUi(Dialog4)
    Dialog4.show()



def open_wikipedia():
    url = QUrl("https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D1%80%D0%B0%D0%B4%D0%B8%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D1%85_%D0%B0%D0%B2%D0%B0%D1%80%D0%B8%D0%B9")
    QDesktopServices.openUrl(url)



def open_mchs():
    mchs_url = QUrl('https://web.whatsapp.com/send?phone=996556112000')
    QDesktopServices.openUrl(mchs_url)



def dialog_input():
    pass

def open_about_as():
    global Dialog2
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow.setWindowTitle('Radiation Zone')
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
