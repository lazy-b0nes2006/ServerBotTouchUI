import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("On-Screen Keyboard Example")
        self.setGeometry(100, 100, 400, 300)
        
        # QLabel to display the input text
        self.displayLabel = QLabel("Input text will be displayed here", self)

        # QPushButton to open the on-screen keyboard
        self.button = QPushButton("Open Keyboard", self)
        self.button.clicked.connect(self.open_keyboard)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.displayLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Initialize keyboard as None
        self.keyboard = None

    def open_keyboard(self):
        # Check if keyboard already exists
        self.displayLabel.setText("")
        if not self.keyboard:
            self.keyboard = Keyboard(self.displayLabel)
            self.keyboard.load_stylesheet("styles.qss")
            self.keyboard.show()
            # Ensure keyboard is cleaned up when closed
            self.keyboard.destroyed.connect(self.on_keyboard_closed)

    def on_keyboard_closed(self):
        # Clean up reference to keyboard
        self.keyboard = None

    def update_display(self, text):
        self.displayLabel.setText(text)

class Keyboard(QMainWindow):
    def __init__(self, input_field):
        super().__init__()
        self.setWindowTitle("On-Screen Keyboard")
        self.setGeometry(100, 400, 600, 300)
        self.input_field = input_field

        # Create buttons for the keyboard
        self.create_buttons()

    def create_buttons(self):
        layout = QVBoxLayout()
        container = QWidget()
        container.setLayout(layout)

        rows = [
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Backspace'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '(', ')'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', ';', '-'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', "'", '"', '_'],
            ['Space', 'Enter']
        ]

        for row in rows:
            row_layout = QHBoxLayout()
            for key in row:
                button = QPushButton(key, self)
                button.clicked.connect(lambda checked, key=key: self.key_pressed(key))
                row_layout.addWidget(button)
            layout.addLayout(row_layout)

        self.setCentralWidget(container)

    def key_pressed(self, key):
        current_text = self.input_field.text()
        if key == 'Backspace':
            self.input_field.setText(current_text[:-1])
        elif key == 'Space':
            self.input_field.setText(current_text + ' ')
        elif key == 'Enter':
            pass
        else:
            self.input_field.setText(current_text + key)

    def load_stylesheet(self, filepath):
        with open(filepath, "r") as file:
            self.setStyleSheet(file.read())

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
