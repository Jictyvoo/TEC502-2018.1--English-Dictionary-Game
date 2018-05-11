from PyQt5 import QtCore, QtWidgets

from Client.util.resource_rc import qInitResources


class MainMenuUi(object):

    def __init__(self):
        self.__central_widget = None
        self.__vertical_layout_2 = None
        self.__vertical_layout_1 = None
        self.__horizontal_layout = None
        self.__boggle_logo_label = None
        self.__start_solo_game_button = None
        self.__search_room_button = None
        self.__menu_bar = None
        self.__status_bar = None
        self.__boggle_room_selection = None
        self.__main_menu = None
        self.__solo_game = None

    def setup_ui(self, main__menu):
        self.__main_menu = main__menu
        main__menu.setObjectName("main__menu")
        main__menu.resize(345, 315)
        self.__central_widget = QtWidgets.QWidget(main__menu)
        self.__central_widget.setObjectName("__central_widget")
        self.__vertical_layout_2 = QtWidgets.QVBoxLayout(self.__central_widget)
        self.__vertical_layout_2.setObjectName("__vertical_layout_2")
        self.__horizontal_layout = QtWidgets.QHBoxLayout()
        self.__horizontal_layout.setObjectName("__horizontal_layout")
        spacer_item_1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                              QtWidgets.QSizePolicy.Minimum)
        self.__horizontal_layout.addItem(spacer_item_1)
        self.__vertical_layout_1 = QtWidgets.QVBoxLayout()
        self.__vertical_layout_1.setObjectName("__vertical_layout_1")
        self.__boggle_logo_label = QtWidgets.QLabel(self.__central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.__boggle_logo_label.sizePolicy().hasHeightForWidth())
        self.__boggle_logo_label.setSizePolicy(size_policy)
        self.__boggle_logo_label.setMinimumSize(QtCore.QSize(200, 0))
        self.__boggle_logo_label.setStyleSheet("image: url(:/boggle_logo/logo_boggle_212810.png);")
        self.__boggle_logo_label.setText("")
        self.__boggle_logo_label.setObjectName("__boggle_logo_label")
        self.__vertical_layout_1.addWidget(self.__boggle_logo_label)
        self.__start_solo_game_button = QtWidgets.QPushButton(self.__central_widget)
        self.__start_solo_game_button.setObjectName("__start_solo_game_button")

        self.__start_solo_game_button.clicked.connect(self.__start_solo_game)

        self.__vertical_layout_1.addWidget(self.__start_solo_game_button)
        self.__search_room_button = QtWidgets.QPushButton(self.__central_widget)
        self.__search_room_button.setObjectName("__search_room_button")

        self.__search_room_button.clicked.connect(self.__call_room_selection)

        self.__vertical_layout_1.addWidget(self.__search_room_button)
        self.__horizontal_layout.addLayout(self.__vertical_layout_1)
        spacer_item_2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                              QtWidgets.QSizePolicy.Minimum)
        self.__horizontal_layout.addItem(spacer_item_2)
        self.__vertical_layout_2.addLayout(self.__horizontal_layout)
        main__menu.setCentralWidget(self.__central_widget)
        self.__menu_bar = QtWidgets.QMenuBar(main__menu)
        self.__menu_bar.setGeometry(QtCore.QRect(0, 0, 345, 21))
        self.__menu_bar.setObjectName("__menu_bar")
        main__menu.setMenuBar(self.__menu_bar)
        self.__status_bar = QtWidgets.QStatusBar(main__menu)
        self.__status_bar.setObjectName("__status_bar")
        main__menu.setStatusBar(self.__status_bar)

        self.__re_translate_ui(main__menu)
        QtCore.QMetaObject.connectSlotsByName(main__menu)

    def __re_translate_ui(self, main__menu):
        _translate = QtCore.QCoreApplication.translate
        main__menu.setWindowTitle(_translate("main__menu", "Boggle Game!"))
        self.__start_solo_game_button.setText(_translate("main__menu", "Iniciar Jogo Solo"))
        self.__search_room_button.setText(_translate("main__menu", "Buscar Salas de Jogo"))

    def __call_room_selection(self):
        qInitResources()

        from Client.views.RoomSelectionUi import RoomSelectionUi
        # self.__boggle_room_selection = QtWidgets.QMainWindow()
        ui = RoomSelectionUi()
        ui.setup_ui(self.__main_menu)
        # self.__main_menu.hide()
        # self.__boggle_room_selection.show()

    def __start_solo_game(self):
        from Client.views.InGameUi import InGameUi
        self.__solo_game = QtWidgets.QDialog()
        ui = InGameUi()
        ui.setup_ui(self.__solo_game)
        self.__main_menu.hide()
        self.__solo_game.show()
