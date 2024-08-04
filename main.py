import sys
from PyQt5 import QtWidgets
from MainUIClass import MainUIClass

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Create MainUIClass instance
    main_window = MainUIClass()
    main_window.show()

    # Execute the application
    sys.exit(app.exec_())
