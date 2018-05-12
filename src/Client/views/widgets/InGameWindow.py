from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


# noinspection PyPep8Naming
class InGameWindow(QtWidgets.QDialog):

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.__buttons_pressed = None
        self.__get_button = lambda button_text: None
        self.__plainTextEdit = None
        self.__keys_dict = {
            Qt.Key_A: "A", Qt.Key_B: "B", Qt.Key_C: "C", Qt.Key_D: "D", Qt.Key_E: "E", Qt.Key_F: "F", Qt.Key_G: "G",
            Qt.Key_H: "H", Qt.Key_I: "I", Qt.Key_J: "J", Qt.Key_K: "K", Qt.Key_L: "L", Qt.Key_M: "M", Qt.Key_N: "N",
            Qt.Key_O: "O", Qt.Key_P: "P", Qt.Key_Q: "Qu", Qt.Key_R: "R", Qt.Key_S: "S", Qt.Key_T: "T", Qt.Key_U: "U",
            Qt.Key_V: "V", Qt.Key_X: "X", Qt.Key_W: "W", Qt.Key_Y: "Y", Qt.Key_Z: "Z"
        }

    def initialize(self, get_button_function=lambda button_text: None, buttons_pressed=None, plain_text_edit=None):
        if buttons_pressed is None:
            buttons_pressed = []
        self.__buttons_pressed = buttons_pressed
        self.__plainTextEdit = plain_text_edit
        self.__get_button = get_button_function

    def keyPressEvent(self, event):
        key = event.key()
        if key in self.__keys_dict:
            # noinspection PyNoneFunctionAssignment
            button = self.__get_button(self.__keys_dict[key])
            if button:
                self.__buttons_pressed.append(button)
                button.setEnabled(False)
                self.__plainTextEdit.insertPlainText(button.text())
