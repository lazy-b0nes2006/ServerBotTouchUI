import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget Names Example")
        self.setGeometry(100, 100, 400, 300)
        
        # QLabel to display the input text
        self.displayLabel = QLabel("Input text will be displayed here", self)
        self.displayLabel.setObjectName("displayLabel")

        # QPushButton to open the on-screen keyboard
        self.button = QPushButton("Open Keyboard", self)
        self.button.setObjectName("openKeyboardButton")
        self.button.clicked.connect(self.print_widget_names)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.displayLabel)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def print_widget_names(self):
        widget_names = self.get_all_widget_names(self)
        print("Widgets on the screen:")
        for name in widget_names:
            print(name)

    def get_all_widget_names(self, widget):
        widget_names = []
        if widget.objectName():
            widget_names.append(widget.objectName())
        for child in widget.children():
            widget_names.extend(self.get_all_widget_names(child))
        return widget_names

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()

    sys.exit(app.exec_())
