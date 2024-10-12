from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel

from MainUIClass.homePage import homePage
from MainUIClass.goPage import goPage
from MainUIClass.keyboard import Keyboard

from MainUIClass.utils import menu

class MainUIClass(QMainWindow, homePage, goPage):
    def __init__(self):
        print("Inside main ui class.")
        print("after super command.")
        
        super(MainUIClass, self).__init__()
        self.init_keyboard()
        self.stackedWidget.setCurrentWidget(self.homePage)
        self.apply_stylesheet()
        self.setupUi(self)



    def init_keyboard(self):
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
            if text in menu:
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

    def remove_item_from_scroll_area(self):
        text = self.keyboard.line_edit.text()
        for i in range(self.scroll_layout.count()):
            item_layout = self.scroll_layout.itemAt(i).layout()
            if item_layout and item_layout.itemAt(0).widget().text() == text:
                # Remove the item
                for j in reversed(range(item_layout.count())):
                    widget = item_layout.itemAt(j).widget()
                    if widget is not None:
                        widget.setParent(None)
                self.scroll_layout.removeItem(item_layout)
                break
        self.keyboard.line_edit.setText("")

