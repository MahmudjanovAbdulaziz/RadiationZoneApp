from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Notes(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(757, 570)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(26, 20, 711, 521))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 50, 671, 230))
        self.label.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(90, 370, 230, 30))
        self.label_7.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_7.setObjectName("label_7")
        self.open_last_notes = QtWidgets.QPushButton(self.widget)
        self.open_last_notes.setGeometry(QtCore.QRect(40, 430, 300, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.open_last_notes.setFont(font)
        self.open_last_notes.setStyleSheet("QPushButton{\n"
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
        self.open_last_notes.setIcon(icon)
        self.open_last_notes.setObjectName("open_last_notes")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(460, 370, 130, 30))
        self.label_8.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.label_8.setObjectName("label_8")
        self.create_notes = QtWidgets.QPushButton(self.widget)
        self.create_notes.setGeometry(QtCore.QRect(370, 430, 300, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.create_notes.setFont(font)
        self.create_notes.setStyleSheet("QPushButton{\n"
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
        self.create_notes.setIcon(icon)
        self.create_notes.setObjectName("create_notes")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Заметка - это небольшой текст, содержащий записи о каком-либо событии, \n"
"идеях или заметках на будущее. Ее главный плюс - это возможность быстрого \n"
"и удобного сохранения информации, которую можно использовать позже в \n"
"своей работе или жизни. Заметки могут быть написаны на бумаге или в \n"
"электронном виде.\n"
"\n"
"Я считаю, что заметки очень полезны, так как они помогают организовать \n"
"информацию и не забыть важные детали. Кроме того, заметки могут быть очень \n"
"личными и помочь сохранить идеи и вдохновение на будущее. В целом, заметки - это \n"
"простой, но эффективный инструмент для повышения производительности \n"
"и организации своей жизни."))
        self.label_7.setText(_translate("Dialog", "Открыть последнюю запись:"))
        self.open_last_notes.setText(_translate("Dialog", "Открыть:"))
        self.label_8.setText(_translate("Dialog", "Сделать запись:"))
        self.create_notes.setText(_translate("Dialog", "Открыть:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Notes()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
