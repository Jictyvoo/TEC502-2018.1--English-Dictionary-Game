from PyQt5 import QtWidgets

from Client.views.Room_Selection import UiBoggleRoomSelection

from Client.util.resource_rc import qInitResources


# noinspection PyArgumentList
def main():
    import sys

    qInitResources()
    app = QtWidgets.QApplication(sys.argv)
    boggle_room_selection = QtWidgets.QMainWindow()
    ui = UiBoggleRoomSelection()
    ui.setup_ui(boggle_room_selection)
    boggle_room_selection.show()
    sys.exit(app.exec_())
