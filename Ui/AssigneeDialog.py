# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/AssigneeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AssigneeDialog(object):
    def setupUi(self, AssigneeDialog):
        AssigneeDialog.setObjectName("AssigneeDialog")
        AssigneeDialog.setWindowModality(QtCore.Qt.WindowModal)
        AssigneeDialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(AssigneeDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.soldiersListWidget = QtWidgets.QListWidget(AssigneeDialog)
        self.soldiersListWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.soldiersListWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.soldiersListWidget.setObjectName("soldiersListWidget")
        self.verticalLayout.addWidget(self.soldiersListWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(AssigneeDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AssigneeDialog)
        self.buttonBox.accepted.connect(AssigneeDialog.accept)
        self.buttonBox.rejected.connect(AssigneeDialog.reject)
        self.soldiersListWidget.doubleClicked['QModelIndex'].connect(AssigneeDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AssigneeDialog)

    def retranslateUi(self, AssigneeDialog):
        _translate = QtCore.QCoreApplication.translate
        AssigneeDialog.setWindowTitle(_translate("AssigneeDialog", "שיבוץ חייל"))
