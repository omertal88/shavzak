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
        Calendar.resize(565, 751)
        self.centralwidget = QtWidgets.QWidget(Calendar)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setMinimumDate(QtCore.QDate(2024, 9, 14))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout.addWidget(self.calendarWidget)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView_2.setObjectName("tableView_2")
        self.verticalLayout.addWidget(self.tableView_2)
        Calendar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calendar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 22))
        self.menubar.setObjectName("menubar")
        Calendar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calendar)
        self.statusbar.setObjectName("statusbar")
        Calendar.setStatusBar(self.statusbar)

        self.retranslateUi(Calendar)
        self.calendarWidget.clicked['QDate'].connect(Calendar.selectNewDate)
        QtCore.QMetaObject.connectSlotsByName(Calendar)

    def retranslateUi(self, Calendar):
        _translate = QtCore.QCoreApplication.translate
        Calendar.setWindowTitle(_translate("Calendar", "MainWindow"))
        self.label.setText(_translate("Calendar", "משמרות"))
        self.label_2.setText(_translate("Calendar", "כוח אדם"))
