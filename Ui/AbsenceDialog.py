# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/AbsenceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AbsenceDialog(object):
    def setupUi(self, AbsenceDialog):
        AbsenceDialog.setObjectName("AbsenceDialog")
        AbsenceDialog.setWindowModality(QtCore.Qt.WindowModal)
        AbsenceDialog.resize(400, 169)
        self.formLayout = QtWidgets.QFormLayout(AbsenceDialog)
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(AbsenceDialog)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fromDateTime = QtWidgets.QDateTimeEdit(AbsenceDialog)
        self.fromDateTime.setObjectName("fromDateTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fromDateTime)
        self.label_5 = QtWidgets.QLabel(AbsenceDialog)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.untilDateTime = QtWidgets.QDateTimeEdit(AbsenceDialog)
        self.untilDateTime.setObjectName("untilDateTime")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.untilDateTime)
        self.buttonBox = QtWidgets.QDialogButtonBox(AbsenceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        self.label = QtWidgets.QLabel(AbsenceDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.commentEdit = QtWidgets.QLineEdit(AbsenceDialog)
        self.commentEdit.setObjectName("commentEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.commentEdit)
        self.label_2 = QtWidgets.QLabel(AbsenceDialog)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.uidEdit = QtWidgets.QLineEdit(AbsenceDialog)
        self.uidEdit.setReadOnly(True)
        self.uidEdit.setObjectName("uidEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uidEdit)

        self.retranslateUi(AbsenceDialog)
        self.buttonBox.accepted.connect(AbsenceDialog.accept)
        self.buttonBox.rejected.connect(AbsenceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AbsenceDialog)
        AbsenceDialog.setTabOrder(self.fromDateTime, self.untilDateTime)
        AbsenceDialog.setTabOrder(self.untilDateTime, self.commentEdit)
        AbsenceDialog.setTabOrder(self.commentEdit, self.uidEdit)

    def retranslateUi(self, AbsenceDialog):
        _translate = QtCore.QCoreApplication.translate
        AbsenceDialog.setWindowTitle(_translate("AbsenceDialog", "Dialog"))
        self.label_4.setText(_translate("AbsenceDialog", "תחילת היעדרות"))
        self.fromDateTime.setDisplayFormat(_translate("AbsenceDialog", "d/M/yyyy hh:mm"))
        self.label_5.setText(_translate("AbsenceDialog", "זמן סיום"))
        self.untilDateTime.setDisplayFormat(_translate("AbsenceDialog", "d/M/yyyy hh:mm"))
        self.label.setText(_translate("AbsenceDialog", "הערה"))
        self.label_2.setText(_translate("AbsenceDialog", "מס\"ד"))
