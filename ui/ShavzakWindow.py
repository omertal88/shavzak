# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ShavzakWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Shavzak(object):
    def setupUi(self, Shavzak):
        Shavzak.setObjectName("Shavzak")
        Shavzak.resize(598, 534)
        self.centralwidget = QtWidgets.QWidget(Shavzak)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.manpowerList = QtWidgets.QListWidget(self.centralwidget)
        self.manpowerList.setObjectName("manpowerList")
        self.verticalLayout.addWidget(self.manpowerList)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.addSoldierButton = QtWidgets.QPushButton(self.centralwidget)
        self.addSoldierButton.setObjectName("addSoldierButton")
        self.horizontalLayout_2.addWidget(self.addSoldierButton)
        self.removeSoldierButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeSoldierButton.setEnabled(False)
        self.removeSoldierButton.setObjectName("removeSoldierButton")
        self.horizontalLayout_2.addWidget(self.removeSoldierButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.positionsList = QtWidgets.QListWidget(self.centralwidget)
        self.positionsList.setObjectName("positionsList")
        self.verticalLayout_2.addWidget(self.positionsList)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addPositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.addPositionButton.setObjectName("addPositionButton")
        self.horizontalLayout_3.addWidget(self.addPositionButton)
        self.removePositionButton = QtWidgets.QPushButton(self.centralwidget)
        self.removePositionButton.setEnabled(False)
        self.removePositionButton.setObjectName("removePositionButton")
        self.horizontalLayout_3.addWidget(self.removePositionButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.shiftsList = QtWidgets.QListWidget(self.centralwidget)
        self.shiftsList.setObjectName("shiftsList")
        self.verticalLayout_3.addWidget(self.shiftsList)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.addShiftButton = QtWidgets.QPushButton(self.centralwidget)
        self.addShiftButton.setObjectName("addShiftButton")
        self.horizontalLayout_4.addWidget(self.addShiftButton)
        self.removeShiftButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeShiftButton.setEnabled(False)
        self.removeShiftButton.setObjectName("removeShiftButton")
        self.horizontalLayout_4.addWidget(self.removeShiftButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 112))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 341, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.fromDateTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.fromDateTime.setObjectName("fromDateTime")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fromDateTime)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.toDateTime = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.toDateTime.setObjectName("toDateTime")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.toDateTime)
        self.horizontalLayout.addLayout(self.formLayout)
        self.generateButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.generateButton.sizePolicy().hasHeightForWidth())
        self.generateButton.setSizePolicy(sizePolicy)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        self.verticalLayout_4.addWidget(self.groupBox)
        Shavzak.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Shavzak)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 22))
        self.menubar.setObjectName("menubar")
        Shavzak.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Shavzak)
        self.statusbar.setObjectName("statusbar")
        Shavzak.setStatusBar(self.statusbar)

        self.retranslateUi(Shavzak)
        self.addSoldierButton.clicked.connect(Shavzak.addNewSoldier)
        self.removeSoldierButton.clicked.connect(Shavzak.removeSoldier)
        self.addPositionButton.clicked.connect(Shavzak.addNewPosition)
        self.removePositionButton.clicked.connect(Shavzak.removePosition)
        self.addShiftButton.clicked.connect(Shavzak.addNewShift)
        self.removeShiftButton.clicked.connect(Shavzak.removeShift)
        self.manpowerList.doubleClicked['QModelIndex'].connect(Shavzak.addNewSoldier)
        self.positionsList.doubleClicked['QModelIndex'].connect(Shavzak.editPosition)
        self.shiftsList.doubleClicked['QModelIndex'].connect(Shavzak.editShift)
        QtCore.QMetaObject.connectSlotsByName(Shavzak)
        Shavzak.setTabOrder(self.manpowerList, self.addSoldierButton)
        Shavzak.setTabOrder(self.addSoldierButton, self.removeSoldierButton)
        Shavzak.setTabOrder(self.removeSoldierButton, self.positionsList)
        Shavzak.setTabOrder(self.positionsList, self.addPositionButton)
        Shavzak.setTabOrder(self.addPositionButton, self.removePositionButton)
        Shavzak.setTabOrder(self.removePositionButton, self.shiftsList)
        Shavzak.setTabOrder(self.shiftsList, self.addShiftButton)
        Shavzak.setTabOrder(self.addShiftButton, self.removeShiftButton)
        Shavzak.setTabOrder(self.removeShiftButton, self.fromDateTime)
        Shavzak.setTabOrder(self.fromDateTime, self.toDateTime)
        Shavzak.setTabOrder(self.toDateTime, self.generateButton)

    def retranslateUi(self, Shavzak):
        _translate = QtCore.QCoreApplication.translate
        Shavzak.setWindowTitle(_translate("Shavzak", "Shavzak Tool"))
        self.label.setText(_translate("Shavzak", "Manpower"))
        self.addSoldierButton.setText(_translate("Shavzak", "Add"))
        self.removeSoldierButton.setText(_translate("Shavzak", "Remove"))
        self.label_2.setText(_translate("Shavzak", "Positions"))
        self.addPositionButton.setText(_translate("Shavzak", "Add"))
        self.removePositionButton.setText(_translate("Shavzak", "Remove"))
        self.label_3.setText(_translate("Shavzak", "Shifts"))
        self.addShiftButton.setText(_translate("Shavzak", "Add"))
        self.removeShiftButton.setText(_translate("Shavzak", "Remove"))
        self.groupBox.setTitle(_translate("Shavzak", "Generator"))
        self.label_4.setText(_translate("Shavzak", "From"))
        self.label_5.setText(_translate("Shavzak", "To"))
        self.generateButton.setText(_translate("Shavzak", "Generate"))
