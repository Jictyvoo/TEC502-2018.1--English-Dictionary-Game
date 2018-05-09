# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Boggle_Game.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


# noinspection PyArgumentList
class UiRoomGame(object):

    def __init__(self):
        self.pushButton = None
        self.verticalLayout_3 = None
        self.verticalLayout_2 = None
        self.verticalLayout = None
        self.time_horizontalLayout = None
        self.remainingTime = None
        self.progressBar = None
        self.plainTextEdit = None
        self.words_horizontalLayout = None
        self.totalPlayers_verticalLayout = None
        self.totalPlayers_scrollArea = None
        self.scrollArea = None
        self.scrollAreaWidgetContents = None
        self.scrollAreaWidgetContents_2 = None
        self.verticalLayout_4 = None
        self.playersInSession_label = None
        self.listWidget_2 = None
        self.gridLayout = None
        self.foundedWords_label = None
        self.listWidget = None
        self.userInput_horizontalLayout = None
        self.guessWord_label = None
        self.word_button = None
        self._translate = None

        self.__current_word = ""
        self.__dice_manipulator = None

    def __button_function(self, button):
        def lambda_function():
            self.__current_word += button.text()
            button.setEnabled(False)
            self.plainTextEdit.insertPlainText(button.text())

        button.clicked.connect(lambda_function)

    def __generate_buttons(self, room__game):
        word_button = []

        count = 0
        for line in range(0, 4):
            for column in range(0, 4):
                current_word_button = QtWidgets.QPushButton(room__game)
                size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                size_policy.setHorizontalStretch(0)
                size_policy.setVerticalStretch(0)
                size_policy.setHeightForWidth(current_word_button.sizePolicy().hasHeightForWidth())
                current_word_button.setSizePolicy(size_policy)
                current_word_button.setObjectName("word_%d" % count)
                self.gridLayout.addWidget(current_word_button, line, column, 1, 1)

                self.__button_function(current_word_button)

                count += 1
                word_button.append(current_word_button)
        self.word_button = tuple(word_button)

    def __players_in_room(self, room_name):
        self.totalPlayers_verticalLayout = QtWidgets.QVBoxLayout()
        self.totalPlayers_verticalLayout.setObjectName("totalPlayers_verticalLayout")
        self.totalPlayers_scrollArea = QtWidgets.QScrollArea(room_name)
        self.totalPlayers_scrollArea.setWidgetResizable(True)
        self.totalPlayers_scrollArea.setObjectName("totalPlayers_scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 142, 296))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.playersInSession_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.playersInSession_label.setObjectName("playersInSession_label")
        self.verticalLayout_4.addWidget(self.playersInSession_label)
        self.listWidget_2 = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(size_policy)
        self.listWidget_2.setMinimumSize(QtCore.QSize(20, 0))
        self.listWidget_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)
        self.verticalLayout_4.addWidget(self.listWidget_2)
        spacer_item = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacer_item)
        self.totalPlayers_scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.totalPlayers_verticalLayout.addWidget(self.totalPlayers_scrollArea)
        self.words_horizontalLayout.addLayout(self.totalPlayers_verticalLayout)

    def __define_characters(self):
        count = 0
        for character in self.__dice_manipulator.randomize():
            self.word_button[count].setText(self._translate("room_name", character))
            count += 1

    def __add_found_words(self, item_text):
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item.setText(self._translate("room_name", item_text))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def setup_ui(self, room_name, active=False):
        room_name.setObjectName("room_name")
        room_name.resize(685, 390)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(room_name)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.time_horizontalLayout = QtWidgets.QHBoxLayout()
        self.time_horizontalLayout.setObjectName("time_horizontalLayout")
        self.remainingTime = QtWidgets.QLabel(room_name)
        self.remainingTime.setObjectName("remainingTime")
        self.time_horizontalLayout.addWidget(self.remainingTime)
        self.progressBar = QtWidgets.QProgressBar(room_name)
        self.progressBar.setMaximum(180)
        self.progressBar.setProperty("value", 34)
        self.progressBar.setObjectName("progressBar")
        self.time_horizontalLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.time_horizontalLayout)
        self.words_horizontalLayout = QtWidgets.QHBoxLayout()
        self.words_horizontalLayout.setObjectName("words_horizontalLayout")

        self._translate = QtCore.QCoreApplication.translate

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        self.__generate_buttons(room_name)

        if active:
            self.__players_in_room(room_name)
        else:
            from Client.util.DiceManipulator import DiceManipulator
            self.__dice_manipulator = DiceManipulator()
            self.__define_characters()

        self.words_horizontalLayout.addLayout(self.gridLayout)
        self.scrollArea = QtWidgets.QScrollArea(room_name)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 143, 298))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.foundedWords_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.foundedWords_label.setObjectName("foundedWords_label")
        self.verticalLayout_2.addWidget(self.foundedWords_label)
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        spacer_item = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacer_item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.words_horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.words_horizontalLayout)
        self.userInput_horizontalLayout = QtWidgets.QHBoxLayout()
        self.userInput_horizontalLayout.setObjectName("userInput_horizontalLayout")
        self.guessWord_label = QtWidgets.QLabel(room_name)
        self.guessWord_label.setObjectName("guessWord_label")
        self.userInput_horizontalLayout.addWidget(self.guessWord_label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(room_name)
        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(size_policy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(0, 20))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setCenterOnScroll(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.userInput_horizontalLayout.addWidget(self.plainTextEdit)
        self.pushButton = QtWidgets.QPushButton(room_name)
        self.pushButton.setObjectName("pushButton")
        self.userInput_horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.userInput_horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.__re_translate_ui(room_name)
        self.listWidget.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(room_name)

    def __re_translate_ui(self, room_name):
        room_name.setWindowTitle(self._translate("room_name", "Boggle Game!"))
        self.remainingTime.setText(self._translate("room_name", "Remaining Time:"))
        self.progressBar.setFormat(self._translate("room_name", "%p seconds"))
        '''self.playersInSession_label.setText(_translate("room_name", "Players In Session:"))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("room_name", "Foo | 5 points"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)'''
        self.foundedWords_label.setText(self._translate("room_name", "Founded Words"))
        self.guessWord_label.setText(self._translate("room_name", "Guess Word:"))
        self.pushButton.setText(self._translate("room_name", "Test Word"))
