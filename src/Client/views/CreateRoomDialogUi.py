# noinspection PyUnresolvedReferences
from PyQt5 import QtCore, QtWidgets


# noinspection PyArgumentList
class CreateRoomDialogUi(object):

    def __init__(self, socket_controller):
        self.__vertical_layout = None
        self.__form_layout = None
        self.__total_players_label = None
        self.__total_players_input = None
        self.__room_name_label = None
        self.__room_name_input = None
        self.__room_password_label = None
        self.__room_password_input = None
        self.__button_box = None
        self.__dialog = None
        self.__socketController = socket_controller

    def setup_ui(self, dialog):
        self.__dialog = dialog
        dialog.setObjectName("dialog")
        dialog.resize(314, 140)
        self.__vertical_layout = QtWidgets.QVBoxLayout(dialog)
        self.__vertical_layout.setObjectName("verticalLayout")
        self.__form_layout = QtWidgets.QFormLayout()
        self.__form_layout.setObjectName("formLayout")
        self.__total_players_label = QtWidgets.QLabel(dialog)
        self.__total_players_label.setObjectName("totalPlayers_label")
        self.__form_layout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.__total_players_label)
        self.__total_players_input = QtWidgets.QPlainTextEdit(dialog)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.__total_players_input.sizePolicy().hasHeightForWidth())
        self.__total_players_input.setSizePolicy(size_policy)
        self.__total_players_input.setMinimumSize(QtCore.QSize(0, 20))
        self.__total_players_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.__total_players_input.setCenterOnScroll(True)
        self.__total_players_input.setObjectName("totalPlayersInput")
        self.__form_layout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.__total_players_input)
        self.__room_name_label = QtWidgets.QLabel(dialog)
        self.__room_name_label.setObjectName("roomName_label")
        self.__form_layout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.__room_name_label)
        self.__room_name_input = QtWidgets.QPlainTextEdit(dialog)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.__room_name_input.sizePolicy().hasHeightForWidth())
        self.__room_name_input.setSizePolicy(size_policy)
        self.__room_name_input.setMinimumSize(QtCore.QSize(0, 20))
        self.__room_name_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.__room_name_input.setCenterOnScroll(True)
        self.__room_name_input.setObjectName("roomNameInput")
        self.__form_layout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.__room_name_input)
        self.__room_password_label = QtWidgets.QLabel(dialog)
        self.__room_password_label.setObjectName("roomPassword_label")
        self.__form_layout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.__room_password_label)
        self.__room_password_input = QtWidgets.QPlainTextEdit(dialog)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.__room_password_input.sizePolicy().hasHeightForWidth())
        self.__room_password_input.setSizePolicy(size_policy)
        self.__room_password_input.setMinimumSize(QtCore.QSize(0, 20))
        self.__room_password_input.setMaximumSize(QtCore.QSize(16777215, 25))
        self.__room_password_input.setCenterOnScroll(True)
        self.__room_password_input.setObjectName("passwordInput")
        self.__form_layout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.__room_password_input)
        self.__vertical_layout.addLayout(self.__form_layout)
        self.__button_box = QtWidgets.QDialogButtonBox(dialog)
        self.__button_box.setOrientation(QtCore.Qt.Horizontal)
        self.__button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.__button_box.setObjectName("buttonBox")
        self.__vertical_layout.addWidget(self.__button_box)

        self.__re_translate_ui(dialog)
        self.__button_box.accepted.connect(lambda: self.__accept_button())
        self.__button_box.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def __accept_button(self):
        try:
            room_name = self.__room_name_input.toPlainText()
            password = self.__room_password_input.toPlainText()
            total_players = int(self.__total_players_input.toPlainText())
            self.__socketController.create_room(room_name, password, total_players)
        except ValueError as error:
            print(error)
        finally:
            self.__dialog.accept()

    def __re_translate_ui(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Room Configuration"))
        self.__total_players_label.setText(_translate("dialog", "Total Players:"))
        self.__room_name_label.setText(_translate("dialog", "Room Name:"))
        self.__room_password_label.setText(_translate("dialog", "Room Password:"))
