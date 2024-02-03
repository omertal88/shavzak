# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ShiftDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShiftDialog(object):
    def setupUi(self, ShiftDialog):
        ShiftDialog.setObjectName("ShiftDialog")
        ShiftDialog.resize(496, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShiftDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(ShiftDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.positionCombo = QtWidgets.QComboBox(ShiftDialog)
        self.positionCombo.setObjectName("positionCombo")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.positionCombo)
        self.label = QtWidgets.QLabel(ShiftDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox_3 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 2, 1, 1)
        self.checkBox_4 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_4.setObjectName("checkBox_4")
        self.gridLayout.addWidget(self.checkBox_4, 1, 0, 1, 1)
        self.checkBox_5 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_5.setObjectName("checkBox_5")
        self.gridLayout.addWidget(self.checkBox_5, 1, 1, 1, 1)
        self.checkBox_6 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_6.setObjectName("checkBox_6")
        self.gridLayout.addWidget(self.checkBox_6, 1, 2, 1, 1)
        self.checkBox_7 = QtWidgets.QCheckBox(ShiftDialog)
        self.checkBox_7.setObjectName("checkBox_7")
        self.gridLayout.addWidget(self.checkBox_7, 2, 1, 1, 1)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_2 = QtWidgets.QLabel(ShiftDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fromTime = QtWidgets.QTimeEdit(ShiftDialog)
        self.fromTime.setObjectName("fromTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.fromTime)
        self.label_3 = QtWidgets.QLabel(ShiftDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.untilTime = QtWidgets.QTimeEdit(ShiftDialog)
        self.untilTime.setObjectName("untilTime")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.untilTime)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShiftDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ShiftDialog)
        self.buttonBox.accepted.connect(ShiftDialog.accept)
        self.buttonBox.rejected.connect(ShiftDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ShiftDialog)

    def retranslateUi(self, ShiftDialog):
        _translate = QtCore.QCoreApplication.translate
        ShiftDialog.setWindowTitle(_translate("ShiftDialog", "Edit Shift"))
        self.label_4.setText(_translate("ShiftDialog", "Position"))
        self.label.setText(_translate("ShiftDialog", "Weekdays"))
        self.checkBox.setText(_translate("ShiftDialog", "Sunday"))
        self.checkBox_2.setText(_translate("ShiftDialog", "Monday"))
        self.checkBox_3.setText(_translate("ShiftDialog", "Tuesday"))
        self.checkBox_4.setText(_translate("ShiftDialog", "Wednesday"))
        self.checkBox_5.setText(_translate("ShiftDialog", "Thursday"))
        self.checkBox_6.setText(_translate("ShiftDialog", "Friday"))
        self.checkBox_7.setText(_translate("ShiftDialog", "Saturday"))
        self.label_2.setText(_translate("ShiftDialog", "From"))
        self.label_3.setText(_translate("ShiftDialog", "Until"))
