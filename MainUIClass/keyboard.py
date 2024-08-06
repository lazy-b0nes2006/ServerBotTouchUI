from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QSizePolicy, QLineEdit, QComboBox
from MainUIClass.utils import menu

class Keyboard(QWidget):

    first_press = True

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        # Create QLineEdit for typing
        self.line_edit = QLineEdit(self)
        self.line_edit.textChanged.connect(self.filter_dropdown)

        # Create QComboBox for dropdown suggestions
        self.dropdown = QComboBox(self)
        self.dropdown.setVisible(False)
        self.dropdown.activated.connect(self.update_line_edit_from_dropdown)

        # Create buttons for the keyboard
        self.create_buttons()

    def create_buttons(self):
        Vlayout = QVBoxLayout()
        container = QWidget()
        container.setLayout(Vlayout)

        # Add the QLineEdit and QComboBox to the layout
        Vlayout.addWidget(self.line_edit)
        Vlayout.addWidget(self.dropdown)

        rows = [
            ['Clear All', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Backspace'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '(', ')'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', ';', '-'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', "'", '"', '_'],
            ['Cancel', 'Space', 'Enter']
        ]

        for row in rows:
            row_layout = QHBoxLayout()
            for key in row:
                button = QPushButton(key, self)
                button.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
                if key == 'Backspace' or key == 'Clear All':
                    button.setFixedSize(110, 90)
                elif key == 'Cancel' or key == 'Space' or key == 'Enter':
                    button.setFixedSize(320, 90)
                else:
                    button.setFixedSize(70, 90)  # Set a fixed size for the buttons
                button.clicked.connect(lambda checked, key=key: self.key_pressed(key))
                row_layout.addWidget(button)
            Vlayout.addLayout(row_layout)

        self.setLayout(Vlayout)

    def key_pressed(self, key):
        if self.first_press:
            self.line_edit.setText("")
            self.first_press = False

        current_text = self.line_edit.text()
        if key == 'Backspace':
            self.line_edit.setText(current_text[:-1])
        elif key == 'Space':
            self.line_edit.setText(current_text + ' ')
        elif key == 'Enter':
            self.main_window.update_display(self.line_edit.text())
        elif key == 'Cancel':
            self.line_edit.setText("")
            self.main_window.stackedWidget.setCurrentWidget(self.main_window.goPage)
        elif key == 'Clear All':
            self.line_edit.setText("")
        else:
            self.line_edit.setText(current_text + key)

    def filter_dropdown(self):
        # Simulated menu list for demonstration
        current_text = self.line_edit.text()
        if current_text:
            self.dropdown.clear()
            filtered_items = [item for item in menu if current_text.lower() in item.lower()]
            self.dropdown.addItems(filtered_items)
            # self.dropdown.setVisible(True)
        else:
            self.dropdown.setVisible(False)

    def update_line_edit_from_dropdown(self):
        selected_item = self.dropdown.currentText()
        if selected_item:
            self.line_edit.setText(selected_item)
            self.dropdown.setVisible(False)

    def load_stylesheet(self, filepath):
        with open(filepath, "r") as file:
            self.setStyleSheet(file.read())
