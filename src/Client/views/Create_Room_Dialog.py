# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Create_Room_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


# noinspection PyArgumentList
class UiDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(314, 140)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.totalPlayers_label = QtWidgets.QLabel(Dialog)
        self.totalPlayers_label.setObjectName("totalPlayers_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totalPlayers_label)
        self.totalPlayersInput = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalPlayersInput.sizePolicy().hasHeightForWidth())
        self.totalPlayersInput.setSizePolicy(sizePolicy)
        self.totalPlayersInput.setMinimumSize(QtCore.QSize(0, 20))
        self.totalPlayersInput.setMaximumSize(QtCore.QSize(16777215, 25))
        self.totalPlayersInput.setCenterOnScroll(True)
        self.totalPlayersInput.setObjectName("totalPlayersInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalPlayersInput)
        self.roomName_label = QtWidgets.QLabel(Dialog)
        self.roomName_label.setObjectName("roomName_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.roomName_label)
        self.roomNameInput = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roomNameInput.sizePolicy().hasHeightForWidth())
        self.roomNameInput.setSizePolicy(sizePolicy)
        self.roomNameInput.setMinimumSize(QtCore.QSize(0, 20))
        self.roomNameInput.setMaximumSize(QtCore.QSize(16777215, 25))
        self.roomNameInput.setCenterOnScroll(True)
        self.roomNameInput.setObjectName("roomNameInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.roomNameInput)
        self.roomPassword_label = QtWidgets.QLabel(Dialog)
        self.roomPassword_label.setObjectName("roomPassword_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.roomPassword_label)
        self.passwordInput = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.passwordInput.sizePolicy().hasHeightForWidth())
        self.passwordInput.setSizePolicy(sizePolicy)
        self.passwordInput.setMinimumSize(QtCore.QSize(0, 20))
        self.passwordInput.setMaximumSize(QtCore.QSize(16777215, 25))
        self.passwordInput.setCenterOnScroll(True)
        self.passwordInput.setObjectName("passwordInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwordInput)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.totalPlayers_label.setText(_translate("Dialog", "Total Players:"))
        self.roomName_label.setText(_translate("Dialog", "Room Name:"))
        self.roomPassword_label.setText(_translate("Dialog", "Room Password:"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = UiDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
