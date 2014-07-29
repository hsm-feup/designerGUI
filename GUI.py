# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created: Tue Jul 29 18:22:31 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dlgMain(object):
    def setupUi(self, dlgMain):
        dlgMain.setObjectName(_fromUtf8("dlgMain"))
        dlgMain.resize(390, 255)
        self.gridLayout = QtGui.QGridLayout(dlgMain)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.chkLED = QtGui.QCheckBox(dlgMain)
        self.chkLED.setObjectName(_fromUtf8("chkLED"))
        self.gridLayout.addWidget(self.chkLED, 0, 0, 1, 1)
        self.edtCmd = QtGui.QLineEdit(dlgMain)
        self.edtCmd.setObjectName(_fromUtf8("edtCmd"))
        self.gridLayout.addWidget(self.edtCmd, 1, 0, 1, 1)
        self.butSend = QtGui.QPushButton(dlgMain)
        self.butSend.setObjectName(_fromUtf8("butSend"))
        self.gridLayout.addWidget(self.butSend, 1, 1, 1, 1)
        self.txtLog = QtGui.QTextEdit(dlgMain)
        self.txtLog.setObjectName(_fromUtf8("txtLog"))
        self.gridLayout.addWidget(self.txtLog, 2, 0, 1, 2)

        self.retranslateUi(dlgMain)
        QtCore.QMetaObject.connectSlotsByName(dlgMain)

    def retranslateUi(self, dlgMain):
        dlgMain.setWindowTitle(_translate("dlgMain", "Main GUI", None))
        self.chkLED.setText(_translate("dlgMain", "LED", None))
        self.butSend.setText(_translate("dlgMain", "Send", None))

