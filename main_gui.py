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
        self.btn_search.clicked.connect(self.search_file)

        self.btn_load = QPushButton("Carregar Dados")

        self.btn_load.setStyleSheet("background-color: #2E86C1; color: white; font-weight: bold;")

        self.archive_layout.addWidget(self.lbl_path)
        self.archive_layout.addWidget(self.btn_search)
        self.archive_layout.addWidget(self.btn_load)

        self.archive_group.setLayout(self.archive_layout)

        self.principal_layout.addWidget(self.archive_group)

        self.operations_group = QGroupBox("Análises e Operações")
        self.operations_layout = QHBoxLayout()

        self.btn_liquidez = QPushButton("Liquidez e Cap. de Giro")
        self.btn_endividamento = QPushButton("Endividamento")
        self.btn_rentabilidade = QPushButton("Rentabilidade")
        self.btn_graficos = QPushButton("Gerar Gráficos")

        self.operations_layout.addWidget(self.btn_liquidez)
        self.operations_layout.addWidget(self.btn_endividamento)
        self.operations_layout.addWidget(self.btn_rentabilidade)
        self.operations_layout.addWidget(self.btn_graficos)

        self.operations_group.setLayout(self.operations_layout)
        self.principal_layout.addWidget(self.operations_group)

        self.log_group = QGroupBox("Terminal de Resultados")
        self.log_layout = QVBoxLayout()

        self.txt_log = QTextEdit()
        self.txt_log.setReadOnly(True)

        self.txt_log.setStyleSheet("background-color: #1e1e1e; color: #00ff00; font-family: Consolas; font-size: 14px;")
        
        self.btn_clear = QPushButton("Limpar Terminal")
        self.btn_clear.clicked.connect(self.txt_log.clear)

        self.log_layout.addWidget(self.txt_log)
        self.log_layout.addWidget(self.btn_clear)

        self.log_group.setLayout(self.log_layout)
        self.principal_layout.addWidget(self.log_group)

        self.principal_layout.addStretch()

    def search_file(self):
        archive_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o arquivo",
            "",
            "Arquivos Excel (*.xlsx *.xls);;Todos os arquivos (*)"
            )

        if archive_path:
            self.lbl_path.setText(archive_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContabilApp()
    window.show()

    sys.exit(app.exec())