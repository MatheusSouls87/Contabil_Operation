import sys
from qt_core import *

class ContabilApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Sistema Contabil")
        self.resize(1200, 720)
        self.setMinimumSize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContabilApp()
    window.show()

    sys.exit(app.exec())