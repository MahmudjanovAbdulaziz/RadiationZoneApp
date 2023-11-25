from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout
from hend import Ui_Dialog
from center import Ui_MainWindow
from RaidiationKoef import Ui_Dialok
from sign_in import Ui_Dialog8
from Administrator import Ui_Dialog9
from admin import Ui_Dialog10
from new_location import chenge_New_Local
from polution import Polution
from more_function import Ui_MoreFunction
from how_to_protect_radiation import Ui_how_to_protect_tadiation
from filters_masks import Ui_filter_masks
from radiation_element import Ui_radiation_elements
from graf import Ui_Dialog4
from how_to_protect import Ui_how_to_protect
from how_to_protect_sun import Ui_how_to_protect_sun
from people_radiation import Ui_people_radiation
from how_to_create_bunker import Ui_how_to_create_bunker
from bunker_1 import Ui_bunker_1
from how_many_wait_radaition import Ui_how_many_wait
from global_calls import Ui_global_calls
from extra_calls import Ui_extra_calls
from calc_instrumets import Ui_calc_instruments
from calc_dozimetr import Ui_Dozimetr
from calc_geyger import Ui_geyger
from calc_spiktometr import Ui_spiktometr
from material_thikcnes_calc import Ui_material_thiknes
from mat_thiknes_calc import Ui_mat_thiknes_calculate
from products_radiation import Ui_product_radiation
from calc_unit import Ui_Calc_unite
from alpha_beta_gamma import Ui_Alpha_beta_gamme
from unite_calculate import Ui_Unite_calculate
from radiation_in_products import Ui_radaition_in_products
from searche_radiation_in_water import Ui_radaition_in_water
from hide_radiation import Ui_hide_radiation
from notess import Ui_Notes
from notes_saves import Ui_Notes_saves
from notes_open import Ui_notes_open




