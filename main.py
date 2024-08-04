import sys
from PyQt5 import QtWidgets
from MainUIClass import MainUIClass

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = MainUIClass()
    MainWindow.show()

    sys.exit(app.exec_())
