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