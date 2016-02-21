from PySide import QtCore, QtGui


class AddContact(QtGui.QWidget):
    """Add contact form"""

    def __init__(self):
        super(AddContact, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName('AddContact')
        self.resize(568, 306)
        self.sendRequestButton = QtGui.QPushButton(self)
        self.sendRequestButton.setGeometry(QtCore.QRect(50, 270, 471, 31))
        self.sendRequestButton.setMinimumSize(QtCore.QSize(0, 0))
        self.sendRequestButton.setBaseSize(QtCore.QSize(0, 0))
        self.sendRequestButton.setObjectName("sendRequestButton")
        self.lineEdit = QtGui.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(50, 40, 471, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(70, 10, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtGui.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(50, 110, 471, 151))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate('AddContact', "Add contact", None, QtGui.QApplication.UnicodeUTF8))
        self.sendRequestButton.setText(QtGui.QApplication.translate("Form", "Send request", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate('AddContact', "TOX ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate('AddContact', "Message:", None, QtGui.QApplication.UnicodeUTF8))


class ProfileSettings(QtGui.QWidget):
    """Form with profile settings such as name, status, TOX ID"""
    def __init__(self):
        super(ProfileSettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("ProfileSettingsForm")
        self.resize(600, 400)
        self.setMinimumSize(QtCore.QSize(600, 400))
        self.setMaximumSize(QtCore.QSize(600, 400))
        self.setBaseSize(QtCore.QSize(600, 400))
        self.nick = QtGui.QLineEdit(self)
        self.nick.setGeometry(QtCore.QRect(30, 60, 351, 27))
        self.nick.setObjectName("nick")
        self.status = QtGui.QLineEdit(self)
        self.status.setGeometry(QtCore.QRect(30, 130, 351, 27))
        self.status.setObjectName("status")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(50, 30, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tox_id = QtGui.QLabel(self)
        self.tox_id.setGeometry(QtCore.QRect(10, 210, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.tox_id.setFont(font)
        self.tox_id.setObjectName("tox_id")
        self.copyId = QtGui.QPushButton(self)
        self.copyId.setGeometry(QtCore.QRect(40, 250, 98, 31))
        self.copyId.setObjectName("copyId")
        self.comboBox = QtGui.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(30, 350, 211, 27))
        self.comboBox.setObjectName("comboBox")
        self.tox_id_2 = QtGui.QLabel(self)
        self.tox_id_2.setGeometry(QtCore.QRect(40, 310, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setWeight(75)
        font.setBold(True)
        self.tox_id_2.setFont(font)
        self.tox_id_2.setObjectName("tox_id_2")
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("ProfileSettingsForm", "Profile settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProfileSettingsForm", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProfileSettingsForm", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProfileSettingsForm", "TOX ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.tox_id.setText(QtGui.QApplication.translate("ProfileSettingsForm", "TOX ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.copyId.setText(QtGui.QApplication.translate("ProfileSettingsForm", "Copy TOX ID", None, QtGui.QApplication.UnicodeUTF8))
        self.tox_id_2.setText(QtGui.QApplication.translate("ProfileSettingsForm", "Language:", None, QtGui.QApplication.UnicodeUTF8))


class NetworkSettings(QtGui.QWidget):
    """Network settings form: UDP, Ipv6 and proxy"""

    def __init__(self):
        super(NetworkSettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("NetworkSettings")
        self.resize(300, 300)
        self.setMinimumSize(QtCore.QSize(300, 300))
        self.setMaximumSize(QtCore.QSize(300, 300))
        self.setBaseSize(QtCore.QSize(300, 300))
        self.ipv = QtGui.QCheckBox(self)
        self.ipv.setGeometry(QtCore.QRect(20, 10, 97, 22))
        self.ipv.setObjectName("ipv")
        self.udp = QtGui.QCheckBox(self)
        self.udp.setGeometry(QtCore.QRect(20, 50, 97, 22))
        self.udp.setObjectName("udp")
        self.proxy = QtGui.QCheckBox(self)
        self.proxy.setGeometry(QtCore.QRect(20, 90, 97, 22))
        self.proxy.setObjectName("proxy")
        self.proxyip = QtGui.QLineEdit(self)
        self.proxyip.setGeometry(QtCore.QRect(40, 160, 231, 27))
        self.proxyip.setObjectName("proxyip")
        self.proxyport = QtGui.QLineEdit(self)
        self.proxyport.setGeometry(QtCore.QRect(40, 220, 231, 27))
        self.proxyport.setObjectName("proxyport")
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(40, 130, 66, 17))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 66, 17))
        self.label_2.setObjectName("label_2")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("NetworkSettings", "Network settings", None, QtGui.QApplication.UnicodeUTF8))
        self.ipv.setText(QtGui.QApplication.translate("Form", "IPv6", None, QtGui.QApplication.UnicodeUTF8))
        self.udp.setText(QtGui.QApplication.translate("Form", "UDP", None, QtGui.QApplication.UnicodeUTF8))
        self.proxy.setText(QtGui.QApplication.translate("Form", "Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Port:", None, QtGui.QApplication.UnicodeUTF8))


class PrivacySettings(QtGui.QWidget):
    """Privacy settings form: history, typing notifications"""

    def __init__(self):
        super(PrivacySettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("privacySettings")
        self.resize(350, 200)
        self.setMinimumSize(QtCore.QSize(350, 200))
        self.setMaximumSize(QtCore.QSize(350, 200))
        self.setBaseSize(QtCore.QSize(350, 200))
        self.saveHistory = QtGui.QCheckBox(self)
        self.saveHistory.setGeometry(QtCore.QRect(40, 20, 291, 22))
        self.saveHistory.setObjectName("saveHistory")
        self.fileautoaccept = QtGui.QCheckBox(self)
        self.fileautoaccept.setGeometry(QtCore.QRect(40, 60, 271, 22))
        self.fileautoaccept.setObjectName("fileautoaccept")
        self.typingNotifications = QtGui.QCheckBox(self)
        self.typingNotifications.setGeometry(QtCore.QRect(40, 90, 350, 31))
        self.typingNotifications.setBaseSize(QtCore.QSize(350, 200))
        self.typingNotifications.setObjectName("typingNotifications")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("privacySettings", "Privacy settings", None, QtGui.QApplication.UnicodeUTF8))
        self.saveHistory.setText(QtGui.QApplication.translate("privacySettings", "Save chat history", None, QtGui.QApplication.UnicodeUTF8))
        self.fileautoaccept.setText(QtGui.QApplication.translate("privacySettings", "Allow file autoaccept", None, QtGui.QApplication.UnicodeUTF8))
        self.typingNotifications.setText(QtGui.QApplication.translate("privacySettings", "Send typing notifications", None, QtGui.QApplication.UnicodeUTF8))


class NotificationsSettings(QtGui.QWidget):
    """Notifications settings form"""

    def __init__(self):
        super(NotificationsSettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("notificationsForm")
        self.resize(300, 200)
        self.setMinimumSize(QtCore.QSize(300, 200))
        self.setMaximumSize(QtCore.QSize(300, 200))
        self.setBaseSize(QtCore.QSize(300, 200))
        self.enableNotifications = QtGui.QCheckBox(self)
        self.enableNotifications.setGeometry(QtCore.QRect(30, 20, 241, 22))
        self.enableNotifications.setObjectName("enableNotifications")
        self.checkBox_2 = QtGui.QCheckBox(self)
        self.checkBox_2.setGeometry(QtCore.QRect(30, 100, 231, 22))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtGui.QCheckBox(self)
        self.checkBox_3.setGeometry(QtCore.QRect(30, 60, 231, 22))
        self.checkBox_3.setObjectName("checkBox_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("notificationsForm", "Notification settings", None, QtGui.QApplication.UnicodeUTF8))
        self.enableNotifications.setText(QtGui.QApplication.translate("notificationsForm", "Enable notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_2.setText(QtGui.QApplication.translate("notificationsForm", "Enable call\'s sound", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_3.setText(QtGui.QApplication.translate("notificationsForm", "Enable sound notifications", None, QtGui.QApplication.UnicodeUTF8))


class InterfaceSettings(QtGui.QWidget):
    """Interface settings form"""

    def __init__(self):
        super(InterfaceSettings, self).__init__()
        self.initUI()

    def initUI(self):
        self.setObjectName("interfaceForm")
        self.resize(300, 300)
        self.setMinimumSize(QtCore.QSize(300, 300))
        self.setMaximumSize(QtCore.QSize(300, 300))
        self.setBaseSize(QtCore.QSize(300, 300))
        self.label = QtGui.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.themeSelect = QtGui.QComboBox(self)
        self.themeSelect.setGeometry(QtCore.QRect(30, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.themeSelect.setFont(font)
        self.themeSelect.setObjectName("themeSelect")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(QtGui.QApplication.translate("interfaceForm", "Interface settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("interfaceForm", "Theme:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = NetworkSettings()
    ex.show()
    app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
    app.exec_()