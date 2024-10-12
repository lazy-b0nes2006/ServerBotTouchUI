import mainGUI
from PyQt5 import QtWidgets
from MainUIClass.utils import Development
import os

class homePage(mainGUI.Ui_MainWindow):
    def init(self):
        # self.setupUi(self)
        print("Home Page init.")
        self.signal_slot_connections()
        super().__init__()

    def signal_slot_connections(self):
        print("Connecting signals and slots in home page.")
        self.startPushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.goPage))
        self.restartPushButton.pressed.connect(self.restart)
        self.stopPushButton.pressed.connect(self.stop)

    def restart(self):
        if Development:
            print("Restarting")
        else:
            os.system('sudo reboot now')
            
    def stop(self):
        if Development:
            print("Stopping")
        else:
            os.system('sudo shutdown now')
