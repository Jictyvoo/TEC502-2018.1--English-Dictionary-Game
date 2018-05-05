from PyQt5 import QtWidgets

from Client.views.Room_Selection import Ui_Boggle_RoomSelection

from Client.views.resource_rc import qInitResources


def main():
    import sys

    qInitResources()
    app = QtWidgets.QApplication(sys.argv)
    boggle__room_selection = QtWidgets.QMainWindow()
    ui = Ui_Boggle_RoomSelection()
    ui.setupUi(boggle__room_selection)
    boggle__room_selection.show()
    sys.exit(app.exec_())
