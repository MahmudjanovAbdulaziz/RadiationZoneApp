import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Notes_saves(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 397)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(11, 11, 449, 371))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")

        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(177, 30, 100, 40))
        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.text_lab_1 = QtWidgets.QLabel(self.widget)
        self.text_lab_1.setGeometry(QtCore.QRect(20, 130, 410, 160))
        self.text_lab_1.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.text_lab_1.setText("")
        self.text_lab_1.setObjectName("text_lab_1")
        self.text_lab_1.setWordWrap(True)

        self.btn_notes_save = QtWidgets.QPushButton(self.widget)
        self.btn_notes_save.setGeometry(QtCore.QRect(20, 330, 410, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.btn_notes_save.setFont(font)
        self.btn_notes_save.setStyleSheet("QPushButton{\n"
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
        self.btn_notes_save.setIcon(icon)
        self.btn_notes_save.setObjectName("btn_notes_save")
        self.inp_line_1 = QtWidgets.QLineEdit(self.widget)
        self.inp_line_1.setGeometry(QtCore.QRect(20, 80, 410, 20))
        self.inp_line_1.setStyleSheet("QLineEdit{\n"
"background-color: rgba(255, 255, 255, 30);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"selection-color: rgb(220, 0, 110);\n"
"alternate-background-color: rgb(220, 0, 110);\n"
"}\n"
"QLineEdit::hover{\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: rgb(220, 0, 110);\n"
"font: italic 12pt \"Arial\";\n"
"}\n"
"QLineEdit::cursor{\n"
"color: rgb(255, 248, 20);\n"
"}\n"
"QPushButton#myButton {\n"
"    border: none; /* удалить рамку кнопки */\n"
"    background-image: url(Images/image.png); /* путь к изображению */\n"
"    background-repeat: no-repeat; /* не повторять фон */\n"
"    background-position: center; /* центрировать изображение */\n"
"}")
        self.inp_line_1.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inp_line_1.setClearButtonEnabled(True)
        self.inp_line_1.setObjectName("inp_line_1")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_notes_save.clicked.connect(self.create_save)
        self.inp_line_1.textChanged.connect(self.text_change)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Сохранение:"))
        self.btn_notes_save.setText(_translate("Dialog", "Сохранить"))

    def text_change(self, text):
        self.text_lab_1.setText(str(text))

    def create_save(self):
        text = self.inp_line_1.text()
        if text:
            with open('DataBases/notes.txt', 'w') as f:
                f.write(text)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Notes_saves()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
