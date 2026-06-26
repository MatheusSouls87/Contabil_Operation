# 📊 Sistema de Análise e Gráficos Contábeis

Este projeto é uma aplicação interativa de terminal (CLI) desenvolvida em Python. Seu objetivo principal é facilitar o cálculo de indicadores contábeis essenciais, gerar relatórios em texto e criar gráficos visuais para análise de desempenho financeiro ao longo do tempo.

---

## ✨ Funcionalidades

O sistema é dividido em módulos interativos acessados via menu:

* **🧮 Cálculos de Indicadores:** 
    * **Liquidez e Capital de Giro:** Liquidez Geral, Liquidez Corrente, Capital Circulante Líquido (CCL).
    * **Lucratividade e Rentabilidade:** ROE, EBITDA, Margem EBITDA, ROIC.
    * **Estrutura e Endividamento:** Relação Capital de Terceiros / Capital Próprio, Composição do Endividamento.
* **📝 Gerador de Relatórios:** Salva o histórico de cálculos e análises em arquivos `.txt`.
* **📈 Gerador de Gráficos:**
    * **Gráficos Absolutos (Barras):** Evolução de valores monetários (R$).
    * **Gráficos Percentuais (Linhas):** Evolução de margens e taxas (%).
    * **Gráficos Comparativos:** Plota múltiplos indicadores no mesmo gráfico (ex: comparar ROIC, ROE e Margem EBITDA ao mesmo tempo).

---

## 🛠️ Pré-requisitos

Para rodar este projeto, você precisará ter o **Python** instalado na sua máquina (versão 3.8 ou superior recomendada). 

> **Aviso para usuários de Windows:** Durante a instalação do Python, certifique-se de marcar a caixa **"Add Python.exe to PATH"** na tela inicial do instalador.

---

## 🚀 Como Instalar e Configurar

Siga o passo a passo abaixo no terminal da sua máquina (Prompt de Comando, PowerShell ou terminal do VS Code) para garantir que o código rode perfeitamente:

**1. Extraia os arquivos**
Abra a pasta do projeto no seu editor de código ou navegue até ela pelo terminal.

**2. Crie um Ambiente Virtual (Recomendado)**
Isso isola as bibliotecas do projeto da sua máquina. Digite:
```bash
python -m venv .venv
```

**3. Ative o Ambiente no Windows**
 * No Windows:
```bash
.venv\Scripts\activate
```
 * No Mac/Linux:
```bash
source .venv/bin/activate
```
(Se ativado corretamente, você verá um (.venv) verde no início da linha do terminal).

**4. Instale as Dependências**

O sistema utiliza a biblioteca ``` matplotlib ``` 
para desenhar os gráficos. Instale as dependências lendo o arquivo de requisitos:
```bash
pip install -r requirements.txt
```

(Caso o arquivo requirements.txt não exista, você pode instalar a biblioteca manualmente digitando: ``` pip install matplotlib ```).

---

# 💻 Como Usar
Com o ambiente ativado e as dependências instaladas, basta iniciar o arquivo principal do programa:
```bash
python main.py
```
Um menu interativo aparecerá na tela. Digite o número da opção desejada e siga as instruções.

 * Para inserir valores em dinheiro, utilize apenas números, usando ponto ou vírgula para os centavos (ex: 150000.50).

 * Os gráficos gerados serão salvos automaticamente na mesma pasta do projeto no formato .png.

---

# 📂 Estrutura do Projeto

 * ``` main.py ``` - Arquivo principal que gerencia o menu e o fluxo do usuário.

 * ``` src/modules/graficos.py ``` - Módulo responsável pela coleta de dados temporais e renderização dos gráficos usando matplotlib.

 * ``` requirements.txt ``` - "Lista de compras" contendo as bibliotecas externas necessárias para rodar o projeto.