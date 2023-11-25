import pyperclip
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_notes_open(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 397)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 449, 371))
        self.widget.setStyleSheet("background-color: rgba(255, 255, 255, 30);\n"
"font: 14pt \"Arial\";\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.widget.setObjectName("widget")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(144, 30, 190, 20))

        self.label_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;\n"
"\n"
"\n"
"")
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.text_lab_2 = QtWidgets.QLabel(self.widget)
        self.text_lab_2.setGeometry(QtCore.QRect(20, 79, 410, 211))
        self.text_lab_2.setStyleSheet("background-color: none;\n"
"border-radius: none;\n"
"font: italic 12pt \"Arial\";\n"
"border: none;")
        self.text_lab_2.setText("")
        self.text_lab_2.setObjectName("text_lab_2")
        self.text_lab_2.setWordWrap(True)
        self.btn_notes_open = QtWidgets.QPushButton(self.widget)
        self.btn_notes_open.setGeometry(QtCore.QRect(20, 330, 410, 24))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.btn_notes_open.setFont(font)
        self.btn_notes_open.setStyleSheet("QPushButton{\n"
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
        self.btn_notes_open.setIcon(icon)
        self.btn_notes_open.setObjectName("btn_notes_open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.btn_notes_open.clicked.connect(self.open_notes)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Сохранённые данные:"))
        self.btn_notes_open.setText(_translate("Dialog", "Открыть"))

    def open_notes(self):
        with open('DataBases/notes.txt', 'r') as r:
            text = r.read()
            self.text_lab_2.setText(str(text))
            pyperclip.copy(self.text_lab_2.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_notes_open()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
