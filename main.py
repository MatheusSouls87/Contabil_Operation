import os
from src.modules.liquidez_e_capital_de_giro.liquidez import liq_geral, liq_corrente, ccLiquido
from src.modules.lucratividade_e_rentabilidade.rentabilidade import rEquity, eBITDA, mEBITDA, encurtedROIC, returnOiC
from src.modules.estrutura_e_endividamento.endividamento import relacaoCTCP, comp_ENDIVIDAMENTO
from src.modules.arquivos import gerenciador

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

ebitda_calculado = None
relatorio_ativo = None

def ask_save(category, indicator, value):
    global relatorio_ativo

    if relatorio_ativo is None:
        print("\n[AVISO] Nenhum relatório ativo no momento. O valor não será guardado no histórico.")
        return
    
    response = input(f"Deseja anexar este resultado ao relatório '{relatorio_ativo}' (s/n)? ").strip().lower()
    if response in ['s', 'sim']:
        note = input('Deseja adicionar alguma nota ou observação (deixe em branco se não quiser)? ')
        sucess = gerenciador.add_indicator(relatorio_ativo, category, indicator, value, note)

        if sucess:
            print('[✓] Indicador anexado com sucesso!')
        else:
            print('[X] Erro ao anexar. O relatório pode ter sido apagado ou movido.')

