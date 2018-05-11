from PyQt5 import QtWidgets

from Client.util.resource_rc import qInitResources
from Client.views.MainMenuUi import MainMenuUi


# noinspection PyArgumentList
def main():
    import sys

    qInitResources()
    app = QtWidgets.QApplication(sys.argv)
    main_menu = QtWidgets.QMainWindow()
    ui = MainMenuUi()
    ui.setup_ui(main_menu)
    main_menu.show()
    sys.exit(app.exec_())
