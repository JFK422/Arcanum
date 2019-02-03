from components import dab, create, crypt
from PyQt5 import QtCore, QtWidgets

class Settings(QtWidgets.QWidget):
    def __init__(self):
        super(Settings, self).__init__()   
        
        #Settings tab layouts
        gSettingsMain = QtWidgets.QGridLayout()
        gSettingsMain.setAlignment(QtCore.Qt.AlignTop)

        #Create the settings tab
        leEmail = QtWidgets.QLineEdit(create.CreateUI.emailAddress)
        leEmail.setPlaceholderText("Email Address")
        leEmail.setMaximumWidth(300)
        gSettingsMain.addWidget(leEmail, 0, 0)

        btnUpdateMail = QtWidgets.QPushButton("Add")
        btnUpdateMail.setMaximumWidth(100)
        btnUpdateMail.setMaximumHeight(leEmail.sizeHint().height())
        btnUpdateMail.clicked.connect(lambda:Settings.addMailAddress(self, leEmail.text()))
        gSettingsMain.addWidget(btnUpdateMail, 0, 1)

        global liAddresses
        liAddresses = QtWidgets.QListWidget()
        liAddresses.setMaximumWidth(400)
        gSettingsMain.addWidget(liAddresses, 1, 0)

        global chkSaltedEncrypt
        chkSaltedEncrypt = QtWidgets.QCheckBox("Encrypt with salt")
        chkSaltedEncrypt.setChecked(False)
        gSettingsMain.addWidget(chkSaltedEncrypt, 0, 2)

        self.setLayout(gSettingsMain)

    def createData(self):
        #Check if salt is used and tick the checkbox if needed
        salt = False
        if dab.DatabaseActions.read(self, "configs", rows=1)[6] == 1: salt=True

        if salt: chkSaltedEncrypt.setChecked(False)
        else: chkSaltedEncrypt.setChecked(True)
        
        #Add all the email adresses!
        liAddresses.clear()
        dataEmail = dab.DatabaseActions.read(self, table="configs", everything=True)
        for i in range(1, len(dataEmail)):
            liAddresses.addItem(crypt.Encryption.decrypt(self, dataEmail[i][2], salt)[0])
            if i == 0:
                create.CreateUI.updateProgressBar(self, 0)
            else:
                create.CreateUI.updateProgressBar(self, (len(dataEmail))/i*100)
        print("Settings tab set")

    def addMailAddress(self, address):
        #name, email, dTest, keyLen, lstChanged
        #Add option later to encryt everything even if it is empty
        insertionData = {"name":"",
            "email":crypt.Encryption.encrypt(self, address),
            "dTest":"",
            "keyLen":"", 
            "lstChanged":""}
        dab.DatabaseActions.insert(self, "configs", insertionData)