import os, sys, index, create, dab
from PyQt5 import QtGui, QtCore, QtWidgets
import qtawesome as qta

class CreateUI(QtWidgets.QWidget):
    #Globals
    msg = None

    def __init__(self):
        super(CreateUI, self).__init__()
        self.setGeometry(50,50,400,100)
        self.setWindowTitle("Connect")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint) #Use this for a frameless window. Will be used later!
        self.center()

        tbLay = QtWidgets.QHBoxLayout()
        tbLay.setAlignment(QtCore.Qt.AlignRight)
        tbLay.setContentsMargins(0,0,0,0)
        tbWid = QtWidgets.QWidget()
        tbWid.setObjectName("titlebar")
        tbWid.setLayout(tbLay)

        mini = QtWidgets.QPushButton(qta.icon("fa.minus", color="#f9f9f9"), "")
        mini.setObjectName("minimize")
        mini.setMinimumSize(QtCore.QSize(30,30))
        #mini.clicked.connect(CreateUI.minimize(self))
        tbLay.addWidget(mini)

        quitBtn = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMinimumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        tbLay.addWidget(quitBtn)
        
        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setContentsMargins(0,0,0,0)
        addressLay = QtWidgets.QGridLayout()
        mainLay.addWidget(tbWid)
        mainLay.addLayout(addressLay)

        #Connection details input
        leHostname = QtWidgets.QLineEdit("")
        leHostname.setPlaceholderText("Hostname")
        addressLay.addWidget(leHostname,0,0)

        lePort = QtWidgets.QLineEdit("3306")
        lePort.setValidator(QtGui.QIntValidator())
        lePort.setPlaceholderText("Port")
        addressLay.addWidget(lePort,0,1)

        leUsername = QtWidgets.QLineEdit("")
        leUsername.setPlaceholderText("Username")
        mainLay.addWidget(leUsername)

        lePassword = QtWidgets.QLineEdit("")
        lePassword.setPlaceholderText("Password")
        lePassword.setEchoMode(2)
        mainLay.addWidget(lePassword)

        leDatabase = QtWidgets.QLineEdit("")
        leDatabase.setPlaceholderText("Database")
        mainLay.addWidget(leDatabase)

        leCryptPass = QtWidgets.QLineEdit("")
        leCryptPass.setPlaceholderText("Encryption Password")
        leCryptPass.setEchoMode(2)
        mainLay.addWidget(leCryptPass)

        btnConnect = QtWidgets.QPushButton("Connect")
        btnConnect.setObjectName("btnConnect")
        btnConnect.clicked.connect(lambda:CreateUI.connect(
            self, username=leUsername.text(), thePassword=lePassword.text(), address=leHostname.text(), thePort=lePort.text(), theDatabase=leDatabase.text()))
        mainLay.addWidget(btnConnect)

        CreateUI.msg = QtWidgets.QMessageBox()

        self.setLayout(mainLay)

    #Connect to the database and raise an error when failed
    def connect(self, username, thePassword, address, thePort, theDatabase):
        dab.DatabaseActions.connect(
            self, username, thePassword, address, thePort, theDatabase)

    #Centers the window at the start
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
    
    #When the connect dialog is closed quit the app
    def closeEvent(self, event):
        quit()

    #Method for minimizing the dialog
    def minimize(self):
        self.showMinimized()
    


    #Methods for moving the window with a custom titlebar
    def mousePressEvent(self, event):
        global dragging
        global clickPos
        clickPos = event.pos()
        if event.buttons() == QtCore.Qt.LeftButton:
            dragging = True

    def mouseReleaseEvent(self, event):
        global dragging
        dragging = False

    def mouseMoveEvent(self, event):
        global dragging
        global clickPos
        if dragging and clickPos.y() < 121:
            self.move(self.pos() + (event.pos() - clickPos))

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = CreateUI()
    gui.show()
    app.exec_()