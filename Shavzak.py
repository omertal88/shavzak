import sys

from PyQt5.QtWidgets import QApplication
from src.ShavzakUi import ShavzakWindow

app = QApplication(sys.argv)
ui = ShavzakWindow()
ui.show()
sys.exit(app.exec_())
