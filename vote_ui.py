# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vote.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
import atexit
import timer
#import session
import DBQuery as dbq




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.FullFrame = QtWidgets.QFrame(self.centralwidget)
        self.FullFrame.setGeometry(QtCore.QRect(0, 0, 811, 661))
        self.FullFrame.setMouseTracking(False)
        self.FullFrame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(85, 170, 255, 255));")
        self.FullFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FullFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FullFrame.setObjectName("FullFrame")


        self.Name_e = QtWidgets.QTextEdit(self.FullFrame)
        self.Name_e.setGeometry(QtCore.QRect(280, 110, 201, 41))
        self.Name_e.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.Name_e.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Name_e.setLineWidth(0)
        self.Name_e.setOverwriteMode(False)
        self.Name_e.setObjectName("Name_e")
        
        self.Name_l = QtWidgets.QLabel(self.FullFrame)
        self.Name_l.setGeometry(QtCore.QRect(300, 70, 171, 31))
        self.Name_l.setStyleSheet("")
        self.Name_l.setObjectName("Name_l")


        self.DOB_l = QtWidgets.QLabel(self.FullFrame)
        self.DOB_l.setGeometry(QtCore.QRect(260, 220, 261, 31))
        self.DOB_l.setStyleSheet("")
        self.DOB_l.setObjectName("DOB_l")
        
        self.DOB_e = QtWidgets.QDateEdit(self.FullFrame)
        self.DOB_e.setGeometry(QtCore.QRect(280, 260, 201, 22))
        self.DOB_e.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:1 rgba(255, 255, 255, 255));")
        self.DOB_e.setObjectName("DOB_e")
                

        self.ID_l = QtWidgets.QLabel(self.FullFrame)
        self.ID_l.setGeometry(QtCore.QRect(280, 310, 201, 31))
        self.ID_l.setStyleSheet("")
        self.ID_l.setObjectName("ID_l")
        
        self.ID_e = QtWidgets.QTextEdit(self.FullFrame)
        self.ID_e.setGeometry(QtCore.QRect(280, 350, 211, 31))
        self.ID_e.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));")
        self.ID_e.setObjectName("ID_e")
        

        self.Submit_b = QtWidgets.QPushButton(self.FullFrame)
        self.Submit_b.setGeometry(QtCore.QRect(310, 500, 151, 41))
        self.Submit_b.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 255));")
        self.Submit_b.setAutoRepeatInterval(100)
        self.Submit_b.setObjectName("Submit_b")
        self.Submit_b.clicked.connect(self.finalizeQuery)
        


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name_e.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.Name_l.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#000000;\">Enter your Name :</span></p></body></html>"))
        self.DOB_l.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter your Date of Birth :</span></p></body></html>"))
        
        
        self.ID_l.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Enter your Voter ID :</span></p></body></html>"))
        self.Submit_b.setText(_translate("MainWindow", "Give Vote!"))

    def finalizeQuery(self):
        parsedName = self.Name_e.toPlainText()
        parsedVID = self.ID_e.toPlainText()
        pDate = self.DOB_e.date()
        parsedDate = pDate.toPyDate()
        self.Name_e.clear()
        self.ID_e.clear()
        self.DOB_e.clear()
        with open('test.txt','w') as f:
            f.write(parsedName + "\t" + str(parsedDate) + "\t" + parsedVID)     #CANT RETURN OBJECTS SO PARSING IT TO A TEMP FILE

        #print(dbq.verify(parsedName,parsedDate,parsedVID))
        




def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    time_left = timer.MyMainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


