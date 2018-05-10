from PyQt5 import QtCore, QtWidgets


class UiGameOver(object):

    def __init__(self, game_over_message):
        self.__verticalLayout = None
        self.__label = None
        self.__buttonBox = None
        self.__gameOverMessage = game_over_message

    def setup_ui(self, game_over):
        game_over.setObjectName("game_over")
        game_over.resize(400, 110)
        self.__verticalLayout = QtWidgets.QVBoxLayout(game_over)
        self.__verticalLayout.setObjectName("__verticalLayout")
        self.__label = QtWidgets.QLabel(game_over)
        self.__label.setAlignment(QtCore.Qt.AlignCenter)
        self.__label.setObjectName("__label")
        self.__verticalLayout.addWidget(self.__label)
        self.__buttonBox = QtWidgets.QDialogButtonBox(game_over)
        self.__buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.__buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.__buttonBox.setObjectName("__buttonBox")
        self.__verticalLayout.addWidget(self.__buttonBox)

        self.__re_translate_ui(game_over)
        self.__buttonBox.rejected.connect(game_over.reject)
        self.__buttonBox.accepted.connect(game_over.accept)
        QtCore.QMetaObject.connectSlotsByName(game_over)

    def __re_translate_ui(self, game_over):
        _translate = QtCore.QCoreApplication.translate
        game_over.setWindowTitle(_translate("game_over", "Game Over!"))
        self.__label.setText(_translate("game_over", self.__gameOverMessage))
