import sys
from qt_core import *

class ContabilApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Sistema Contabil")
        self.resize(1200, 720)
        self.setMinimumSize(800, 600)

        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        self.principal_layout = QVBoxLayout(self.widget_central)

        self.title_label = QLabel("Bem-vindo ao Sistema Contábil")

        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        self.principal_layout.addWidget(self.title_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContabilApp()
    window.show()

    sys.exit(app.exec())