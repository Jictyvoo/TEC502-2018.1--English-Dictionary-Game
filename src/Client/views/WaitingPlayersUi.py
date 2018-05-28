# noinspection PyUnresolvedReferences
from PyQt5 import QtCore, QtWidgets


class WaitingPlayersUi(object):

    def __init__(self):
        self._translate = None
        self.horizontalLayout_1 = None
        self.horizontalLayout_2 = None
        self.verticalLayout_1 = None
        self.verticalLayout_2 = None
        self.progressBar = None
        self.label = None
        self.listWidget = None
        self.buttonBox = None

    def setup_ui(self, waiting_connections):
        waiting_connections.setObjectName("waiting_connections")
        waiting_connections.resize(400, 300)
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(waiting_connections)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(waiting_connections)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
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
        self.buttonBox.accepted.connect(waiting_connections.accept)
        self.buttonBox.rejected.connect(waiting_connections.reject)
        QtCore.QMetaObject.connectSlotsByName(waiting_connections)

    def __add_players(self):
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = self.listWidget.item(0)
        item.setText(self._translate("waiting_connections", "Rustorier"))
        item = self.listWidget.item(1)
        item.setText(self._translate("waiting_connections", "Jictyvoo"))

    def re_translate_ui(self, waiting_connections):
        self._translate = QtCore.QCoreApplication.translate
        waiting_connections.setWindowTitle(self._translate("waiting_connections", "Waiting Players"))
        self.label.setText(self._translate("waiting_connections", "Players Connected"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)