class Center(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.calculate.clicked.connect(self.open_hend)
        self.ui.hide_polution.clicked.connect(self.openPolution)
        self.ui.radiation_Koeficent.clicked.connect(self.openRadiationKoef)
        self.ui.additional_features.clicked.connect(self.openAdminS)
        self.ui.btn_calculator.clicked.connect(self.open_Calculator)
        self.ui.radiation_function.clicked.connect(self.open_more_function)




    def open_hend(self):
        # self.close()
        self.second_hend =  Hend()
        self.second_hend.exec_()
        # self.show()


    def openRadiationKoef(self):
        self.close()
        self.radiation_koefik = Radiation_koefic()
        self.radiation_koefik.exec_()
        self.show()

    def openAdminS(self):
        self.close()
        self.open_Admini = SignIn()
        self.open_Admini.exec_()

    def open_Calculator(self):
        self.openCalculator = Calculators()
        self.openCalculator.exec_()

    def openPolution(self):
        self.close()
        self.polut = CreatePolution()
        self.polut.exec_()
        self.show()

    def open_more_function(self):
        self.close()
        self.parmore_function = classmore_function()
        self.parmore_function.exec_()


class Hend(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class Radiation_koefic(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialok()
        self.ui.setupUi(self)

class SignIn(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog8()
        self.ui.setupUi(self)
        self.ui.sign_in.clicked.connect(self.open_Administrator)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)

    def open_Administrator(self):
        if self.ui.count == 2:
            self.open_researchersAdmin()

    def open_researchersAdmin(self):
        self.researchers = researchersAdmin()
        self.hide()
        self.researchers.exec_()



class researchersAdmin(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog9()
        self.ui.setupUi(self)

        self.ui.change_radiation.clicked.connect(self.Admin_change)
        self.ui.new_location_chenche.clicked.connect(self.open_chenge_local)


    def Admin_change(self):
        self.openAdmin = Change_radiation()
        self.openAdmin.exec_()

    def open_chenge_local(self):
        self.open_New_Location = Change_New_Loc()
        self.open_New_Location.exec_()

class clas_graf(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog4()
        self.ui.setupUi(self)

class Change_radiation(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog10()
        self.ui.setupUi(self)


class Change_New_Loc(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = chenge_New_Local()
        self.ui.setupUi(self)

class CreatePolution(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Polution()
        self.ui.setupUi(self)


class classfilter_Maks(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_filter_masks()
        self.ui.setupUi(self)

class classradiation_elements(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_radiation_elements()
        self.ui.setupUi(self)

class classhow_to_protect(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_how_to_protect()
        self.ui.setupUi(self)

class classhow_to_protect_sun(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_how_to_protect_sun()
        self.ui.setupUi(self)

class classpeople_radiation(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_people_radiation()
        self.ui.setupUi(self)

class classhow_to_protect_radiation(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_how_to_protect_tadiation()
        self.ui.setupUi(self)
        self.ui.filter_and_mask.clicked.connect(self.openfilter_masks)
        self.ui.radiation_elements.clicked.connect(self.open_radiation_elements)
        self.ui.rad_map.clicked.connect(self.openradaition_map)
        self.ui.rad_protect.clicked.connect(self.open_how_to_protect)
        self.ui.how_protect_sun_red.clicked.connect(self.openhow_to_protect_sun)
        self.ui.you_are_seck.clicked.connect(self.openpeople_radiation)

    def openfilter_masks(self):
        self.parfilter = classfilter_Maks()
        self.parfilter.exec_()

    def open_radiation_elements(self):
        self.parradiation_el = classradiation_elements()
        self.parradiation_el.exec_()

    def openradaition_map(self):
        self.parmap = clas_graf()
        self.parmap.exec_()

    def open_how_to_protect(self):
        self.parhow_to_prot = classhow_to_protect()
        self.parhow_to_prot.exec_()

    def openhow_to_protect_sun(self):
        self.parhow_to_prot = classhow_to_protect_sun()
        self.parhow_to_prot.exec_()

    def openpeople_radiation(self):
        self.parpeople = classpeople_radiation()
        self.parpeople.exec_()


class classbunker_1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_bunker_1()
        self.ui.setupUi(self)

class classhow_manywait(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_how_many_wait()
        self.ui.setupUi(self)

class classhow_to_create_bunker(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_how_to_create_bunker()
        self.ui.setupUi(self)

        self.ui.bunker_1.clicked.connect(self.openbunker_1)
        self.ui.bunker_radiation_calk.clicked.connect(self.openhow_many_wait)


    def openbunker_1(self):
        self.parbunker_1 = classbunker_1()
        self.parbunker_1.exec_()

    def openhow_many_wait(self):
        self.perhow_many_wait = classhow_manywait()
        self.perhow_many_wait.exec_()

class classextra_calls(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_extra_calls()
        self.ui.setupUi(self)

class classGloba_calls(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_global_calls()
        self.ui.setupUi(self)
        self.ui.extra_calls.clicked.connect(self.openextra_calls)

    def openextra_calls(self):
        self.perextracalls = classextra_calls()
        self.perextracalls.exec_()

class classdozimetr_calc(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dozimetr()
        self.ui.setupUi(self)

class classcalk_geyger(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_geyger()
        self.ui.setupUi(self)

class classspiktometr(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_spiktometr()
        self.ui.setupUi(self)

class classcalc_instaruments(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_calc_instruments()
        self.ui.setupUi(self)
        self.ui.dozimetr.clicked.connect(self.openDozimert)
        self.ui.geyger.clicked.connect(self.openGeyger)
        self.ui.spektrometr.clicked.connect(self.openSpiktometr)

    def openDozimert(self):
        self.perdozimetr = classdozimetr_calc()
        self.perdozimetr.exec_()

    def openGeyger(self):
        self.pergeyger = classcalk_geyger()
        self.pergeyger.exec_()

    def openSpiktometr(self):
        self.perspiktometr = classspiktometr()
        self.perspiktometr.exec_()

class classmaterial_thiknes_calc(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mat_thiknes_calculate()
        self.ui.setupUi(self)

class classmaterial_thiknes(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_material_thiknes()
        self.ui.setupUi(self)
        self.ui.calk_radiation_protect.clicked.connect(self.open_math_thiknes)

    def open_math_thiknes(self):
        self.per_math_thiknes = classmaterial_thiknes_calc()
        self.per_math_thiknes.exec_()

class classalpha_beta_gamma(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Alpha_beta_gamme()
        self.ui.setupUi(self)

class classunite_calculate(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Unite_calculate()
        self.ui.setupUi(self)

class classcalc_unite(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Calc_unite()
        self.ui.setupUi(self)

        self.ui.calc_alpa_beta_gamma.clicked.connect(self.open_alpha_betta_gamma)
        self.ui.radiation_converter.clicked.connect(self.open_radaition_converter)

    def open_alpha_betta_gamma(self):
        self.peralpha_beta_gamma = classalpha_beta_gamma()
        self.peralpha_beta_gamma.exec_()

    def open_radaition_converter(self):
        self.perradaition_converter = classunite_calculate()
        self.perradaition_converter.exec_()

class classradaition_in_products(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_radaition_in_products()
        self.ui.setupUi(self)
class classproducts_radaition(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_product_radiation()
        self.ui.setupUi(self)
        
        self.ui.pushButton.clicked.connect(self.open_radaition_products)

    def open_radaition_products(self):
        self.perradiation_products = classradaition_in_products()
        self.perradiation_products.exec_()

class classhideradaition(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_hide_radiation()
        self.ui.setupUi(self)

class classradaition_in_water(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_radaition_in_water()
        self.ui.setupUi(self)

        self.ui.searche_radaition_water_and.clicked.connect(self.open_hide_radiation)

    def open_hide_radiation(self):
        self.perhide_radaiiton = classhideradaition()
        self.perhide_radaiiton.exec_()

class classnotes_saves(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Notes_saves()
        self.ui.setupUi(self)

class classopen_notes(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_notes_open()
        self.ui.setupUi(self)
class classNotes(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Notes()
        self.ui.setupUi(self)

        self.ui.create_notes.clicked.connect(self.opensave_notes)
        self.ui.open_last_notes.clicked.connect(self.open_last_notes)

    def opensave_notes(self):
        self.persave_notes = classnotes_saves()
        self.persave_notes.exec_()

    def open_last_notes(self):
        self.perlast_notes = classopen_notes()
        self.perlast_notes.exec_()


class classmore_function(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MoreFunction()
        self.ui.setupUi(self)

        self.ui.how_to_protect.clicked.connect(self.openhow_to_protect_radiation)
        self.ui.hoe_to_create_bunker.clicked.connect(self.open_how_to_create_bunker)
        self.ui.global_call.clicked.connect(self.openglobal_calls)
        self.ui.dozimetr_calculate.clicked.connect(self.opencalc_instrumets)
        self.ui.thicknes_calculate.clicked.connect(self.open_material_thiknes)
        self.ui.food_calculate.clicked.connect(self.open_product_radaition)
        self.ui.unit_calculate.clicked.connect(self.opencalc_unite)
        self.ui.hide_eadiation.clicked.connect(self.open_radiation_in_water)
        self.ui.notes.clicked.connect(self.open_Notes)



    def openhow_to_protect_radiation(self):
        self.close()
        self.parhow_to_protect = classhow_to_protect_radiation()
        self.parhow_to_protect.exec_()
        self.show()

    def open_how_to_create_bunker(self):
        self.close()
        self.parhow_to_create = classhow_to_create_bunker()
        self.parhow_to_create.exec_()
        self.show()

    def openglobal_calls(self):
        self.close()
        self.perglobal_calls = classGloba_calls()
        self.perglobal_calls.exec_()
        self.show()

    def opencalc_instrumets(self):
        self.close()
        self.percalc_instruments = classcalc_instaruments()
        self.percalc_instruments.exec_()
        self.show()

    def open_material_thiknes(self):
        self.close()
        self.per_material = classmaterial_thiknes()
        self.per_material.exec_()
        self.show()

    def open_product_radaition(self):
        self.close()
        self.per_product = classproducts_radaition()
        self.per_product.exec_()
        self.show()

    def opencalc_unite(self):
        self.close()
        self.perunitecalc = classcalc_unite()
        self.perunitecalc.exec_()
        self.show()

    def open_radiation_in_water(self):
        self.close()
        self.perradaition_in_water = classradaition_in_water()
        self.perradaition_in_water.exec_()
        self.show()

    def open_Notes(self):
        self.close()
        self.pernotes = classNotes()
        self.pernotes.exec_()
        self.show()






class Calculators(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()


        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')

        self.result_label = QLabel('Result: ')
        self.result_lineedit = QLineEdit()
        self.result_lineedit.setReadOnly(True)

        # Создаем кнопки для цифр и операторов
        self.buttons = {}
        for i in range(10):
            self.buttons[i] = QPushButton(str(i))
        self.button_dot = QPushButton('.')
        self.button_plus = QPushButton('+')
        self.button_minus = QPushButton('-')
        self.button_multiply = QPushButton('*')
        self.button_divide = QPushButton('/')
        self.button_equals = QPushButton('=')
        self.button_clear = QPushButton('Clear')

        # Создаем сетку для кнопок цифр и операторов
        grid = QVBoxLayout()
        row1 = QHBoxLayout()
        row2 = QHBoxLayout()
        row3 = QHBoxLayout()
        row4 = QHBoxLayout()
        row5 = QHBoxLayout()

        row1.addWidget(self.result_label)
        row1.addWidget(self.result_lineedit)

        row2.addWidget(self.buttons[7])
        row2.addWidget(self.buttons[8])
        row2.addWidget(self.buttons[9])
        row2.addWidget(self.button_divide)

        row3.addWidget(self.buttons[4])
        row3.addWidget(self.buttons[5])
        row3.addWidget(self.buttons[6])
        row3.addWidget(self.button_multiply)

        row4.addWidget(self.buttons[1])
        row4.addWidget(self.buttons[2])
        row4.addWidget(self.buttons[3])
        row4.addWidget(self.button_minus)

        row5.addWidget(self.buttons[0])
        row5.addWidget(self.button_dot)
        row5.addWidget(self.button_equals)
        row5.addWidget(self.button_plus)

        grid.addLayout(row1)
        grid.addLayout(row2)
        grid.addLayout(row3)
        grid.addLayout(row4)
        grid.addLayout(row5)
        grid.addWidget(self.button_clear)

        self.setLayout(grid)

        # Подключаем события для кнопок
        for i in range(10):
            self.buttons[i].clicked.connect(self.add_digit)
        self.button_dot.clicked.connect(self.add_dot)
        self.button_plus.clicked.connect(self.add_operator)
        self.button_minus.clicked.connect(self.add_operator)
        self.button_multiply.clicked.connect(self.add_operator)
        self.button_divide.clicked.connect(self.add_operator)
        self.button_equals.clicked.connect(self.calculate)
        self.button_clear.clicked.connect(self.clear)

        button_style = '''
            QPushButton {
                font-size: 18pt;
                background-color: #3daee9;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #61c4f7;
            }
            QPushButton:pressed {
                background-color: #3292b9;
            }
        '''
        self.setStyleSheet(button_style)

    def add_digit(self):
        sender = self.sender()
        digit = int(sender.text())
        self.result_lineedit.setText(self.result_lineedit.text() + str(digit))

    def add_dot(self):
        if '.' not in self.result_lineedit.text():
            self.result_lineedit.setText(self.result_lineedit.text() + '.')

    def add_operator(self):
        sender = self.sender()
        operator = sender.text()
        self.result_lineedit.setText(self.result_lineedit.text() + operator)

    def calculate(self):
        try:
            result = eval(self.result_lineedit.text())
            self.result_lineedit.setText(str(result))
        except Exception:
            self.result_lineedit.setText('Error')

    def clear(self):
        self.result_lineedit.clear()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Center()
    window.show()
    sys.exit(app.exec_())
