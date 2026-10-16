import sys
from src.qt_core.qtlibrary import *

class contabilApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contabil System")
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = contabilApp()
    window.show()

    sys.exit(app.exec())