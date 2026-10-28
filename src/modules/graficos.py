import math
import re
import unicodedata

import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

plt.style.use(
    "seaborn-v0_8-whitegrid"
    if "seaborn-v0_8-whitegrid" in plt.style.available
    else "ggplot"
)

CORES = ["#2b5c8f", "#d9534f", "#5cb85c", "#f0ad4e", "#8064a2", "#46a6a6"]
MARCADORES = ["o", "s", "^", "D", "v", "P"]


def _numero_ptbr(texto):
    #Converte texto numérico, aceitando vírgula decimal.
    valor = str(texto).strip().replace("R$", "").replace("%", "").replace(" ", "")

    if not valor:
        raise ValueError("O valor não pode ficar vazio.")

    if "," in valor and "." in valor:
        if valor.rfind(",") > valor.rfind("."):
            valor = valor.replace(".", "").replace(",", ".")
        else:
            valor = valor.replace(",", "")
    elif "," in valor:
        valor = valor.replace(",", ".")

    numero = float(valor)

    if not math.isfinite(numero):
        raise ValueError("Use um número finito, sem NaN ou infinito.")

    return numero


def _validar_tipo(tipo_grafico):
    if tipo_grafico not in ("absoluto", "percentual"):
        raise ValueError("O tipo deve ser 'absoluto' ou 'percentual'.")


def _validar_dados(anos, valores, tipo_grafico):
    _validar_tipo(tipo_grafico)

    if not anos or not valores:
        raise ValueError("Informe pelo menos um ano e um valor.")

    if len(anos) != len(valores):
        raise ValueError("A quantidade de anos deve ser igual à quantidade de valores.")

    anos = [str(ano).strip() for ano in anos]

    if any(not ano for ano in anos):
        raise ValueError("Os anos não podem ficar vazios.")

    if len(set(anos)) != len(anos):
        raise ValueError("Existem anos repetidos.")

    valores_validos = []

    for valor in valores:
        numero = float(valor)

        if not math.isfinite(numero):
            raise ValueError("Os valores devem ser números finitos.")

        if tipo_grafico == "percentual" and not 0 <= numero <= 100:
            raise ValueError(
                "Informe percentuais de 0 a 100 "
                "(ex.: 12.5 para 12,5%)."
            )

        valores_validos.append(numero)

    return anos, valores_validos


