# noinspection PyUnresolvedReferences
from PyQt5 import QtCore, QtWidgets


class WaitingPlayersUi(object):

    def __init__(self, socket_controller, maximum_players=2, room_name="", player_name="HaveNoName"):
        self._translate = None
        self.horizontalLayout_1 = None
        self.horizontalLayout_2 = None
        self.verticalLayout_1 = None
        self.verticalLayout_2 = None
        self.progressBar = None
        self.label = None
        self.listWidget = None
        self.buttonBox = None
        self.__socketController = socket_controller
        self.__maximum_players = maximum_players
        self.__room_name = room_name
        self.__currentPlayers = 0
        self.__timer = None
        self.__playerName = player_name
        self.__waiting_connections = None
        self.__game_window = None

    def setup_ui(self, waiting_connections):
        self.__waiting_connections = waiting_connections
        waiting_connections.setObjectName("waiting_connections")
        waiting_connections.resize(400, 300)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(waiting_connections)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(waiting_connections)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(self.__maximum_players)
        self.progressBar.setMinimum(0)
        self.verticalLayout_2.addWidget(self.progressBar)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.label = QtWidgets.QLabel(waiting_connections)
        self.label.setObjectName("label")
        self.verticalLayout_1.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(waiting_connections)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_1.addWidget(self.listWidget)
        self.horizontalLayout_2.addLayout(self.verticalLayout_1)
        self.buttonBox = QtWidgets.QDialogButtonBox(waiting_connections)
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_1.addLayout(self.verticalLayout_2)

        self.re_translate_ui(waiting_connections)

        self.__create_timer()

        self.buttonBox.accepted.connect(lambda: self.__accept_button())
        self.buttonBox.rejected.connect(waiting_connections.reject)
        QtCore.QMetaObject.connectSlotsByName(waiting_connections)

    def __accept_button(self):
        dices = self.__socketController.start_game(self.__room_name)
        from Client.views.InGameUi import InGameUi
        from Client.views.widgets.InGameWindow import InGameWindow
        if self.__game_window:
            self.__game_window.hide()

        # self.__solo_game = QtWidgets.QDialog(self.__main_menu)
        self.__game_window = InGameWindow()
        ui = InGameUi()
        ui.setup_ui(self.__game_window, True, dices)
        # self.__main_menu.hide()
        self.__game_window.show()
        self.__waiting_connections.accept()

    def __create_timer(self):
        def callback_tick():
            if self.__currentPlayers == self.__maximum_players:
                self.__timer.stop()
            else:
                self.__refresh_players()

        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(callback_tick)
        self.__timer.start(1000)

    def __refresh_players(self):
        players_names = self.__socketController.get_players_names(self.__room_name).decode('utf-8')
        if players_names:
            self.__currentPlayers = len(players_names.split("|_|"))
        self.progressBar.setValue(self.__currentPlayers)
        self.progressBar.setFormat(self._translate("waiting_connections", "%.0f players" % self.__currentPlayers))
        self.__add_players(players_names.split("|_|"))

    def __add_players(self, names_list):
        self.listWidget.clear()
        for name in names_list:
            item = QtWidgets.QListWidgetItem()
            item.setText(self._translate("waiting_connections", name))
            self.listWidget.addItem(item)

    def re_translate_ui(self, waiting_connections):
        self._translate = QtCore.QCoreApplication.translate
        waiting_connections.setWindowTitle(self._translate("waiting_connections", "Waiting Players"))
        self.label.setText(self._translate("waiting_connections", "Players Connected"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
