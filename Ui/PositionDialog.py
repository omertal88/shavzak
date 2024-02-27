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
        NewPositionDialog.resize(587, 413)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(NewPositionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
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
        self.frame = QtWidgets.QFrame(NewPositionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_17 = QtWidgets.QLabel(self.frame)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 4, 1, 1)
        self.platoonCommanderSpin = QtWidgets.QSpinBox(self.frame)
        self.platoonCommanderSpin.setObjectName("platoonCommanderSpin")
        self.gridLayout.addWidget(self.platoonCommanderSpin, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 4, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 0, 1, 1)
        self.squadCommanderSpin = QtWidgets.QSpinBox(self.frame)
        self.squadCommanderSpin.setObjectName("squadCommanderSpin")
        self.gridLayout.addWidget(self.squadCommanderSpin, 0, 5, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 4, 1, 1)
        self.companyCommanderSpin = QtWidgets.QSpinBox(self.frame)
        self.companyCommanderSpin.setObjectName("companyCommanderSpin")
        self.gridLayout.addWidget(self.companyCommanderSpin, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 3, 2, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 4, 1, 1)
        self.sharpshooterSpin = QtWidgets.QSpinBox(self.frame)
        self.sharpshooterSpin.setObjectName("sharpshooterSpin")
        self.gridLayout.addWidget(self.sharpshooterSpin, 1, 1, 1, 1)
        self.sniperSpin = QtWidgets.QSpinBox(self.frame)
        self.sniperSpin.setObjectName("sniperSpin")
        self.gridLayout.addWidget(self.sniperSpin, 2, 1, 1, 1)
        self.hamalRunnerSpin = QtWidgets.QSpinBox(self.frame)
        self.hamalRunnerSpin.setObjectName("hamalRunnerSpin")
        self.gridLayout.addWidget(self.hamalRunnerSpin, 3, 1, 1, 1)
        self.grenadeLauncherSpin = QtWidgets.QSpinBox(self.frame)
        self.grenadeLauncherSpin.setObjectName("grenadeLauncherSpin")
        self.gridLayout.addWidget(self.grenadeLauncherSpin, 1, 3, 1, 1)
        self.signallerSpin = QtWidgets.QSpinBox(self.frame)
        self.signallerSpin.setObjectName("signallerSpin")
        self.gridLayout.addWidget(self.signallerSpin, 2, 3, 1, 1)
        self.driverSpin = QtWidgets.QSpinBox(self.frame)
        self.driverSpin.setObjectName("driverSpin")
        self.gridLayout.addWidget(self.driverSpin, 3, 3, 1, 1)
        self.medicSpin = QtWidgets.QSpinBox(self.frame)
        self.medicSpin.setObjectName("medicSpin")
        self.gridLayout.addWidget(self.medicSpin, 1, 5, 1, 1)
        self.hamalistSpin = QtWidgets.QSpinBox(self.frame)
        self.hamalistSpin.setObjectName("hamalistSpin")
        self.gridLayout.addWidget(self.hamalistSpin, 2, 5, 1, 1)
        self.riflemanSpin = QtWidgets.QSpinBox(self.frame)
        self.riflemanSpin.setObjectName("riflemanSpin")
        self.gridLayout.addWidget(self.riflemanSpin, 3, 5, 1, 1)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.frame)
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
        NewPositionDialog.setTabOrder(self.prioritySpin, self.companyCommanderSpin)
        NewPositionDialog.setTabOrder(self.companyCommanderSpin, self.platoonCommanderSpin)
        NewPositionDialog.setTabOrder(self.platoonCommanderSpin, self.squadCommanderSpin)
        NewPositionDialog.setTabOrder(self.squadCommanderSpin, self.sharpshooterSpin)
        NewPositionDialog.setTabOrder(self.sharpshooterSpin, self.grenadeLauncherSpin)
        NewPositionDialog.setTabOrder(self.grenadeLauncherSpin, self.medicSpin)
        NewPositionDialog.setTabOrder(self.medicSpin, self.sniperSpin)
        NewPositionDialog.setTabOrder(self.sniperSpin, self.signallerSpin)
        NewPositionDialog.setTabOrder(self.signallerSpin, self.hamalistSpin)
        NewPositionDialog.setTabOrder(self.hamalistSpin, self.hamalRunnerSpin)
        NewPositionDialog.setTabOrder(self.hamalRunnerSpin, self.driverSpin)
        NewPositionDialog.setTabOrder(self.driverSpin, self.riflemanSpin)
        NewPositionDialog.setTabOrder(self.riflemanSpin, self.spacingNeededCheck)
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
        self.label_17.setText(_translate("NewPositionDialog", "חמליסט"))
        self.label_16.setText(_translate("NewPositionDialog", "קשר"))
        self.label_11.setText(_translate("NewPositionDialog", "מ\"כ"))
        self.label_15.setText(_translate("NewPositionDialog", "צלף"))
        self.label_14.setText(_translate("NewPositionDialog", "חובש"))
        self.label_13.setText(_translate("NewPositionDialog", "מטול"))
        self.label_12.setText(_translate("NewPositionDialog", "קלע"))
        self.label_10.setText(_translate("NewPositionDialog", "מ\"מ / סמ\"ח"))
        self.label_9.setText(_translate("NewPositionDialog", "מ\"פ / סמ\"פ"))
        self.label_18.setText(_translate("NewPositionDialog", "רץ חמל"))
        self.label_19.setText(_translate("NewPositionDialog", "נהג"))
        self.label_20.setText(_translate("NewPositionDialog", "חפ\"ש"))
