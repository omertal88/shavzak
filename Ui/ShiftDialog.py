# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/ShiftDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ShiftDialog(object):
    def setupUi(self, ShiftDialog):
        ShiftDialog.setObjectName("ShiftDialog")
        ShiftDialog.setWindowModality(QtCore.Qt.WindowModal)
        ShiftDialog.resize(496, 390)
        self.verticalLayout = QtWidgets.QVBoxLayout(ShiftDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(ShiftDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.positionCombo = QtWidgets.QComboBox(ShiftDialog)
        self.positionCombo.setObjectName("positionCombo")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.positionCombo)
        self.label = QtWidgets.QLabel(ShiftDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.sundayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.sundayCheck.setObjectName("sundayCheck")
        self.gridLayout.addWidget(self.sundayCheck, 0, 0, 1, 1)
        self.mondayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.mondayCheck.setObjectName("mondayCheck")
        self.gridLayout.addWidget(self.mondayCheck, 0, 1, 1, 1)
        self.tuesdayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.tuesdayCheck.setObjectName("tuesdayCheck")
        self.gridLayout.addWidget(self.tuesdayCheck, 0, 2, 1, 1)
        self.wednesdayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.wednesdayCheck.setObjectName("wednesdayCheck")
        self.gridLayout.addWidget(self.wednesdayCheck, 1, 0, 1, 1)
        self.thursdayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.thursdayCheck.setObjectName("thursdayCheck")
        self.gridLayout.addWidget(self.thursdayCheck, 1, 1, 1, 1)
        self.fridayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.fridayCheck.setObjectName("fridayCheck")
        self.gridLayout.addWidget(self.fridayCheck, 1, 2, 1, 1)
        self.saturdayCheck = QtWidgets.QCheckBox(ShiftDialog)
        self.saturdayCheck.setObjectName("saturdayCheck")
        self.gridLayout.addWidget(self.saturdayCheck, 2, 0, 1, 1)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.gridLayout)
        self.label_2 = QtWidgets.QLabel(ShiftDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.fromTime = QtWidgets.QTimeEdit(ShiftDialog)
        self.fromTime.setObjectName("fromTime")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fromTime)
        self.label_3 = QtWidgets.QLabel(ShiftDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(ShiftDialog)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.durationHoursEdit = QtWidgets.QLineEdit(ShiftDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationHoursEdit.sizePolicy().hasHeightForWidth())
        self.durationHoursEdit.setSizePolicy(sizePolicy)
        self.durationHoursEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.durationHoursEdit.setObjectName("durationHoursEdit")
        self.horizontalLayout.addWidget(self.durationHoursEdit)
        self.label_6 = QtWidgets.QLabel(ShiftDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.durationMinutesEdit = QtWidgets.QLineEdit(ShiftDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.durationMinutesEdit.sizePolicy().hasHeightForWidth())
        self.durationMinutesEdit.setSizePolicy(sizePolicy)
        self.durationMinutesEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.durationMinutesEdit.setObjectName("durationMinutesEdit")
        self.horizontalLayout.addWidget(self.durationMinutesEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(ShiftDialog)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.stickToShiftCombo = QtWidgets.QComboBox(ShiftDialog)
        self.stickToShiftCombo.setObjectName("stickToShiftCombo")
        self.stickToShiftCombo.addItem("")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.stickToShiftCombo)
        self.label_8 = QtWidgets.QLabel(ShiftDialog)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_9 = QtWidgets.QLabel(ShiftDialog)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.validFromDatetime = QtWidgets.QDateTimeEdit(ShiftDialog)
        self.validFromDatetime.setObjectName("validFromDatetime")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.validFromDatetime)
        self.validUntilDatetime = QtWidgets.QDateTimeEdit(ShiftDialog)
        self.validUntilDatetime.setObjectName("validUntilDatetime")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.validUntilDatetime)
        self.label_10 = QtWidgets.QLabel(ShiftDialog)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.uidEdit = QtWidgets.QLineEdit(ShiftDialog)
        self.uidEdit.setReadOnly(True)
        self.uidEdit.setObjectName("uidEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uidEdit)
        self.label_11 = QtWidgets.QLabel(ShiftDialog)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.nicknameEdit = QtWidgets.QLineEdit(ShiftDialog)
        self.nicknameEdit.setObjectName("nicknameEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.nicknameEdit)
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
        ShiftDialog.setTabOrder(self.positionCombo, self.nicknameEdit)
        ShiftDialog.setTabOrder(self.nicknameEdit, self.sundayCheck)
        ShiftDialog.setTabOrder(self.sundayCheck, self.mondayCheck)
        ShiftDialog.setTabOrder(self.mondayCheck, self.tuesdayCheck)
        ShiftDialog.setTabOrder(self.tuesdayCheck, self.wednesdayCheck)
        ShiftDialog.setTabOrder(self.wednesdayCheck, self.thursdayCheck)
        ShiftDialog.setTabOrder(self.thursdayCheck, self.fridayCheck)
        ShiftDialog.setTabOrder(self.fridayCheck, self.saturdayCheck)
        ShiftDialog.setTabOrder(self.saturdayCheck, self.fromTime)
        ShiftDialog.setTabOrder(self.fromTime, self.durationHoursEdit)
        ShiftDialog.setTabOrder(self.durationHoursEdit, self.durationMinutesEdit)
        ShiftDialog.setTabOrder(self.durationMinutesEdit, self.stickToShiftCombo)
        ShiftDialog.setTabOrder(self.stickToShiftCombo, self.validFromDatetime)
        ShiftDialog.setTabOrder(self.validFromDatetime, self.validUntilDatetime)
        ShiftDialog.setTabOrder(self.validUntilDatetime, self.uidEdit)

    def retranslateUi(self, ShiftDialog):
        _translate = QtCore.QCoreApplication.translate
        ShiftDialog.setWindowTitle(_translate("ShiftDialog", "עריכת משמרת"))
        self.label_4.setText(_translate("ShiftDialog", "עמדה"))
        self.label.setText(_translate("ShiftDialog", "ימים"))
        self.sundayCheck.setText(_translate("ShiftDialog", "ראשון"))
        self.mondayCheck.setText(_translate("ShiftDialog", "שני"))
        self.tuesdayCheck.setText(_translate("ShiftDialog", "שלישי"))
        self.wednesdayCheck.setText(_translate("ShiftDialog", "רביעי"))
        self.thursdayCheck.setText(_translate("ShiftDialog", "חמישי"))
        self.fridayCheck.setText(_translate("ShiftDialog", "שישי"))
        self.saturdayCheck.setText(_translate("ShiftDialog", "שבת"))
        self.label_2.setText(_translate("ShiftDialog", "שעת התחלה"))
        self.label_3.setText(_translate("ShiftDialog", "זמן משמרת"))
        self.label_5.setText(_translate("ShiftDialog", "שעות"))
        self.label_6.setText(_translate("ShiftDialog", "דקות"))
        self.label_7.setText(_translate("ShiftDialog", "הצמד למשמרת"))
        self.stickToShiftCombo.setItemText(0, _translate("ShiftDialog", "ללא הצמדה"))
        self.label_8.setText(_translate("ShiftDialog", "החל מ-"))
        self.label_9.setText(_translate("ShiftDialog", "עד ל-"))
        self.validFromDatetime.setDisplayFormat(_translate("ShiftDialog", "d/M/yy hh:mm"))
        self.validUntilDatetime.setDisplayFormat(_translate("ShiftDialog", "d/M/yy hh:mm"))
        self.label_10.setText(_translate("ShiftDialog", "מזהה משמרת"))
        self.label_11.setText(_translate("ShiftDialog", "כינוי משמרת"))
