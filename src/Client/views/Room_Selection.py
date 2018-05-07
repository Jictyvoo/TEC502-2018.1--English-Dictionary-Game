from PyQt5 import QtCore, QtWidgets


# noinspection PyArgumentList
class UiBoggleRoomSelection(object):

    def __init__(self):
        self.__central_widget = None
        self.verticalLayout_2 = None
        self.label_2 = None
        self.scrollArea = None
        self.scrollAreaWidgetContents = None
        self.horizontalLayout_2 = None
        self.listWidget = None
        self.line = None
        self.verticalLayout = None
        self.label = None
        self.plainTextEdit = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.pushButton_4 = None
        self.horizontalLayout_3 = None
        self.horizontalLayout = None
        self.pushButton = None
        self.__status_bar = None
        self.__menu_bar = None

    def setup_ui(self, boggle_room_selection):
        boggle_room_selection.setObjectName("boggle_room_selection")
        boggle_room_selection.resize(480, 344)
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
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
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
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        spacer_item_1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacer_item_1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        spacer_item_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacer_item_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.__central_widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.__central_widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
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

    def __re_translate_ui(self, boggle_room_selection):
        _translate = QtCore.QCoreApplication.translate
        boggle_room_selection.setWindowTitle(_translate("boggle_room_selection", "Boggle Room Selection"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("boggle_room_selection", "Room Name: 4/5 Players"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("boggle_room_selection", "Username:"))
        self.pushButton_3.setText(_translate("boggle_room_selection", "Configuration"))
        self.pushButton_4.setText(_translate("boggle_room_selection", "Refresh"))
        self.pushButton_2.setText(_translate("boggle_room_selection", "Join Room"))
        self.pushButton.setText(_translate("boggle_room_selection", "Create new Room"))
