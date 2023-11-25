from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_radiation_elements(object):
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
        self.label.setGeometry(QtCore.QRect(10, 10, 441, 591))
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
        self.label.setText(_translate("Dialog", "Радиоактивные элементы - это элементы, которые \n"
"испускают излучение в процессе распада ядер. \n"
"Излучение может быть в виде частиц или энергии в \n"
"форме электромагнитных волн. Это свойство делает \n"
"их полезными для медицинских, промышленных и \n"
"научных приложений, но также может представлять \n"
"угрозу для здоровья и окружающей среды, если они \n"
"не управляются должным образом.\n"
"\n"
"Радиоактивные элементы могут быть \n"
"естественными, такими как уран, торий и калий, \n"
"или искусственными, созданными путем ядерных \n"
"реакций, например, плутоний и америций. Излучение \n"
"от радиоактивных элементов может быть альфа-, \n"
"бета- или гамма-излучением, которые имеют \n"
"различные характеристики и способность \n"
"проникновения в различные материалы.\n"
"\n"
"Некоторые радиоактивные элементы используются \n"
"в медицине, например, радиоактивные изотопы йода \n"
"используются для лечения рака щитовидной железы, \n"
"а радиоизотоп технеция используется для создания \n"
"изображений в медицинской диагностике. В \n"
"промышленности, радиоактивные элементы могут \n"
"использоваться для контроля уровня жидкостей в \n"
"трубопроводах, измерения плотности материалов, \n"
"а также для дефектоскопии металлических \n"
"конструкций."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_radiation_elements()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
