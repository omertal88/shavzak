# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/Calendar.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calendar(object):
    def setupUi(self, Calendar):
        Calendar.setObjectName("Calendar")
        Calendar.resize(495, 566)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Res/soldier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Calendar.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Calendar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2023, 9, 14))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_2.addWidget(self.calendarWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.addAssignmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.addAssignmentButton.setObjectName("addAssignmentButton")
        self.verticalLayout.addWidget(self.addAssignmentButton)
        self.removeAssignmentButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeAssignmentButton.setObjectName("removeAssignmentButton")
        self.verticalLayout.addWidget(self.removeAssignmentButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.assignmentsView = QtWidgets.QTableView(self.centralwidget)
        self.assignmentsView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.assignmentsView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.assignmentsView.setObjectName("assignmentsView")
        self.horizontalLayout.addWidget(self.assignmentsView)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.manpowerListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.manpowerListWidget.setObjectName("manpowerListWidget")
        self.verticalLayout_2.addWidget(self.manpowerListWidget)
        Calendar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calendar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName("menubar")
        Calendar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calendar)
        self.statusbar.setObjectName("statusbar")
        Calendar.setStatusBar(self.statusbar)

        self.retranslateUi(Calendar)
        self.addAssignmentButton.clicked.connect(Calendar.addAssignment)
        self.removeAssignmentButton.clicked.connect(Calendar.removeAssignment)
        self.assignmentsView.doubleClicked['QModelIndex'].connect(Calendar.editAssignment)
        self.calendarWidget.selectionChanged.connect(Calendar.reloadSelectedDate)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "שיבוץ קרבי"))
        self.label.setText(_translate("Calendar", "משימות"))
        self.addAssignmentButton.setText(_translate("Calendar", "הוסף"))
        self.removeAssignmentButton.setText(_translate("Calendar", "הסר"))
        self.label_2.setText(_translate("Calendar", "כוח אדם"))
from Ui import resources_rc
