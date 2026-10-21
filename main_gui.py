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

        self.archive_group = QGroupBox("Gerenciador de Arquivos")
        
        self.archive_layout = QHBoxLayout()

        self.lbl_path = QLineEdit()
        self.lbl_path.setPlaceholderText("Selecione a planilha ou arquivo contabil...")
        self.lbl_path.setReadOnly(True)

        self.btn_search = QPushButton("Procurar Arquivo")
        self.btn_load = QPushButton("Carregar Dados")

        self.btn_load.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold;")

        self.archive_layout.addWidget(self.lbl_path)
        self.archive_layout.addWidget(self.btn_search)
        self.archive_layout.addWidget(self.btn_load)

        self.archive_group.setLayout(self.archive_layout)

        self.principal_layout.addWidget(self.archive_group)

        self.principal_layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContabilApp()
    window.show()

    sys.exit(app.exec())