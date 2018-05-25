from PyQt5 import QtCore, QtWidgets


# noinspection PyArgumentList
from Client.controllers.SocketController import SocketController


class RoomSelectionUi(object):

    def __init__(self):
        self.__central_widget = None
        self.scrollArea = None
        self.scrollAreaWidgetContents = None
        self.verticalLayout = None
        self.verticalLayout_2 = None
        self.horizontalLayout = None
        self.horizontalLayout_2 = None
        self.horizontalLayout_3 = None
        self.listWidget = None
        self.line = None
        self.label = None
        self.label_2 = None
        self.plainTextEdit = None
        self.__configButton = None
        self.__joinRoomButton = None
        self.__refreshButton = None
        self.__createRoomButton = None
        self.__status_bar = None
        self.__menu_bar = None

        self.__room_selection_window = None
        self.__dialog = None
        self.__socketController = SocketController()

    def setup_ui(self, boggle_room_selection):
        self.__room_selection_window = boggle_room_selection
        boggle_room_selection.setObjectName("boggle_room_selection")
        boggle_room_selection.resize(480, 350)
        self.__central_widget = QtWidgets.QWidget(boggle_room_selection)
        self.__central_widget.setObjectName("__central_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.__central_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.__central_widget)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(size_policy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 90))
        self.label_2.setStyleSheet("image: url(:/boggle_logo/logo_boggle_212810.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.scrollArea = QtWidgets.QScrollArea(self.__central_widget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 460, 146))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")

        self.listWidget.itemDoubleClicked.connect(self.__select_item)

        self.horizontalLayout_2.addWidget(self.listWidget)
        spacer_item_0 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacer_item_0)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_2.addWidget(self.line)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(size_policy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.__configButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.__configButton.setObjectName("__configButton")
        self.verticalLayout.addWidget(self.__configButton)
        spacer_item_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item_1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.__refreshButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.__refreshButton.setObjectName("__refreshButton")

        self.__refreshButton.clicked.connect(lambda: self.__refresh_rooms())

        self.horizontalLayout_3.addWidget(self.__refreshButton)
        spacer_item_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacer_item_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.__joinRoomButton = QtWidgets.QPushButton(self.__central_widget)
        self.__joinRoomButton.setObjectName("__joinRoomButton")

        self.__joinRoomButton.clicked.connect(lambda: self.__select_item(self.listWidget.currentItem()))

        self.horizontalLayout.addWidget(self.__joinRoomButton)
        self.__createRoomButton = QtWidgets.QPushButton(self.__central_widget)
        self.__createRoomButton.setObjectName("__createRoomButton")

        self.__createRoomButton.clicked.connect(lambda: self.__create_room_dialog())

        self.horizontalLayout.addWidget(self.__createRoomButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        boggle_room_selection.setCentralWidget(self.__central_widget)
        self.__menu_bar = QtWidgets.QMenuBar(boggle_room_selection)
        self.__menu_bar.setGeometry(QtCore.QRect(0, 0, 480, 25))
        self.__menu_bar.setObjectName("__menu_bar")
        boggle_room_selection.setMenuBar(self.__menu_bar)
        self.__status_bar = QtWidgets.QStatusBar(boggle_room_selection)
        self.__status_bar.setObjectName("__status_bar")
        boggle_room_selection.setStatusBar(self.__status_bar)

        self.__re_translate_ui(boggle_room_selection)
        QtCore.QMetaObject.connectSlotsByName(boggle_room_selection)

    def __refresh_rooms(self):
        rooms = self.__socketController.get_rooms()
        self.listWidget.clear()
        for room in rooms:
            self.add_item(room)

    def __select_item(self, item):
        print("Here comes a method that call connection functions", item)

    def add_item(self, room_data):
        item = QtWidgets.QListWidgetItem()
        item.setText(self._translate("boggle_room_selection", "%s Players" % room_data))
        self.listWidget.addItem(item)

    def __create_room_dialog(self):
        from Client.views.CreateRoomDialogUi import CreateRoomDialogUi
        self.__dialog = QtWidgets.QDialog(self.__room_selection_window)
        ui = CreateRoomDialogUi(self.__socketController)
        ui.setup_ui(self.__dialog)
        self.__dialog.show()

    def __re_translate_ui(self, boggle_room_selection):
        self._translate = QtCore.QCoreApplication.translate
        boggle_room_selection.setWindowTitle(self._translate("boggle_room_selection", "Boggle Room Selection"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(self._translate("boggle_room_selection", "Username:"))
        self.__configButton.setText(self._translate("boggle_room_selection", "Configuration"))
        self.__refreshButton.setText(self._translate("boggle_room_selection", "Refresh"))
        self.__joinRoomButton.setText(self._translate("boggle_room_selection", "Join Room"))
        self.__createRoomButton.setText(self._translate("boggle_room_selection", "Create new Room"))
