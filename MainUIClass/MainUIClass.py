from PyQt5 import QtWidgets
import mainGUI
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel
from MainUIClass.keyboard import Keyboard

class MainUIClass(QtWidgets.QMainWindow, mainGUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainUIClass, self).__init__(parent)
        self.setupUi(self)
        self.apply_stylesheet()
        self.signal_slot_connections()
        self.stackedWidget.setCurrentWidget(self.homePage)

        # Initialize keyboard and input field
        self.keyboard = Keyboard(self)
        self.keyboardText = ''

        # Add the keyboard and input label to the keyboardPage
        self.keyboardVlayout.addWidget(self.keyboard)
        self.keyboard.setVisible(False)

    def apply_stylesheet(self):
        with open("styles.qss", "r") as file:
            stylesheet = file.read()
            self.setStyleSheet(stylesheet)

    def signal_slot_connections(self):
        # Home Page
        self.startPushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.goPage))
        self.addItemPushButton.pressed.connect(lambda: self.show_keyboard('addItem'))
        self.enterDestinationPushButton.pressed.connect(lambda: self.show_keyboard('enterDestination'))

        # Go Page
        self.homePushButton.pressed.connect(lambda: self.stackedWidget.setCurrentWidget(self.homePage))

    def show_keyboard(self, function):
        self.keyboard.setVisible(True)
        self.function = function
        self.stackedWidget.setCurrentWidget(self.keyboardPage)
        self.keyboard.setFocus()

        if function == 'addItem':
            self.keyboard.dropdown.setVisible(True)
        else:
            self.keyboard.dropdown.setVisible(False)

    def update_display(self, text):
        if (text.isdigit() and self.function == 'enterDestination') or self.function == 'addItem':
            self.keyboardText = text
            if self.function == 'addItem':
                pass
            elif self.function == 'enterDestination':
                self.tableNumberLabel.setText(text)
            self.keyboard.line_edit.setText("")
            self.stackedWidget.setCurrentWidget(self.goPage)
            self.keyboard.first_press = True
        else:
            self.keyboard.line_edit.setText("")