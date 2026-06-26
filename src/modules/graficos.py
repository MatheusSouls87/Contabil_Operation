import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'ggplot')

def coletar_dados_usuario(tipo_grafico):
    print(f"\n--- Coleta de Dados ({tipo_grafico.upper()}) ---")
    nome_indicador = input("Qual operação/indicador deseja graficar? (ex: ROE, Lucro Líquido): ").strip()
    
    anos = []
    valores = []

    print(f"\nDigite os dados para '{nome_indicador}'.")
    print("Quando terminar, digite '0' no ano para gerar o gráfico.")

    while True:
        try:
            ano_input = input("\nAno (ou 0 para encerrar): ").strip()
            if ano_input == '0':
                break
            
            ano = int(ano_input)
            
            simbolo = 'R$' if tipo_grafico == 'absoluto' else '%'
            valor_input = input(f"Valor em {simbolo} para {ano}: ").strip()
            
            valor_limpo = valor_input.replace('R$', '').replace('%', '').strip()
            if ',' in valor_limpo and '.' in valor_limpo:
                valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
            elif ',' in valor_limpo:
                valor_limpo = valor_limpo.replace(',', '.')
                
            valor = float(valor_limpo)
            
            anos.append(str(ano))
            valores.append(valor)
            
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números válidos.")

    return nome_indicador, anos, valores


def gerar_grafico(nome_indicador, anos, valores, tipo_grafico):
    if len(anos) == 0:
        print("\n[AVISO] Nenhum dado foi inserido. Gráfico cancelado.")
        return False

    fig, ax = plt.subplots(figsize=(8, 5))

    if tipo_grafico == 'absoluto':
        # Gráfico de Barras para valores em Dinheiro
        ax.bar(anos, valores, color='#2b5c8f', width=0.5)
        ax.set_ylabel('Valores em R$', fontweight='bold')
        # Formata eixo Y para moeda
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, p: f"R$ {v:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")))
    
    elif tipo_grafico == 'percentual':
        # Gráfico de Linha para Porcentagens
        ax.plot(anos, valores, marker='o', markersize=8, color='#d9534f', linewidth=2.5)
        ax.set_ylabel('Percentual (%)', fontweight='bold')
        # Formata eixo Y para porcentagem
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(100.0 if max(valores) > 1.0 else 1.0))
        # Adiciona os rótulos de dados em cima de cada ponto na linha
        for i, txt in enumerate(valores):
            ax.annotate(f"{txt}%", (anos[i], valores[i]), textcoords="offset points", xytext=(0,10), ha='center')

    ax.set_title(f'Evolução - {nome_indicador.upper()}', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Período (Anos)', fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)

    nome_arquivo = f"grafico_{nome_indicador.replace(' ', '_').lower()}.png"
    
    plt.tight_layout()
    plt.savefig(nome_arquivo, dpi=300)
    plt.close()
    
    print(f"\n[SUCESSO] Gráfico gerado e salvo como '{nome_arquivo}'!")
    return True

def coletar_dados_multiplos(tipo_grafico, qtd_indicadores=3):
    print(f"\n--- Coleta de Dados Múltiplos Comparativos ({tipo_grafico.upper()}) ---")
    
    anos_input = input("Quais anos deseja analisar? (Separe por vírgula, ex: 2023, 2024, 2025): ").strip()
    anos = [ano.strip() for ano in anos_input.split(',')]
    
    dados_completos = {}

    for i in range(qtd_indicadores):
        nome_indicador = input(f"\nQual o nome do {i+1}º indicador/operação? ").strip()
        valores = []

        print(f"-> Inserindo dados para: {nome_indicador.upper()}")
        for ano in anos:
            simbolo = 'R$' if tipo_grafico == 'absoluto' else '%'
            while True:
                try:
                    valor_input = input(f"Valor em {simbolo} para {ano}: ").strip()
                    
                    valor_limpo = valor_input.replace('R$', '').replace('%', '').strip()
                    if ',' in valor_limpo and '.' in valor_limpo:
                        valor_limpo = valor_limpo.replace('.', '').replace(',', '.')
                    elif ',' in valor_limpo:
                        valor_limpo = valor_limpo.replace(',', '.')
                        
                    valor = float(valor_limpo)
                    valores.append(valor)
                    break # Sai do loop se a conversão deu certo
                except ValueError:
                    print("Entrada inválida! Por favor, digite apenas números válidos.")
                    
        # Salva a lista de valores atrelada ao nome do indicador
        dados_completos[nome_indicador] = valores

    return anos, dados_completos


def gerar_grafico_multiplo(anos, dados_completos, tipo_grafico):
    if not anos or not dados_completos:
        print("\n[AVISO] Dados insuficientes. Gráfico cancelado.")
        return False

    fig, ax = plt.subplots(figsize=(10, 6))

    cores = ['#2b5c8f', '#d9534f', '#5cb85c', '#f0ad4e'] 
    marcadores = ['o', 's', '^', 'D']

    # Desenha uma linha para cada indicador coletado
    for i, (indicador, valores) in enumerate(dados_completos.items()):
        cor = cores[i % len(cores)]
        marcador = marcadores[i % len(marcadores)]
        
        ax.plot(anos, valores, marker=marcador, markersize=8, linewidth=2.5, label=indicador, color=cor)
        
        # Se for percentual, adicionamos os textinhos em cima dos pontos
        if tipo_grafico == 'percentual':
            for j, txt in enumerate(valores):
                ax.annotate(f"{txt}%", (anos[j], valores[j]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

    # Formatação do Eixo Y
    if tipo_grafico == 'absoluto':
        ax.set_ylabel('Valores em R$', fontweight='bold')
        ax.yaxis.set_major_formatter(mtick.FuncFormatter(lambda v, p: f"R$ {v:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")))
    else:
        ax.set_ylabel('Percentual (%)', fontweight='bold')
        # Pega o maior valor de todas as listas para definir a escala correta
        maior_valor_geral = max([max(v) for v in dados_completos.values()])
        ax.yaxis.set_major_formatter(mtick.PercentFormatter(100.0 if maior_valor_geral > 1.0 else 1.0))

    ax.set_title('Análise Comparativa de Indicadores', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Período (Anos)', fontweight='bold')
    ax.grid(True, linestyle='--', alpha=0.6)

    ax.legend(title="Indicadores", loc='upper left', bbox_to_anchor=(1, 1), frameon=True, shadow=True)

    nome_arquivo = "grafico_comparativo_multiplo.png"
    
    fig.tight_layout()
    fig.savefig(nome_arquivo, dpi=300)
    plt.close(fig)
    
    print(f"\n[SUCESSO] Gráfico múltiplo gerado e salvo como '{nome_arquivo}'!")
    return True