def _formatar_moeda(valor, _posicao=None):
    return (
        f"R$ {valor:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def _nome_arquivo_seguro(nome):
    nome = unicodedata.normalize("NFKD", str(nome))
    nome = nome.encode("ascii", "ignore").decode("ascii")
    nome = re.sub(r"[^A-Za-z0-9_-]+", "_", nome.strip().lower())
    nome = nome.strip("_-")
    return nome or "indicador"


def nome_arquivo_grafico(nome_indicador):
    """Retorna o nome padronizado do arquivo de gráfico individual."""
    return f"grafico_{_nome_arquivo_seguro(nome_indicador)}.png"


def coletar_dados_usuario(tipo_grafico):
    _validar_tipo(tipo_grafico)

    print(f"\n--- Coleta de Dados ({tipo_grafico.upper()}) ---")

    nome_indicador = input(
        "Qual operação/indicador deseja graficar? "
        "(ex.: ROE, Lucro Líquido): "
    ).strip()

    while not nome_indicador:
        print("O nome do indicador não pode ficar vazio.")
        nome_indicador = input("Nome do indicador: ").strip()

    anos = []
    valores = []

    print(f"\nDigite os dados para '{nome_indicador}'.")
    print("Quando terminar, digite '0' no ano para gerar o gráfico.")

    if tipo_grafico == "percentual":
        print("Use percentuais de 0 a 100: digite 12.5 para 12,5%.")

    while True:
        ano_input = input("\nAno (ou 0 para encerrar): ").strip()

        if ano_input == "0":
            break

        try:
            ano = int(ano_input)

            if str(ano) in anos:
                print("Esse ano já foi informado.")
                continue

            simbolo = "R$" if tipo_grafico == "absoluto" else "%"
            valor_input = input(f"Valor em {simbolo} para {ano}: ")
            valor = _numero_ptbr(valor_input)

            if tipo_grafico == "percentual" and not 0 <= valor <= 100:
                print("Informe um percentual entre 0 e 100.")
                continue

            anos.append(str(ano))
            valores.append(valor)

        except ValueError as erro:
            print(f"Entrada inválida: {erro}")

    return nome_indicador, anos, valores


def gerar_grafico(nome_indicador, anos, valores, tipo_grafico):
    #Gera um gráfico individual e retorna True se o PNG for salvo.

    try:
        if not str(nome_indicador).strip():
            raise ValueError("O nome do indicador não pode ficar vazio.")

        anos, valores = _validar_dados(anos, valores, tipo_grafico)

    except (TypeError, ValueError) as erro:
        print(f"\n[AVISO] Gráfico não gerado: {erro}")
        return False

    fig, ax = plt.subplots(figsize=(8, 5))

    try:
        if tipo_grafico == "absoluto":
            barras = ax.bar(
                anos, valores, color=CORES[0], width=0.55
            )
            ax.set_ylabel("Valor (R$)", fontweight="bold")
            ax.yaxis.set_major_formatter(
                mtick.FuncFormatter(_formatar_moeda)
            )

            ax.bar_label(
                barras,
                labels=[_formatar_moeda(v) for v in valores],
                padding=3,
                fontsize=8,
            )

        else:
            ax.plot(
                anos, valores,
                marker="o",
                markersize=7,
                color=CORES[1],
                linewidth=2.5,
            )
            ax.set_ylabel("Percentual (%)", fontweight="bold")
            ax.yaxis.set_major_formatter(
                mtick.PercentFormatter(xmax=100, decimals=1)
            )

            for ano, valor in zip(anos, valores):
                ax.annotate(
                    f"{valor:g}%",
                    (ano, valor),
                    textcoords="offset points",
                    xytext=(0, 9),
                    ha="center",
                )

        ax.set_title(
            f"Evolução - {str(nome_indicador).strip().upper()}",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax.set_xlabel("Período (anos)", fontweight="bold")
        ax.grid(True, linestyle="--", alpha=0.6)

        fig.tight_layout()
        nome_arquivo = nome_arquivo_grafico(nome_indicador)
        fig.savefig(nome_arquivo, dpi=300, bbox_inches="tight")

        print(f"\n[SUCESSO] Gráfico salvo como '{nome_arquivo}'!")
        return True

    except (OSError, ValueError) as erro:
        print(f"\n[ERRO] Não foi possível salvar o gráfico: {erro}")
        return False

    finally:
        plt.close(fig)


def coletar_dados_multiplos(tipo_grafico, qtd_indicadores=3):
    _validar_tipo(tipo_grafico)

    try:
        qtd_indicadores = int(qtd_indicadores)
        if qtd_indicadores < 1:
            raise ValueError
    except (TypeError, ValueError):
        raise ValueError("A quantidade de indicadores deve ser positiva.")

    print(
        "\n--- Coleta de Dados Múltiplos "
        f"Comparativos ({tipo_grafico.upper()}) ---"
    )

    while True:
        anos_input = input(
            "Quais anos deseja analisar? "
            "(separe por vírgula, ex.: 2023, 2024, 2025): "
        ).strip()

        anos = [item.strip() for item in anos_input.split(",") if item.strip()]

        if not anos:
            print("Informe pelo menos um ano.")
            continue

        if any(not ano.isdigit() for ano in anos):
            print("Informe anos inteiros separados por vírgula.")
            continue

        if len(set(anos)) != len(anos):
            print("Há anos repetidos. Informe cada ano uma única vez.")
            continue

        break

    dados_completos = {}

    for i in range(qtd_indicadores):
        while True:
            nome = input(
                f"\nQual o nome do {i + 1}º indicador/operação? "
            ).strip()

            if not nome:
                print("O nome não pode ficar vazio.")
            elif nome in dados_completos:
                print("Esse nome já foi usado. Informe outro.")
            else:
                break

        valores = []
        print(f"-> Inserindo dados para: {nome.upper()}")

        for ano in anos:
            while True:
                try:
                    simbolo = "R$" if tipo_grafico == "absoluto" else "%"
                    valor = _numero_ptbr(
                        input(f"Valor em {simbolo} para {ano}: ")
                    )

                    if tipo_grafico == "percentual" and not 0 <= valor <= 100:
                        raise ValueError("Informe um percentual entre 0 e 100.")

                    valores.append(valor)
                    break

                except ValueError as erro:
                    print(f"Entrada inválida: {erro}")

        dados_completos[nome] = valores

    return anos, dados_completos


def gerar_grafico_multiplo(anos, dados_completos, tipo_grafico):
    #Gera barras agrupadas para valores monetários ou linhas para percentuais.

    try:
        _validar_tipo(tipo_grafico)

        if not anos or not dados_completos:
            raise ValueError("Informe anos e pelo menos um indicador.")

        anos = [str(ano).strip() for ano in anos]

        if any(not ano for ano in anos) or len(set(anos)) != len(anos):
            raise ValueError("Os anos devem estar preenchidos e ser únicos.")

        dados_validos = {}

        for nome, valores in dados_completos.items():
            if not str(nome).strip():
                raise ValueError("Os nomes dos indicadores não podem ficar vazios.")

            _, valores_validos = _validar_dados(
                anos, valores, tipo_grafico
            )
            dados_validos[str(nome).strip()] = valores_validos

    except (TypeError, ValueError) as erro:
        print(f"\n[AVISO] Gráfico comparativo não gerado: {erro}")
        return False

    fig, ax = plt.subplots(figsize=(10, 6))

    try:
        if tipo_grafico == "absoluto":
            import numpy as np

            x = np.arange(len(anos))
            quantidade = len(dados_validos)
            largura = min(0.8 / quantidade, 0.25)

            for i, (indicador, valores) in enumerate(dados_validos.items()):
                deslocamento = (i - (quantidade - 1) / 2) * largura

                ax.bar(
                    x + deslocamento,
                    valores,
                    width=largura,
                    label=indicador,
                    color=CORES[i % len(CORES)],
                )

            ax.set_xticks(x, anos)
            ax.set_ylabel("Valor (R$)", fontweight="bold")
            ax.yaxis.set_major_formatter(
                mtick.FuncFormatter(_formatar_moeda)
            )

        else:
            for i, (indicador, valores) in enumerate(dados_validos.items()):
                ax.plot(
                    anos,
                    valores,
                    marker=MARCADORES[i % len(MARCADORES)],
                    markersize=7,
                    linewidth=2.2,
                    label=indicador,
                    color=CORES[i % len(CORES)],
                )

            ax.set_ylabel("Percentual (%)", fontweight="bold")
            ax.yaxis.set_major_formatter(
                mtick.PercentFormatter(xmax=100, decimals=1)
            )

        ax.set_title(
            "Análise Comparativa de Indicadores",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        ax.set_xlabel("Período (anos)", fontweight="bold")
        ax.grid(True, axis="y", linestyle="--", alpha=0.6)
        ax.set_axisbelow(True)
        ax.legend(
            title="Indicadores",
            loc="upper left",
            bbox_to_anchor=(1.02, 1),
            frameon=True,
        )

        fig.tight_layout()
        nome_arquivo = "grafico_comparativo_multiplo.png"
        fig.savefig(nome_arquivo, dpi=300, bbox_inches="tight")

        print(f"\n[SUCESSO] Gráfico múltiplo salvo como '{nome_arquivo}'!")
        return True

    except (OSError, ValueError) as erro:
        print(f"\n[ERRO] Não foi possível salvar o gráfico: {erro}")
        return False

    finally:
        plt.close(fig)