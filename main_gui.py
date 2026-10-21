import sys
import os
from core import *

class ContabilApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.loaded_data = None

        self.setWindowTitle("Meu Sistema Contabil")
        self.resize(1200, 720)
        self.setMinimumSize(800, 600)

        self.widget_central = QWidget()
        self.setCentralWidget(self.widget_central)

        self.principal_layout = QVBoxLayout(self.widget_central)

        self.title_label = QLabel("Bem-vindo ao Sistema Contábil")
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.principal_layout.addWidget(self.title_label)

        # --- GERENCIADOR DE ARQUIVOS ---
        self.archive_group = QGroupBox("Gerenciador de Arquivos")
        self.archive_layout = QHBoxLayout()

        self.lbl_path = QLineEdit()
        self.lbl_path.setPlaceholderText("Selecione o relatório (.kpw)...")
        self.lbl_path.setReadOnly(True)

        # Botão para criar relatório
        self.btn_new = QPushButton("Novo Relatório")
        self.btn_new.setStyleSheet("background-color: #f39c12; color: white; font-weight: bold;")
        self.btn_new.clicked.connect(self.create_new_report)

        self.btn_search = QPushButton("Procurar Arquivo")
        self.btn_search.clicked.connect(self.search_file)

        self.btn_load = QPushButton("Carregar Dados")
        self.btn_load.setStyleSheet("background-color: #2E86C1; color: white; font-weight: bold;")
        self.btn_load.clicked.connect(self.load_data)

        self.archive_layout.addWidget(self.btn_new)
        self.archive_layout.addWidget(self.lbl_path)
        self.archive_layout.addWidget(self.btn_search)
        self.archive_layout.addWidget(self.btn_load)

        self.archive_group.setLayout(self.archive_layout)
        self.principal_layout.addWidget(self.archive_group)

        # --- ANÁLISES E OPERAÇÕES ---
        self.operations_group = QGroupBox("Análises e Operações")
        self.operations_layout = QHBoxLayout()

        self.btn_liquidez = QPushButton("Liquidez e Cap. de Giro")
        self.btn_liquidez.clicked.connect(self.calc_liquidez)
        self.btn_endividamento = QPushButton("Endividamento")
        self.btn_endividamento.clicked.connect(self.calc_endividamento)
        self.btn_rentabilidade = QPushButton("Rentabilidade")
        self.btn_rentabilidade.clicked.connect(self.calc_rentabilidade)
        self.btn_graficos = QPushButton("Gerar Gráficos")
        self.btn_graficos.clicked.connect(self.show_graphics)

        self.operations_layout.addWidget(self.btn_liquidez)
        self.operations_layout.addWidget(self.btn_endividamento)
        self.operations_layout.addWidget(self.btn_rentabilidade)
        self.operations_layout.addWidget(self.btn_graficos)

        self.operations_group.setLayout(self.operations_layout)
        self.principal_layout.addWidget(self.operations_group)

        # --- TERMINAL DE RESULTADOS ---
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

    def create_new_report(self):
        nome, ok1 = QInputDialog.getText(self, "Novo Relatório", "Digite o nome do relatório (ex: title_2025): ")
        if not ok1 or not nome.strip(): return
        
        desc, ok2 = QInputDialog.getText(self, "Novo Relatório", "Digite uma breve descrição: ")
        if not ok2: desc = ""

        # Chama a função de criar o .rel
        sucesso = create_new_archive(nome.strip(), desc.strip())

        if sucesso:
            self.loaded_data = nome.strip()
            self.lbl_path.setText(f"{self.loaded_data}.rel")
            self.txt_log.append(f"Relatório '{self.loaded_data}.rel' criado com sucesso!")
            self.txt_log.append("Ele agora é o relatório ATIVO. Novos cálculos serão salvos nele.\n")
        else:
            self.txt_log.append(f"Erro: Já existe um relatório chamado '{nome}'.\n")

    def search_file(self):
        archive_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecione o relatório",
            "",
            "Relatórios do Sistema (*.rel);;Todos os arquivos (*)"
        )

        if archive_path:
            self.lbl_path.setText(archive_path)

    def load_data(self):
        archive_path = self.lbl_path.text()

        if not archive_path:
            self.txt_log.append("AVISO: Nenhum ficheiro selecionado!\nPor favor, procure um ficheiro primeiro.\n")
            return
        
        nome_arquivo = os.path.basename(archive_path).replace('.rel', '')
        conteudo = read_files(nome_arquivo)

        if conteudo is not None:
            self.txt_log.append(f"--- LENDO O RELATÓRIO: {nome_arquivo.upper()} ---")
            self.txt_log.append(conteudo)
            self.loaded_data = nome_arquivo 
            self.txt_log.append(f"Relatório '{nome_arquivo}' definido como ATIVO. Novos cálculos serão salvos nele.\n")
        else:
            self.txt_log.append(f"Erro ao ler o relatório '{nome_arquivo}'. Ele pode não existir.\n")

    def ask_save_gui(self, categoria, indicador, valor):
        # Se não houver arquivo ativado, a função encerra silenciosamente
        if not self.loaded_data:
            return

        resposta = QMessageBox.question(
            self, 
            "Salvar no Histórico", 
            f"Deseja anexar o resultado de '{indicador}' ({valor:.2f}) ao relatório ativo '{self.loaded_data}'?",
            QMessageBox.Yes | QMessageBox.No
        )

        if resposta == QMessageBox.Yes:
            nota, ok = QInputDialog.getText(self, "Nota Opcional", "Deseja adicionar alguma nota ou observação? (Deixe em branco se não quiser)")
            if not ok: nota = ""

            sucesso = add_indicator(self.loaded_data, categoria, indicador, valor, nota)

            if sucesso:
                self.txt_log.append(f"[Salvo] {indicador} anexado com sucesso ao relatório.\n")
            else:
                self.txt_log.append(f"Erro ao anexar o indicador.\n")

    # ================= FUNCIONALIDADES DE CÁLCULO =================

    def calc_liquidez(self):
        
        atvc, ok1 = QInputDialog.getDouble(self, "Entrada de Dados", "Informe o Ativo Circulante (R$):", 0, 0, 1000000000, 2)
        if not ok1: return
        pc, ok2 = QInputDialog.getDouble(self, "Entrada de Dados", "Informe o Passivo Circulante (R$):", 0, 0, 1000000000, 2)
        if not ok2: return
        rlp, ok3 = QInputDialog.getDouble(self, "Entrada de Dados", "Informe o Realizável a Longo Prazo (R$):", 0, 0, 1000000000, 2)
        if not ok3: return
        elp, ok4 = QInputDialog.getDouble(self, "Entrada de Dados", "Informe o Exigível a Longo Prazo (R$):", 0, 0, 1000000000, 2)
        if not ok4: return

        self.txt_log.append("--- RESULTADOS DA LIQUIDEZ E CAPITAL DE GIRO ---")
        
        resultado_corrente = liq_corrente(atvc, pc)
        resultado_geral = liq_geral(atvc, rlp, pc, elp)
        resultado_ccl = ccLiquido(atvc, pc)

        if resultado_corrente is not None:
            self.txt_log.append(f"Liquidez Corrente: {resultado_corrente:.2f}")
            self.ask_save_gui("Liquidez e Capital de Giro", "Liquidez Corrente", resultado_corrente)
        else:
            self.txt_log.append("Erro: O Passivo Circulante não pode ser zero.")

        if resultado_geral is not None:
            self.txt_log.append(f"Liquidez Geral: {resultado_geral:.2f}")
            self.ask_save_gui("Liquidez e Capital de Giro", "Liquidez Geral", resultado_geral)

        self.txt_log.append(f"Capital Circulante Líquido: R$ {resultado_ccl:.2f}")
        self.ask_save_gui("Liquidez e Capital de Giro", "Capital Circulante Líquido", resultado_ccl)
        
        # AVISO GERAL SE NÃO TIVER ARQUIVO ABERTO
        if not self.loaded_data:
            self.txt_log.append("Resultados apenas exibidos. Crie ou carregue um relatório para salvá-los.\n")
        else:
            self.txt_log.append("\n")
    
    def calc_endividamento(self):
        ct, ok1 = QInputDialog.getDouble(self, "Endividamento", "Capital de Terceiros (Passivo Total):", 0, 0, 1e9, 2)
        if not ok1: return
        cp, ok2 = QInputDialog.getDouble(self, "Endividamento", "Capital Próprio (Patrimônio Líquido):", 0, 0, 1e9, 2)
        if not ok2: return
        pc, ok3 = QInputDialog.getDouble(self, "Endividamento", "Passivo Circulante:", 0, 0, 1e9, 2)
        if not ok3: return
        pnc, ok4 = QInputDialog.getDouble(self, "Endividamento", "Passivo Não Circulante:", 0, 0, 1e9, 2)
        if not ok4: return

        self.txt_log.append("--- RESULTADOS DE ESTRUTURA E ENDIVIDAMENTO ---")
        
        r_ctcp = relacaoCTCP(ct, cp)
        if r_ctcp is not None:
            self.txt_log.append(f"Relação CT/CP: {r_ctcp:.2f}%")
            self.ask_save_gui("Estrutura e Endividamento", "Relação CT/CP", r_ctcp)
        else:
            self.txt_log.append("Erro: Capital Próprio não pode ser zero.")

        comp_end = comp_ENDIVIDAMENTO(pc, pnc)
        if comp_end is not None:
            self.txt_log.append(f"Composição do Endividamento: {comp_end:.2f}%")
            self.ask_save_gui("Estrutura e Endividamento", "Composição do Endividamento", comp_end)
        else:
            self.txt_log.append("Erro: Passivo Total não pode ser zero.")

        if not self.loaded_data:
            self.txt_log.append("Resultados apenas exibidos. Crie ou carregue um relatório para salvá-los.\n")
        else:
            self.txt_log.append("\n")

    def calc_rentabilidade(self):
        ll, ok1 = QInputDialog.getDouble(self, "Rentabilidade", "Lucro Líquido:", 0, -1e9, 1e9, 2)
        if not ok1: return
        pl, ok2 = QInputDialog.getDouble(self, "Rentabilidade", "Patrimônio Líquido:", 0, -1e9, 1e9, 2)
        if not ok2: return
        lop, ok3 = QInputDialog.getDouble(self, "Rentabilidade", "Lucro Operacional:", 0, -1e9, 1e9, 2)
        if not ok3: return
        dep, ok4 = QInputDialog.getDouble(self, "Rentabilidade", "Depreciação:", 0, 0, 1e9, 2)
        if not ok4: return
        amo, ok5 = QInputDialog.getDouble(self, "Rentabilidade", "Amortização:", 0, 0, 1e9, 2)
        if not ok5: return
        rl, ok6 = QInputDialog.getDouble(self, "Rentabilidade", "Receita Líquida:", 0, 0, 1e9, 2)
        if not ok6: return

        self.txt_log.append("--- RESULTADOS DE LUCRATIVIDADE E RENTABILIDADE ---")

        roe = rEquity(ll, pl)
        if roe is not None:
            self.txt_log.append(f"ROE: {roe:.2f}%")
            self.ask_save_gui("Lucratividade e Rentabilidade", "Return of Equity (ROE)", roe)

        ebitda_val = eBITDA(lop, dep, amo)
        self.txt_log.append(f"EBITDA: R$ {ebitda_val:.2f}")
        self.ask_save_gui("Lucratividade e Rentabilidade", "EBITDA", ebitda_val)

        m_ebitda = mEBITDA(ebitda_val, rl)
        if m_ebitda is not None:
            self.txt_log.append(f"Margem EBITDA: {m_ebitda:.2f}%")
            self.ask_save_gui("Lucratividade e Rentabilidade", "Margem EBITDA", m_ebitda)

        if not self.loaded_data:
            self.txt_log.append("Resultados apenas exibidos. Crie ou carregue um relatório para salvá-los.\n")
        else:
            self.txt_log.append("\n")

    def show_graphics(self):
        indicador, ok1 = QInputDialog.getText(self, "Gráficos", "Nome do Indicador (ex: ROE):")
        if not ok1 or not indicador: return

        anos_str, ok2 = QInputDialog.getText(self, "Gráficos", "Anos separados por vírgula (ex: 2021, 2022, 2023):")
        if not ok2 or not anos_str: return

        valores_str, ok3 = QInputDialog.getText(self, "Gráficos", "Valores separados por vírgula (ex: 10.5, 12.0, 15.3):")
        if not ok3 or not valores_str: return

        # Cria uma janela com uma lista suspensa para escolher o formato
        tipos = ["Absoluto (R$)", "Percentual (%)"]
        tipo_escolhido, ok4 = QInputDialog.getItem(self, "Tipo de Gráfico", "Escolha o formato do gráfico:", tipos, 0, False)
        if not ok4: return
        
        # Converte a escolha do usuário para a string que o graficos.py espera
        tipo_grafico = 'absoluto' if "Absoluto" in tipo_escolhido else 'percentual'

        try:
            anos = [ano.strip() for ano in anos_str.split(',')]
            valores = [float(v.strip().replace(',', '.')) for v in valores_str.split(',')]

            if len(anos) != len(valores):
                self.txt_log.append("Erro: A quantidade de anos e valores deve ser igual.\n")
                return

            gerar_grafico(indicador, anos, valores, tipo_grafico)
            
            nome_arquivo = f"grafico_{indicador.replace(' ', '_').lower()}.png"
            self.txt_log.append(f"Gráfico gerado com sucesso: {nome_arquivo}\n")
            
        except ValueError:
            self.txt_log.append("Erro: Certifique-se de digitar apenas números nos valores.\n")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ContabilApp()
    window.show()

    sys.exit(app.exec())