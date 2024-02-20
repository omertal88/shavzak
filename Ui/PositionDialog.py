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
        NewPositionDialog.resize(587, 289)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewPositionDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_5 = QtWidgets.QLabel(NewPositionDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.uidEdit = QtWidgets.QLineEdit(NewPositionDialog)
        self.uidEdit.setText("")
        self.uidEdit.setReadOnly(True)
        self.uidEdit.setObjectName("uidEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uidEdit)
        self.label_3 = QtWidgets.QLabel(NewPositionDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.positionNameEdit = QtWidgets.QLineEdit(NewPositionDialog)
        self.positionNameEdit.setObjectName("positionNameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.positionNameEdit)
        self.label = QtWidgets.QLabel(NewPositionDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(NewPositionDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.rolesWidget = RolesWidget(NewPositionDialog)
        self.rolesWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.rolesWidget.setObjectName("rolesWidget")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rolesWidget)
        self.label_4 = QtWidgets.QLabel(NewPositionDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.notPhysicalCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.notPhysicalCheck.setObjectName("notPhysicalCheck")
        self.gridLayout_2.addWidget(self.notPhysicalCheck, 1, 1, 1, 1)
        self.organicPlatoonsCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.organicPlatoonsCheck.setObjectName("organicPlatoonsCheck")
        self.gridLayout_2.addWidget(self.organicPlatoonsCheck, 1, 0, 1, 1)
        self.notCommanderCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.notCommanderCheck.setObjectName("notCommanderCheck")
        self.gridLayout_2.addWidget(self.notCommanderCheck, 2, 0, 1, 1)
        self.restingPositionCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.restingPositionCheck.setObjectName("restingPositionCheck")
        self.gridLayout_2.addWidget(self.restingPositionCheck, 2, 1, 1, 1)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.gridLayout_2)
        self.spacingNeededCheck = QtWidgets.QCheckBox(NewPositionDialog)
        self.spacingNeededCheck.setObjectName("spacingNeededCheck")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.spacingNeededCheck)
        self.widget = QtWidgets.QWidget(NewPositionDialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.spacingHourSpin = QtWidgets.QSpinBox(self.widget)
        self.spacingHourSpin.setEnabled(False)
        self.spacingHourSpin.setObjectName("spacingHourSpin")
        self.horizontalLayout.addWidget(self.spacingHourSpin)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.spacingMinuteSpin = QtWidgets.QSpinBox(self.widget)
        self.spacingMinuteSpin.setEnabled(False)
        self.spacingMinuteSpin.setObjectName("spacingMinuteSpin")
        self.horizontalLayout.addWidget(self.spacingMinuteSpin)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.manpowerSpin = QtWidgets.QSpinBox(NewPositionDialog)
        self.manpowerSpin.setMinimum(1)
        self.manpowerSpin.setObjectName("manpowerSpin")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.manpowerSpin)
        self.label_8 = QtWidgets.QLabel(NewPositionDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.prioritySpin = QtWidgets.QSpinBox(NewPositionDialog)
        self.prioritySpin.setObjectName("prioritySpin")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.prioritySpin)
        self.verticalLayout.addLayout(self.formLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewPositionDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(NewPositionDialog)
        self.buttonBox.accepted.connect(NewPositionDialog.accept)
        self.buttonBox.rejected.connect(NewPositionDialog.reject)
        self.spacingNeededCheck.toggled['bool'].connect(self.spacingHourSpin.setEnabled)
        self.spacingNeededCheck.toggled['bool'].connect(self.spacingMinuteSpin.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(NewPositionDialog)
        NewPositionDialog.setTabOrder(self.positionNameEdit, self.manpowerSpin)
        NewPositionDialog.setTabOrder(self.manpowerSpin, self.prioritySpin)
        NewPositionDialog.setTabOrder(self.prioritySpin, self.rolesWidget)
        NewPositionDialog.setTabOrder(self.rolesWidget, self.spacingNeededCheck)
        NewPositionDialog.setTabOrder(self.spacingNeededCheck, self.spacingHourSpin)
        NewPositionDialog.setTabOrder(self.spacingHourSpin, self.spacingMinuteSpin)
        NewPositionDialog.setTabOrder(self.spacingMinuteSpin, self.organicPlatoonsCheck)
        NewPositionDialog.setTabOrder(self.organicPlatoonsCheck, self.notPhysicalCheck)
        NewPositionDialog.setTabOrder(self.notPhysicalCheck, self.notCommanderCheck)
        NewPositionDialog.setTabOrder(self.notCommanderCheck, self.restingPositionCheck)
        NewPositionDialog.setTabOrder(self.restingPositionCheck, self.uidEdit)

    def retranslateUi(self, NewPositionDialog):
        _translate = QtCore.QCoreApplication.translate
        NewPositionDialog.setWindowTitle(_translate("NewPositionDialog", "עריכת עמדה"))
        self.label_5.setText(_translate("NewPositionDialog", "מזהה עמדה"))
        self.label_3.setText(_translate("NewPositionDialog", "שם העמדה"))
        self.label.setText(_translate("NewPositionDialog", "סד\"כ נדרש"))
        self.label_2.setText(_translate("NewPositionDialog", "בעלי תפקידים"))
        self.label_4.setText(_translate("NewPositionDialog", "מאפיינים"))
        self.notPhysicalCheck.setText(_translate("NewPositionDialog", "לא פיזי"))
        self.organicPlatoonsCheck.setText(_translate("NewPositionDialog", "מחלקות אורגניות"))
        self.notCommanderCheck.setText(_translate("NewPositionDialog", "לא מפקד"))
        self.restingPositionCheck.setText(_translate("NewPositionDialog", "עמדת מנוחה"))
        self.spacingNeededCheck.setText(_translate("NewPositionDialog", "הפסקה דרושה"))
        self.label_6.setText(_translate("NewPositionDialog", "שעות"))
        self.label_7.setText(_translate("NewPositionDialog", "דקות"))
        self.label_8.setText(_translate("NewPositionDialog", "קדימות בשיבוץ"))
from Ui.Promoted.RolesWidget import RolesWidget
