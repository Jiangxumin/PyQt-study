#coding=utf-8
__author__ = 'Administrator'
import sys
from PyQt4 import QtGui,QtCore

class InputDialog(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self)

        self.setGeometry(300,300,350,80)#位置尺寸
        self.setWindowTitle("InputDialog")#标题
        self.button = QtGui.QPushButton("Dialog",self)#按钮部件
        self.button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.button.move(20,20)
        self.connect(self.button,QtCore.SIGNAL('clicked()'),self.showDialog)
        self.setFocus()

        self.label = QtGui.QLineEdit(self)#
        self.label.move(130,22)

    def showDialog(self):
        text,ok = QtGui.QInputDialog.getText(self,'Input Dialog',"Enter your name:")

        if ok:
            self.label.setText(unicode(text))

app = QtGui.QApplication(sys.argv)
incon = InputDialog()
incon.show()
sys.exit(app.exec_())
