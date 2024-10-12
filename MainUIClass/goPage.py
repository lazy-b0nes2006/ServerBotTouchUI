import mainGUI
from PyQt5 import QtWidgets
from MainUIClass.utils import Development

class goPage(mainGUI.Ui_MainWindow):
    def init(self):
        # self.setupUi(self)
        self.signal_slot_connections()
        super().__init__()

    def signal_slot_connections(self):
        self.homePushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
        self.addItemPushButton.pressed.connect(lambda: self.show_keyboard('addItem'))
        self.enterDestinationPushButton.pressed.connect(lambda: self.show_keyboard('enterDestination'))
        self.removeItemPushButton.pressed.connect(self.remove_item_from_scroll_area)