while True:
    limpar_tela()

    print("|-----------------------------------------|")
    print("|------(INDICADORES DA KEPLER WEBER)------|")
    print("|-----------------------------------------|\n")

    print('1 - Liquidez e Capital de Giro\n2 - Lucratividade e Rentabilidade.\n3 - Estrutura e Endividamento\n4 - Gerenciador de Relatórios\n0 - Sair do programa.')

    try:
        userPut = int(input('Escolha o que deseja operar: '))
    except ValueError:
        input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
        continue
    
    match userPut:
        case 1:            
            while True:
                limpar_tela()
                print('1 - Calcular a Liquidez Geral.\n2 - Calcular a Liquidez Corrente.\n3 - Calcular a Capital Circulante Líquida (CCL)\n0 - Voltar ao Menu Principal.')

                try:
                    option = int(input('Escolha o que deseja operar: '))
                except ValueError:
                    input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
                    continue

                match option:
                    case 1:
                        try:
                            atvc = float(input('\nInforme o Ativo Circulante: R$ '))
                            rlp = float(input('Informe o Realizável a Longo Prazo: R$ '))
                            pc = float(input('Informe o Passivo Circulante: R$ '))
                            elp = float(input('Informe o Exigível a Longo Prazo: R$ '))
                        
                            l_Geral = liq_geral(atvc, rlp, pc, elp)
                            if l_Geral is not None:
                                print(f'\nO valor da Liquidez Geral é: R$ {l_Geral:.2f}')

                                ask_save("Liquidez e Capital de Giro", "Liquidez Geral", l_Geral)
                            else:
                                print('\nERRO! Divisão por zero. O Passivo e Exigível não podem ser zero.')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 2:
                        try:
                            atvc = float(input('\nInforme o Ativo Circulante: R$ '))
                            pc = float(input('Informe o Passivo Circulante: R$ '))

                            l_Corrente = liq_corrente(atvc, pc)
                            if l_Corrente is not None:
                                print(f'\nO valor da Liquidez Corrente é: R$ {l_Corrente:.2f}')
                                ask_save("Liquidez e Capital de Giro", "Liquidez Corrente", liq_corrente)
                            else:
                                print('\nERRO! Divisão por zero. O Passivo Circulante não pode ser zero.')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 3:
                        try:
                            atvc = float(input('\nInforme o Ativo Circulante: R$ '))
                            pc = float(input('Informe o Passivo Circulante: R$ '))

                            c_Liquido = ccLiquido(atvc, pc)
                            print(f'\nO valor da Capital Circulante Líquida é: R$ {c_Liquido:.2f}')
                            ask_save("Liquidez e Capital de Giro", "Capital Circulante Líquido (CCL)", c_Liquido)
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 0:
                        break
                    case _:
                        input('Opção inválida. Aperte [ENTER] para continuar...')
        
        case 2:
            while True:
                limpar_tela()
                print("1 - Calcular o Retorno Sobre o Patrimonio Líquido (ROE).\n2 - Calcular o EBITDA.\n3 - Calcular a Margem de EBITDA.\n4 - Calcular o Retorno Sobre o Capital Investido (ROIC).\n0 - Voltar ao Menu Principal")
                
                try:
                    option1 = int(input('Escolha o que deseja operar: '))
                except ValueError:
                    input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
                    continue

                match option1:
                    case 1:
                        try:
                            ll = float(input('\nInforme o Lucro Líquido: R$ '))
                            pl = float(input('Informe o Patrimônio Líquido: R$ '))

                            r_Equity = rEquity(ll, pl)
                            if r_Equity is not None:
                                print(f'\nO valor do ROE é: {r_Equity:.2f}%')
                                ask_save("Lucratividade e Rentabilidade", "Return of Equity (ROE)", r_Equity)
                            else:
                                print('\nERRO! Divisão por zero. O Patrimônio Líquido não pode ser zero.')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 2:
                        try:
                            l_Operacional = float(input('\nInforme o Lucro Operacional: R$ '))
                            dp = float(input('Informe a Depreciação: R$ '))
                            am = float(input('Informe a Amortização: R$ '))

                            ebitda_calculado = eBITDA(l_Operacional, dp, am)
                            print(f'\nO valor do EBITDA é: R$ {ebitda_calculado:.2f}')
                            ask_save("Lucratividade e Rentabilidade", "Lucro antes de Juros, Impostos, Depreciação e Amortização (EBITDA)", ebitda_calculado)
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 3:
                        try:
                            ebitda_atual = 0
                            
                            if ebitda_calculado is not None:
                                confirmation = input(f'Deseja utilizar o EBITDA R$ {ebitda_calculado:.2f} calculado anteriormente (s/n)? ').strip().lower()
                                if confirmation in ['s', 'sim']:
                                    ebitda_atual = ebitda_calculado
                                elif confirmation in ['n', 'nao', 'não']:
                                    ebitda_atual = float(input('Digite o valor do EBITDA: R$ '))
                                else:
                                    input('Opção inválida. Aperte [ENTER] para continuar...')
                                    continue
                            else:
                                ebitda_atual = float(input('Digite o valor do EBITDA: R$ '))

                            receita_liquida = float(input('Informe Receita Líquida: R$ '))
                            margem_EBITDA = mEBITDA(ebitda_atual, receita_liquida)

                            if margem_EBITDA is not None:
                                print(f'A Margem EBITDA calculada é: {margem_EBITDA:.2f}%')
                                ask_save("Lucratividade e Rentabilidade", "Margem EBITDA", margem_EBITDA)
                            else:
                                print('\nERRO! A Receita Líquida não pode ser zero.')
                            input('Aperte [ENTER] para continuar...')
                            
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                    
                    case 4:
                        try:
                            check = input('Você já possui o NOPAT calculado (s/n)? ').strip().lower()
                            if check not in ['s', 'sim', 'n', 'nao', 'não']:
                                input('Opção inválida. Aperte [ENTER] para continuar...')
                                continue
                            
                            nopat = 0
                            if check in ['s', 'sim']:
                                nopat = float(input('Informe o NOPAT: R$ '))
                            else:
                                ebitN = float(input('Informe o valor do EBIT: R$ '))
                                isl = float(input('Informe os Impostos Sobre o Lucro: R$ '))
                                nopat = ebitN - isl

                            check2 = input('Você já possui o valor calculado do Capital Investido (s/n)? ').strip().lower()
                            if check2 not in ['s', 'sim', 'n', 'nao', 'não']:
                                input('Opção inválida. Aperte [ENTER] para continuar...')
                                continue
                            
                            roic_result = None
                            if check2 in ['s', 'sim']:
                                cInvestido = float(input('Informe o Capital Investido: R$ '))
                                roic_result = encurtedROIC(nopat, cInvestido)
                            else:
                                pl = float(input('Informe o Patrimônio Líquido: R$ '))
                                divBruta = float(input('Informe o Passivo Oneroso (Dívida Bruta): R$ '))
                                caixa = float(input('Informe o valor de Caixa e Equivalente: R$ '))
                                po = divBruta - caixa
                                roic_result = returnOiC(nopat, pl, po)

                            if roic_result is not None:
                                print(f'O valor relativo/percentual do ROIC é: {roic_result:.2f}%')
                                ask_save("Lucratividade e Rentabilidade", "Retorno Sobre o Capítal Investido (ROIC)", roic_result)
                            else:
                                print('\nERRO! Divisão por zero no cálculo do ROIC.')
                            input('Aperte [ENTER] para continuar...')

                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')

                    case 0:
                        break
                    case _:
                        input('Opção inválida. Aperte [ENTER] para continuar...')

        case 3:
            while True:
                limpar_tela()
                print('1 - Calcular a Relação CT/CP (Endividamento).\n2 - Calcular a Composição do Endividamento.\n0 - Voltar ao Menu Principal.')

                try:
                    userOption = int(input('Escolha o que deseja operar: '))
                except ValueError:
                    input('ERROR! Opção digite um número.\nAperte [ENTER] para continuar...')
                    continue
                
                match userOption:
                    case 1:
                        try:
                            ct = float(input('Digite o Capital de Terceiros (Passivo Total): R$ '))
                            cp = float(input('Digite o Capital Próprio (Patrimônio Líquido): R$ '))

                            r_CTCP = relacaoCTCP(ct, cp)
                            if r_CTCP is not None:
                                print(f'O valor relativo/percentual da Relação CT/CP é de {r_CTCP:.2f}%.')
                                ask_save("Estrutura e Endividamento", "Relação CT/CP", r_CTCP)
                            else:
                                print('\nERRO! O Capital Próprio não pode ser zero.')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                            
                    case 2:
                        try:
                            pc = float(input('Digite o Passivo Circulante: R$ '))
                            pnc = float(input('Digite o Passivo Não Circulante: R$ '))

                            composicao_Endividamento = comp_ENDIVIDAMENTO(pc, pnc)
                            if composicao_Endividamento is not None:
                                print(f'O valor relativo/percentual da Composição do Endividamento é {composicao_Endividamento:.2f}%.')
                                ask_save("Estrutura e Endividamento", "Composição do Endividamento", composicao_Endividamento)
                            else:
                                print('\nERRO! O Passivo Total não pode ser zero.')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com "." para decimais. Aperte [ENTER]...')
                            
                    case 0:
                        break
                    case _:
                        input('Opção inválida! Aperte [ENTER] para continuar...')
        
        case 4:
            while True:
                limpar_tela()
                print('--- GERENCIADOR DE RELATÓRIOS ---')
                print('1 - Listar e Ler Relatórios Salvos.\n2 - Criar Novo Relatório (Em Breve).\n0 - Voltar ao Menu Principal.')

                try:
                    op_archive = int(input('\nEscolha a operação: '))
                except ValueError:
                    input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
                    continue

                match op_archive:
                    case 1:
                        saved_files = gerenciador.list_files()

                        if len(saved_files) == 0:
                            print('\nNenhum relatório encontrado no sistema.')
                            input('Aperte [ENTER] para continuar...')
                        else:
                            print('\nRelatórios Disponíveis:')
                            for i, arq in enumerate(saved_files):
                                clean_name = arq.replace(gerenciador.extension, "")
                                print(f'[{i+1}] - {clean_name}')
                            
                            try:
                                choose = int(input('\nDigite o número do relatório que deseja abrir (0 para cancelar): '))
                                if choose > 0 and choose <= len(saved_files):
                                    archive_choose = saved_files[choose - 1]
                                    conteudo = gerenciador.read_files(archive_choose)

                                    limpar_tela()
                                    print(conteudo)
                                    
                                    define = input('Deseja definir este relatório como o ativo no momento (s/n)? ').strip().lower()
                                    if define not in ['s', 'sim', 'n', 'nao', 'não']:
                                        input('Opção inválida. Aperte [ENTER] para continuar...')
                                        continue

                                    if define in ['s', 'sim']:
                                        relatorio_ativo = archive_choose
                                        print(f"Relatório '{relatorio_ativo}' definido como ativo.")
                                    else:
                                        pass

                                    input('\nFim do relatório. Aperte [ENTER] para continuar...')
                                elif choose != 0:
                                    input('Número inválido. Aperte [ENTER] para continuar...')
                            except ValueError:
                                input('ERRO! Digite apenas o número correspondente.\nAperte [ENTER] para continuar...')
                    
                    case 2:
                        limpar_tela()
                        print("--- CRIAR NOVO RELATÓRIO ---")
                        new_name = input('Digite o nome do projeto/relatório (ex: kepler_2025): ').strip()
                        describe = input('Digite uma breve descrição para este relatório: ').strip()

                        sucess = gerenciador.create_new_archive(new_name, describe)

                        if sucess:
                            relatorio_ativo = new_name
                            print(f"\n[✓] Relatório '{new_name}{gerenciador.extension}' criado com sucesso!")
                            print("Este relatório está agora ATIVO. Todos os novos cálculos podem ser guardados nele.")
                        else:
                            print(f"\n[X] Já existe um relatório com esse nome '{new_name}'.")
                        
                        input('\nAperte [ENTER] para continuar...')
                    case 0:
                        break
                    case _:
                        input('Opção inválida. Aperte [ENTER] para continuar...')

        case 0:
            print('Encerrando o programa...')
            break
        case _:
            input('Opção inválida. Aperte [ENTER] para continuar...')