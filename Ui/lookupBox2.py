# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lookupBox2.ui'
#
# Created: Thu Mar 30 21:02:21 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PyDictionary import PyDictionary
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import * 
from PyQt4.QtCore import * 

word =""

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

class RoundWidget(QtGui.QWidget):
    """ docstring for ControlBar"""
    def __init__(self,parent=None):
        super(RoundWidget, self).__init__(parent)
        self.resize(340,150)
	
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowTitle("QLinearGradient Vertical Gradient ")
	self.setMinimumSize(QtCore.QSize(330, 10))
        self.setMaximumSize(QtCore.QSize(340, 150))
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.buildUi()   

    def paintEvent(self, ev):
        painter = QtGui.QPainter(self)
	painter.setPen(QtGui.QColor(250, 250, 250))
        gradient = QtGui.QLinearGradient(QtCore.QRectF(self.rect()).topLeft(),QtCore.QRectF(self.rect()).bottomLeft())
        gradient.setColorAt(0.0,QColor(250, 240, 240))#Qt.white)
        gradient.setColorAt(0.4,QColor(250, 240, 240))# QtCore.Qt.white)
        gradient.setColorAt(0.7,QColor(250, 240, 240))# QtCore.Qt.white)
        painter.setBrush(gradient)
        painter.drawRoundedRect(0, 0, 340, 150, 15.0, 15.0)

    def buildUi(self):
    	global word
        self.gridlayout = QtGui.QGridLayout()
	title=QLabel()
	titleFont = QtGui.QFont("Verdana", 12, QtGui.QFont.Bold)
	title.setFont(titleFont)
	title.setText(word.title())
	title.setAlignment(QtCore.Qt.AlignHCenter)
	self.gridlayout.addWidget(title)#,0,0,1,1)


        l=QtGui.QTextEdit()
        #font=QtGui.QFont()
        #font.setFamily(_fromUtf8("Baskerville Old Face"))
        dictionary=PyDictionary()
	
        meanings=dictionary.meaning(word)
        Nouns=[]
        Verbs=[]
        for types in meanings:
            if types == "Noun":
                Nouns=meanings[u'Noun']
            elif types == "Verb":
                Verbs = meanings[u'Verb']
        

        out=""


        for x in meanings:
        	out=out+'<b><font face="Comic sans MS" color="red">'+x.upper()+'</font></b><br/>'
                for y in meanings[x]:
                	out=out+ '<br/><font face="Comic sans MS">• ' + y+'</font><br/>'
	l.setHtml(out)
        #l.setHtml("<h3> HEY </h3>")
	#a = QtCore.QString('<b>HEY</b>')
	#l.insertHtml(a)
            
        #l.setPlainText(out)    
        self.gridlayout.addWidget(l)#,0,0,1,1)
        self.setLayout(self.gridlayout)

class Ui_Form(object):
    
    def ReSize(self,length,breath):
    	self.Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.Form.resize(length,breath)
        self.Form.setMinimumSize(QtCore.QSize(length,breath))
        self.Form.setMaximumSize(QtCore.QSize(length,breath))
        self.Form.setStyleSheet(_fromUtf8("background:transparent;"))
	self.gridWidget = RoundWidget(self.Form)

    def setupUi(self, Form,text,err):
    	global word
	word=text
        self.Form=Form
        Form.setObjectName(_fromUtf8("Form"))
        self.ReSize(340,150)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate(" ", " ", None))

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
