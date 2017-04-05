# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lookupBox2.ui'
#
# Created: Thu Mar 30 21:02:21 2017
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
    def ReSize(self,length,breath,Form):
        Form.resize(length,breath)
        Form.setMinimumSize(QtCore.QSize(length,breath))
        Form.setMaximumSize(QtCore.QSize(length,breath))
        Form.setStyleSheet(_fromUtf8("background:transparent;"))
        self.gridWidget = QtGui.QWidget(Form)
        self.gridWidget.setGeometry(QtCore.QRect(0, 0, length, breath))
        self.gridWidget.setMinimumSize(QtCore.QSize(length, breath))
        self.gridWidget.setMaximumSize(QtCore.QSize(length, breath))
        #return Form
    def setupUi(self, Form,text,error):
        Form.setObjectName(_fromUtf8("Form"))
       
        self.ReSize(340,150,Form)

        
        self.gridWidget.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.gridWidget.setObjectName(_fromUtf8("gridWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridWidget)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);"))
        out=""
        if not error:
            try :
                dictionary = PyDictionary()
                meanings = dictionary.meaning(text)
                out = ""
                for x in meanings:
                    out = out + "\nType :- " + x
                    for y in meanings[x]:
                        out = out + "\n*" + y
            except:
                self.ReSize(250,80,Form)
                out="""
                Maximum tries exceeded.
                Try again later
                """

            
        else:
            self.ReSize(250,80)
            out = """
            Word not found
            """
        self.plainTextEdit.setPlainText(out)

        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.gridLayout_2.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate(" ", " ", None))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

