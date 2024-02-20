# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/PositionDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewPositionDialog(object):
    def setupUi(self, NewPositionDialog):
        NewPositionDialog.setObjectName("NewPositionDialog")
        NewPositionDialog.setWindowModality(QtCore.Qt.WindowModal)
        NewPositionDialog.resize(587, 261)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewPositionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(NewPositionDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.positionNameEdit = QtWidgets.QLineEdit(NewPositionDialog)
        self.positionNameEdit.setObjectName("positionNameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.positionNameEdit)
        self.label = QtWidgets.QLabel(NewPositionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.manpowerEdit = QtWidgets.QLineEdit(NewPositionDialog)
        self.manpowerEdit.setObjectName("manpowerEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.manpowerEdit)
        self.label_2 = QtWidgets.QLabel(NewPositionDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(NewPositionDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.notPhysicalCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.notPhysicalCheck.setObjectName("notPhysicalCheck")
        self.gridLayout_2.addWidget(self.notPhysicalCheck, 1, 1, 1, 1)
        self.mixPlatoonsCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.mixPlatoonsCheck.setObjectName("mixPlatoonsCheck")
        self.gridLayout_2.addWidget(self.mixPlatoonsCheck, 1, 0, 1, 1)
        self.noRestCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.noRestCheck.setObjectName("noRestCheck")
        self.gridLayout_2.addWidget(self.noRestCheck, 2, 0, 1, 1)
        self.notCommanderCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.notCommanderCheck.setObjectName("notCommanderCheck")
        self.gridLayout_2.addWidget(self.notCommanderCheck, 2, 1, 1, 1)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.gridLayout_2)
        self.label_5 = QtWidgets.QLabel(NewPositionDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.uidEdit = QtWidgets.QLineEdit(NewPositionDialog)
        self.uidEdit.setText("")
        self.uidEdit.setReadOnly(True)
        self.uidEdit.setObjectName("uidEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uidEdit)
        self.rolesWidget = RolesWidget(NewPositionDialog)
        self.rolesWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rolesWidget.setObjectName("rolesWidget")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rolesWidget)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewPositionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPositionDialog)
        self.buttonBox.accepted.connect(NewPositionDialog.accept)
        self.buttonBox.rejected.connect(NewPositionDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewPositionDialog)
        NewPositionDialog.setTabOrder(self.positionNameEdit, self.manpowerEdit)
        NewPositionDialog.setTabOrder(self.manpowerEdit, self.rolesWidget)
        NewPositionDialog.setTabOrder(self.rolesWidget, self.mixPlatoonsCheck)
        NewPositionDialog.setTabOrder(self.mixPlatoonsCheck, self.notPhysicalCheck)
        NewPositionDialog.setTabOrder(self.notPhysicalCheck, self.noRestCheck)
        NewPositionDialog.setTabOrder(self.noRestCheck, self.notCommanderCheck)
        NewPositionDialog.setTabOrder(self.notCommanderCheck, self.uidEdit)

    def retranslateUi(self, NewPositionDialog):
        _translate = QtCore.QCoreApplication.translate
        NewPositionDialog.setWindowTitle(_translate("NewPositionDialog", "עריכת עמדה"))
        self.label_3.setText(_translate("NewPositionDialog", "שם העמדה"))
        self.label.setText(_translate("NewPositionDialog", "סד\"כ נדרש"))
        self.label_2.setText(_translate("NewPositionDialog", "בעלי תפקידים"))
        self.label_4.setText(_translate("NewPositionDialog", "מאפיינים"))
        self.notPhysicalCheck.setText(_translate("NewPositionDialog", "לא פיזי"))
        self.mixPlatoonsCheck.setText(_translate("NewPositionDialog", "ערבוב מחלקות"))
        self.noRestCheck.setText(_translate("NewPositionDialog", "אין צורך במנוחה"))
        self.notCommanderCheck.setText(_translate("NewPositionDialog", "לא מפקד"))
        self.label_5.setText(_translate("NewPositionDialog", "מזהה עמדה"))
from Ui.Promoted.RolesWidget import RolesWidget
