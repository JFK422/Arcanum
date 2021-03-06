import qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets
from components import crypt, dab
from components.uiElements import seperator
from components.uiElements.tabs import passwords

class CreateUI(QtWidgets.QWidget):
    def setup(self, passIndex, name, lastChanged, generated, email="", username="", twoFa="False", comment=""):
        #Main layouts and layout widgets
        lMain = QtWidgets.QGridLayout()
        lMain.setContentsMargins(0,0,0,0)
        gMain = QtWidgets.QGridLayout()
        gMain.setContentsMargins(10,10,10,10)
        lMain.addLayout(gMain, 1, 0)
        wMain = QtWidgets.QWidget()
        wMain.setObjectName("passSlate")
        vBack = QtWidgets.QVBoxLayout()
        vBack.setContentsMargins(0,0,0,0)

        #put everything into self so it can be acessed independantly form other passItems
        self.index = passIndex
        self.name = name
        self.lastChanged = lastChanged
        self.generated = generated
        self.email = email
        self.username = username
        self.twoFa = twoFa
        self.comment = comment

        #Banner to the Password currently only in placeholder version! Will be removed later!
        iBanner = QtWidgets.QLabel()

        #There is a layout (lmain) which holds the banner and the delete button so the delet btn can be directly in the corner
        iBanner.setPixmap(QtGui.QPixmap("./resources/icons/icon256.png").scaled(128, 128, QtCore.Qt.KeepAspectRatio))
        lMain.addWidget(iBanner, 0, 0)
        
        vQuit = QtWidgets.QVBoxLayout()
        vQuit.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignRight)
        vQuit.setContentsMargins(0,0,0,0)

        #Delete and Edit buttons
        btnDel = QtWidgets.QPushButton(qta.icon("fa.times", color="#f9f9f9"), "")
        btnDel.setObjectName("quitBtn")
        btnDel.setMinimumSize(QtCore.QSize(30,30))
        btnDel.clicked.connect(lambda:CreateUI.delPassword(self))
        vQuit.addWidget(btnDel)

        btnEdit = QtWidgets.QPushButton(qta.icon("fa.edit", color="#f9f9f9"), "")
        btnEdit.setMinimumSize(QtCore.QSize(30,30))
        btnEdit.clicked.connect(lambda:passwords.Passwords.editPassword(self))
        vQuit.addWidget(btnEdit)

        wQuit = QtWidgets.QWidget()
        wQuit.setLayout(vQuit)
        lMain.addWidget(wQuit, 0, 1)

        #Create the widgets to display the main data
        lPassIndexLabel = QtWidgets.QLabel("Index:")
        lPassIndexLabel.setObjectName("passLabel")
        gMain.addWidget(lPassIndexLabel, 1, 0)
        global lPassIndex
        lPassIndex = QtWidgets.QLabel(str(passIndex))
        lPassIndex.setObjectName("passLabel")
        gMain.addWidget(lPassIndex, 1, 1)

        lNameLabel = QtWidgets.QLabel("Name:")
        lNameLabel.setObjectName("passLabel")
        gMain.addWidget(lNameLabel, 2, 0)
        lName = QtWidgets.QLabel(name)
        lName.setObjectName("passLabel")
        lName.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        gMain.addWidget(lName, 2, 1)

        if email != "":
            lEmailLabel = QtWidgets.QLabel("Email:")
            lEmailLabel.setObjectName("passLabel")
            gMain.addWidget(lEmailLabel, 3, 0)
            lEmail = QtWidgets.QLabel("")
            lEmail.setText(email)
            lEmail.setObjectName("passLabel")
            lEmail.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            gMain.addWidget(lEmail, 3, 1)

        if username != "":
            lUsernameLabel = QtWidgets.QLabel("Username:")
            lUsernameLabel.setObjectName("passLabel")
            gMain.addWidget(lUsernameLabel, 4, 0)
            lUsername = QtWidgets.QLabel("")
            lUsername.setText(username)
            lUsername.setObjectName("passLabel")
            lUsername.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            gMain.addWidget(lUsername, 4, 1)
        
        lPasswordLabel = QtWidgets.QLabel("Password:")
        lPasswordLabel.setObjectName("passLabel")
        gMain.addWidget(lPasswordLabel, 5, 0)
        data = dab.DatabaseActions.read(self, table="passTable", row=passIndex)
        lPassword = QtWidgets.QLabel("")
        lPassword.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        
        lPassword.setText(str(crypt.Encryption.decrypt(self, data[7])[0]))

        gMain.addWidget(lPassword, 5, 1)

        #Use later to decrypt the password on demand
        """
        passBtn = passButton()
        passBtn.setup(passIndex)
        gMain.addWidget(passBtn, 5, 1)
        """

        lTwoFALabel = QtWidgets.QLabel("2FA")
        lTwoFALabel.setObjectName("passLabel")
        gMain.addWidget(lTwoFALabel, 6, 0)
        lTwoFA = QtWidgets.QLabel("2FA: ")
        lTwoFA.setObjectName("passLabel")
        lTwoFA.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        if twoFa == "False":
            lTwoFA.setText("2FA: Inactive")
        elif twoFa == "True":
            lTwoFA.setText("2FA: Active")
        else:
            lTwoFA.setText("2FA: Error:{0}".format(twoFa))
        gMain.addWidget(lTwoFA, 6, 1)

        lGeneratedLabel = QtWidgets.QLabel("Generated:")
        lGeneratedLabel.setObjectName("passLabel")
        gMain.addWidget(lGeneratedLabel, 7, 0)
        lGenerated = QtWidgets.QLabel()
        lGenerated.setObjectName("passLabel")
        lGenerated.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        if generated == "True":
            lGenerated.setText("True")
        elif generated == "False":
            lGenerated.setText("False")
        else:
            lGenerated.setText("Error")
        gMain.addWidget(lGenerated, 7, 1)

        lDateLabel = QtWidgets.QLabel("Last Changed:")
        lDateLabel.setObjectName("passLabel")
        gMain.addWidget(lDateLabel, 8, 0)       
        lDate = QtWidgets.QLabel(str(lastChanged).split(".")[0])
        lDate.setObjectName("passLabel")
        lDate.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        gMain.addWidget(lDate, 8, 1)

        lCommentLabel = QtWidgets.QLabel("Comment:")
        lCommentLabel.setObjectName("passLabel")
        gMain.addWidget(lCommentLabel, 9, 0)
        lComment = QtWidgets.QLabel(comment)
        lComment.setObjectName("passLabel")
        lComment.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        gMain.addWidget(lComment, 9, 1)

        wMain.setLayout(lMain)
        vBack.addWidget(wMain)

        self.setLayout(vBack)
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum))
    
    #Works! Kinda! The password gets removed but only in a temporary local manner.
    #The db still contains the item. Probably a permission issue!
    def delPassword(self):
        text, ok = QtWidgets.QInputDialog.getText(self, 'Delete?', 'Confirm deletion by typing delete:')
        if ok:
            if text=="delete" or text=="Delete" or text=="DELETE":
                logging.info("Deleting the selected password")
                dab.DatabaseActions.delete(self, "passwords", self.index)
                passwords.Passwords.createPassSlates(self)
            else:
                CreateUI.delPassword(self)

#Idea, that the password is reveald only for a certain ammount of time when a button is pressed
class passButton(QtWidgets.QWidget):
    def setup(self, index = 0):
        passIndex = index
        #Main layouts and layout widgets
        global lBtnMain
        lBtnMain = QtWidgets.QStackedLayout()
        lBtnMain.setContentsMargins(0,0,0,0)

        btnReveal = QtWidgets.QPushButton("Reveal Password")
        btnReveal.clicked.connect(lambda:passButton.reveal(self, passIndex))
        lBtnMain.addWidget(btnReveal)
        
        self.setLayout(lBtnMain)
    
    def reveal(self, theIndex):
        data = dab.DatabaseActions.read(self, table="passTable", rows=theIndex)        
        global lPassword
        lPassword = QtWidgets.QLabel(crypt.Encryption.decrypt(self, data[9])[0])
        lBtnMain.addWidget(lPassword)

        lBtnMain.setCurrentIndex(1)

        timer = QtCore.QTimer(self)
        timer.setSingleShot(True)
        timer.setInterval(15000)
        timer.timeout.connect(lambda:passButton.clear(self))
        timer.start()
    
    def clear(self):
        lPassword.setText("")
        lBtnMain.setCurrentIndex(0)