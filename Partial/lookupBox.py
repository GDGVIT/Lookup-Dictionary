'Author - Ujjwal Ayyangar'
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lookupBox.ui'
#
# Created: Mon Feb 27 23:55:13 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PyDictionary import PyDictionary
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

class Ui_Form(object):
    def setupUi(self, Form,text):
    	
    	Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(340, 150)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(_fromUtf8(""))
        self.gridLayoutWidget = QtGui.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 341, 151))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.textEdit = QtGui.QTextEdit(self.gridLayoutWidget)
        self.textEdit.setStyleSheet(_fromUtf8("background-image: url(:/white.jpg);\n""font: 12pt \"Verdana\";"))
	dictionary = PyDictionary()
	meanings = dictionary.meaning(text)
	out=""
	for x in meanings:
		out=out+"Type :- "+x
		for y in meanings[x]:
			out=out+"\n"+y

		


	
	self.textEdit.setPlainText(out)
	self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

    def keyPressEvent(self, event):
    	if event.key() == QtCore.Qt.Key_Escape: 
        	self.close()
		

		




import image2_rc
