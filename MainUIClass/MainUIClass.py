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

        # Initialize the layout for items in the scroll area
        self.scroll_layout = QVBoxLayout()
        self.items_widget = QWidget()
        self.items_widget.setLayout(self.scroll_layout)
        self.itemsSelectedScrollArea.setWidget(self.items_widget)

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
        self.keyboardText = text
        if text.isdigit() and self.function == 'enterDestination':
            self.tableNumberLabel.setText(text)
            self.stackedWidget.setCurrentWidget(self.goPage)
            self.keyboard.first_press = True
        elif self.function == 'addItem':
            self.add_item_to_scroll_area(text)
            self.stackedWidget.setCurrentWidget(self.goPage)
            self.keyboard.first_press = True
        self.keyboard.line_edit.setText("")

    def add_item_to_scroll_area(self, item_name):
        # Check if the item is already in the scroll area
        for i in range(self.scroll_layout.count()):
            item_layout = self.scroll_layout.itemAt(i).layout()
            if item_layout and item_layout.itemAt(0).widget().text() == item_name:
                # Update the quantity
                quantity_label = item_layout.itemAt(1).widget()
                current_quantity = int(quantity_label.text())
                quantity_label.setText(str(current_quantity + 1))
                return

        # If the item is not present, add a new row with item name and quantity
        item_layout = QHBoxLayout()
        item_label = QLabel(item_name)
        quantity_label = QLabel("1")
        item_layout.addWidget(item_label)
        item_layout.addWidget(quantity_label)
        self.scroll_layout.addLayout(item_layout)
