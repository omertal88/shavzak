# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/AssignmentDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AssignmentDialog(object):
    def setupUi(self, AssignmentDialog):
        AssignmentDialog.setObjectName("AssignmentDialog")
        AssignmentDialog.setWindowModality(QtCore.Qt.WindowModal)
        AssignmentDialog.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(AssignmentDialog)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(AssignmentDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.startDatetime = QtWidgets.QDateTimeEdit(AssignmentDialog)
        self.startDatetime.setObjectName("startDatetime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.startDatetime)
        self.endDatetime = QtWidgets.QDateTimeEdit(AssignmentDialog)
        self.endDatetime.setObjectName("endDatetime")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.endDatetime)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.soldiersListWidget = QtWidgets.QListWidget(AssignmentDialog)
        self.soldiersListWidget.setObjectName("soldiersListWidget")
        self.horizontalLayout.addWidget(self.soldiersListWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.assignSoldierButton = QtWidgets.QPushButton(AssignmentDialog)
        self.assignSoldierButton.setObjectName("assignSoldierButton")
        self.verticalLayout.addWidget(self.assignSoldierButton)
        self.unassignSoldierButton = QtWidgets.QPushButton(AssignmentDialog)
        self.unassignSoldierButton.setObjectName("unassignSoldierButton")
        self.verticalLayout.addWidget(self.unassignSoldierButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(AssignmentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.buttonBox)
        self.positionCombo = QtWidgets.QComboBox(AssignmentDialog)
        self.positionCombo.setObjectName("positionCombo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.positionCombo)
        self.label_2 = QtWidgets.QLabel(AssignmentDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(AssignmentDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(AssignmentDialog)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_4)

        self.retranslateUi(AssignmentDialog)
        self.buttonBox.accepted.connect(AssignmentDialog.accept)
        self.buttonBox.rejected.connect(AssignmentDialog.reject)
        self.assignSoldierButton.clicked.connect(AssignmentDialog.addAssignee)
        self.unassignSoldierButton.clicked.connect(AssignmentDialog.removeAssignee)
        QtCore.QMetaObject.connectSlotsByName(AssignmentDialog)

    def retranslateUi(self, AssignmentDialog):
        _translate = QtCore.QCoreApplication.translate
        AssignmentDialog.setWindowTitle(_translate("AssignmentDialog", "עריכת משימה"))
        self.label.setText(_translate("AssignmentDialog", "עמדה"))
        self.startDatetime.setDisplayFormat(_translate("AssignmentDialog", "d/M/yy hh:mm"))
        self.endDatetime.setDisplayFormat(_translate("AssignmentDialog", "d/M/yy hh:mm"))
        self.assignSoldierButton.setText(_translate("AssignmentDialog", "שבץ חייל"))
        self.unassignSoldierButton.setText(_translate("AssignmentDialog", "הסר חייל"))
        self.label_2.setText(_translate("AssignmentDialog", "התחלת משימה"))
        self.label_3.setText(_translate("AssignmentDialog", "סיום משימה"))
        self.label_4.setText(_translate("AssignmentDialog", "כוח אדם"))
