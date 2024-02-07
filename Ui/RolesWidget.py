# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui/RolesWidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RolesWidget(object):
    def setupUi(self, RolesWidget):
        RolesWidget.setObjectName("RolesWidget")
        RolesWidget.resize(370, 102)
        self.gridLayout = QtWidgets.QGridLayout(RolesWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.platoonCommanderCheck = QtWidgets.QCheckBox(RolesWidget)
        self.platoonCommanderCheck.setObjectName("platoonCommanderCheck")
        self.gridLayout.addWidget(self.platoonCommanderCheck, 0, 1, 1, 1)
        self.squadCommanderCheck = QtWidgets.QCheckBox(RolesWidget)
        self.squadCommanderCheck.setObjectName("squadCommanderCheck")
        self.gridLayout.addWidget(self.squadCommanderCheck, 0, 2, 1, 1)
        self.companyCommanderCheck = QtWidgets.QCheckBox(RolesWidget)
        self.companyCommanderCheck.setObjectName("companyCommanderCheck")
        self.gridLayout.addWidget(self.companyCommanderCheck, 0, 0, 1, 1)
        self.driverCheck = QtWidgets.QCheckBox(RolesWidget)
        self.driverCheck.setObjectName("driverCheck")
        self.gridLayout.addWidget(self.driverCheck, 2, 3, 1, 1)
        self.hamalRunnerCheck = QtWidgets.QCheckBox(RolesWidget)
        self.hamalRunnerCheck.setObjectName("hamalRunnerCheck")
        self.gridLayout.addWidget(self.hamalRunnerCheck, 2, 2, 1, 1)
        self.hamalistCheck = QtWidgets.QCheckBox(RolesWidget)
        self.hamalistCheck.setObjectName("hamalistCheck")
        self.gridLayout.addWidget(self.hamalistCheck, 2, 1, 1, 1)
        self.signallerCheck = QtWidgets.QCheckBox(RolesWidget)
        self.signallerCheck.setObjectName("signallerCheck")
        self.gridLayout.addWidget(self.signallerCheck, 2, 0, 1, 1)
        self.sniperCheck = QtWidgets.QCheckBox(RolesWidget)
        self.sniperCheck.setObjectName("sniperCheck")
        self.gridLayout.addWidget(self.sniperCheck, 1, 3, 1, 1)
        self.medicCheck = QtWidgets.QCheckBox(RolesWidget)
        self.medicCheck.setObjectName("medicCheck")
        self.gridLayout.addWidget(self.medicCheck, 1, 2, 1, 1)
        self.grenadeLauncherCheck = QtWidgets.QCheckBox(RolesWidget)
        self.grenadeLauncherCheck.setObjectName("grenadeLauncherCheck")
        self.gridLayout.addWidget(self.grenadeLauncherCheck, 1, 1, 1, 1)
        self.sharpshooterCheck = QtWidgets.QCheckBox(RolesWidget)
        self.sharpshooterCheck.setObjectName("sharpshooterCheck")
        self.gridLayout.addWidget(self.sharpshooterCheck, 1, 0, 1, 1)
        self.riflemanCheck = QtWidgets.QCheckBox(RolesWidget)
        self.riflemanCheck.setObjectName("riflemanCheck")
        self.gridLayout.addWidget(self.riflemanCheck, 0, 3, 1, 1)

        self.retranslateUi(RolesWidget)
        QtCore.QMetaObject.connectSlotsByName(RolesWidget)
        RolesWidget.setTabOrder(self.companyCommanderCheck, self.platoonCommanderCheck)
        RolesWidget.setTabOrder(self.platoonCommanderCheck, self.squadCommanderCheck)
        RolesWidget.setTabOrder(self.squadCommanderCheck, self.riflemanCheck)
        RolesWidget.setTabOrder(self.riflemanCheck, self.sharpshooterCheck)
        RolesWidget.setTabOrder(self.sharpshooterCheck, self.grenadeLauncherCheck)
        RolesWidget.setTabOrder(self.grenadeLauncherCheck, self.medicCheck)
        RolesWidget.setTabOrder(self.medicCheck, self.sniperCheck)
        RolesWidget.setTabOrder(self.sniperCheck, self.signallerCheck)
        RolesWidget.setTabOrder(self.signallerCheck, self.hamalistCheck)
        RolesWidget.setTabOrder(self.hamalistCheck, self.hamalRunnerCheck)
        RolesWidget.setTabOrder(self.hamalRunnerCheck, self.driverCheck)

    def retranslateUi(self, RolesWidget):
        _translate = QtCore.QCoreApplication.translate
        RolesWidget.setWindowTitle(_translate("RolesWidget", "תפקידים"))
        self.platoonCommanderCheck.setText(_translate("RolesWidget", "מ\"מ / סמל"))
        self.squadCommanderCheck.setText(_translate("RolesWidget", "מ\"כ"))
        self.companyCommanderCheck.setText(_translate("RolesWidget", "מ\"פ / סמ\"פ"))
        self.driverCheck.setText(_translate("RolesWidget", "נהג"))
        self.hamalRunnerCheck.setText(_translate("RolesWidget", "רץ חמ\"ל"))
        self.hamalistCheck.setText(_translate("RolesWidget", "חמ\"ליסט"))
        self.signallerCheck.setText(_translate("RolesWidget", "קשר"))
        self.sniperCheck.setText(_translate("RolesWidget", "צלף"))
        self.medicCheck.setText(_translate("RolesWidget", "חובש"))
        self.grenadeLauncherCheck.setText(_translate("RolesWidget", "מטול"))
        self.sharpshooterCheck.setText(_translate("RolesWidget", "קלע"))
        self.riflemanCheck.setText(_translate("RolesWidget", "חפ\"ש"))
