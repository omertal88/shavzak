# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/SoldierDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SoldierDialog(object):
    def setupUi(self, SoldierDialog):
        SoldierDialog.setObjectName("SoldierDialog")
        SoldierDialog.setWindowModality(QtCore.Qt.WindowModal)
        SoldierDialog.resize(623, 444)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(SoldierDialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(SoldierDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pnEdit = QtWidgets.QLineEdit(SoldierDialog)
        self.pnEdit.setObjectName("pnEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pnEdit)
        self.label = QtWidgets.QLabel(SoldierDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.soldierNameEdit = QtWidgets.QLineEdit(SoldierDialog)
        self.soldierNameEdit.setObjectName("soldierNameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.soldierNameEdit)
        self.label_2 = QtWidgets.QLabel(SoldierDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.platoonCombo = QtWidgets.QComboBox(SoldierDialog)
        self.platoonCombo.setObjectName("platoonCombo")
        self.platoonCombo.addItem("")
        self.platoonCombo.addItem("")
        self.platoonCombo.addItem("")
        self.platoonCombo.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.platoonCombo)
        self.label_6 = QtWidgets.QLabel(SoldierDialog)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.telephoneEdit = QtWidgets.QLineEdit(SoldierDialog)
        self.telephoneEdit.setObjectName("telephoneEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.telephoneEdit)
        self.label_3 = QtWidgets.QLabel(SoldierDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.rolesWidget = RolesWidget(SoldierDialog)
        self.rolesWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rolesWidget.setObjectName("rolesWidget")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.rolesWidget)
        self.label_7 = QtWidgets.QLabel(SoldierDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.commentEdit = QtWidgets.QLineEdit(SoldierDialog)
        self.commentEdit.setObjectName("commentEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.commentEdit)
        self.label_4 = QtWidgets.QLabel(SoldierDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.absencesView = QtWidgets.QTableView(SoldierDialog)
        self.absencesView.setMinimumSize(QtCore.QSize(0, 140))
        self.absencesView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.absencesView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.absencesView.setObjectName("absencesView")
        self.verticalLayout.addWidget(self.absencesView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addAbsenceButton = QtWidgets.QPushButton(SoldierDialog)
        self.addAbsenceButton.setObjectName("addAbsenceButton")
        self.horizontalLayout.addWidget(self.addAbsenceButton)
        self.removeAbsenceButton = QtWidgets.QPushButton(SoldierDialog)
        self.removeAbsenceButton.setObjectName("removeAbsenceButton")
        self.horizontalLayout.addWidget(self.removeAbsenceButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.label_8 = QtWidgets.QLabel(SoldierDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.manualAssignCheck = QtWidgets.QCheckBox(SoldierDialog)
        self.manualAssignCheck.setObjectName("manualAssignCheck")
        self.gridLayout.addWidget(self.manualAssignCheck, 0, 0, 1, 1)
        self.noPhysicalCheck = QtWidgets.QCheckBox(SoldierDialog)
        self.noPhysicalCheck.setObjectName("noPhysicalCheck")
        self.gridLayout.addWidget(self.noPhysicalCheck, 0, 1, 1, 1)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SoldierDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(SoldierDialog)
        self.buttonBox.accepted.connect(SoldierDialog.accept)
        self.buttonBox.rejected.connect(SoldierDialog.reject)
        self.addAbsenceButton.clicked.connect(SoldierDialog.addAbsence)
        self.removeAbsenceButton.clicked.connect(SoldierDialog.removeAbsence)
        QtCore.QMetaObject.connectSlotsByName(SoldierDialog)
        SoldierDialog.setTabOrder(self.pnEdit, self.soldierNameEdit)
        SoldierDialog.setTabOrder(self.soldierNameEdit, self.platoonCombo)
        SoldierDialog.setTabOrder(self.platoonCombo, self.telephoneEdit)
        SoldierDialog.setTabOrder(self.telephoneEdit, self.rolesWidget)
        SoldierDialog.setTabOrder(self.rolesWidget, self.commentEdit)
        SoldierDialog.setTabOrder(self.commentEdit, self.addAbsenceButton)
        SoldierDialog.setTabOrder(self.addAbsenceButton, self.removeAbsenceButton)

    def retranslateUi(self, SoldierDialog):
        _translate = QtCore.QCoreApplication.translate
        SoldierDialog.setWindowTitle(_translate("SoldierDialog", "עריכת חייל"))
        self.label_5.setText(_translate("SoldierDialog", "מ.א"))
        self.label.setText(_translate("SoldierDialog", "שם החייל"))
        self.label_2.setText(_translate("SoldierDialog", "מחלקה"))
        self.platoonCombo.setItemText(0, _translate("SoldierDialog", "1"))
        self.platoonCombo.setItemText(1, _translate("SoldierDialog", "2"))
        self.platoonCombo.setItemText(2, _translate("SoldierDialog", "3"))
        self.platoonCombo.setItemText(3, _translate("SoldierDialog", "מפל\"ג"))
        self.label_6.setText(_translate("SoldierDialog", "מספר טלפון"))
        self.label_3.setText(_translate("SoldierDialog", "תפקיד"))
        self.label_7.setText(_translate("SoldierDialog", "הערות"))
        self.label_4.setText(_translate("SoldierDialog", "היעדרויות"))
        self.addAbsenceButton.setText(_translate("SoldierDialog", "הוסף היעדרות"))
        self.removeAbsenceButton.setText(_translate("SoldierDialog", "הסר היעדרות"))
        self.label_8.setText(_translate("SoldierDialog", "מאפיינים"))
        self.manualAssignCheck.setText(_translate("SoldierDialog", "שיבוץ ידני בלבד"))
        self.noPhysicalCheck.setText(_translate("SoldierDialog", "לא משימות פיזיות"))
from Ui.Promoted.RolesWidget import RolesWidget
