# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selection.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import atexit

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(801, 536)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(85, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.kek_b = QtWidgets.QPushButton(Dialog)
        self.kek_b.setGeometry(QtCore.QRect(10, 300, 341, 211))
        self.kek_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.kek_b.setObjectName("kek_b")
        self.Simp_b = QtWidgets.QPushButton(Dialog)
        self.Simp_b.setGeometry(QtCore.QRect(430, 300, 341, 211))
        self.Simp_b.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:1, stop:0 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));")
        self.Simp_b.setObjectName("Simp_b")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 331, 281))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/img/bjplogo.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(420, 10, 351, 281))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/img/inclogo.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.kek_b.setText(_translate("Dialog", "Bhartiya Janata Party"))
        self.Simp_b.setText(_translate("Dialog", "Indian National Congress"))

'''import bjp_rc
import images1_rc
import images_rc'''

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
