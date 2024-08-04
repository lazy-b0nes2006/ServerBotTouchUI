from PyQt5 import QtWidgets
import mainGUI

class MainUIClass(QtWidgets.QMainWindow, mainGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.apply_stylesheet()
        self.signal_slot_connections()
        self.stackedWidget.setCurrentWidget(self.homePage)

    def apply_stylesheet(self):
        with open("styles.qss", "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def signal_slot_connections(self):
        # Home Page
        self.startPushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.goPage))

        # Go Page
        self.homePushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))
