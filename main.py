from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

# All you need is http:/doc.gt.io/gtforpython-6/
if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    application.exec()
