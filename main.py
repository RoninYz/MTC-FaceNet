import sys
from PyQt5 import QtWidgets, QtCore, QtGui

import config_gui
import config_gui_event
class MainWindowController(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.config_gui = config_gui.Ui_MainWindow()
        self.config_gui.setupUi(self)
        self.config_event = config_gui_event.EventHandler(self.config_gui)
        self.config_event.init_events()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindowController()
    main_window.show()
    sys.exit(app.exec_())
