import os
from src.modules.liquidez_e_capital_de_giro.liquidez import liq_geral, liq_corrente, ccLiquido
from src.modules.lucratividade_e_rentabilidade.rentabilidade import rEquity, eBITDA, mEBITDA, encurtedROIC, returnOiC
from src.modules.estrutura_e_endividamento.endividamento import relacaoCTCP, comp_ENDIVIDAMENTO

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

ebitda_calculado = None

while True:

    limpar_tela()

    print("|-----------------------------------------|")
    print("|------(INDICADORES DA KEPLER WEBER)------|")
    print("|-----------------------------------------|\n")

    print('1 - Liquidez e Capital de Giro\n2 - Lucratividade e Rentabilidade.\n3 - Estrutura e Endividamento\n0 - Sair do programa.')

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
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue

                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                    case 2:
                        try:
                            atvc = float(input('\nInforme o Ativo Circulante: R$ '))
                            pc = float(input('Informe o Passivo Circulante: R$ '))

                            l_Corrente = liq_corrente(atvc, pc)
                            if l_Corrente is not None:
                                print(f'\nO valor da Liquidez Corrente é: R$ {l_Corrente:.2f}')
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue

                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                    case 3:
                        try:
                            atvc = float(input('\nInforme o Ativo Circulante: R$ '))
                            pc = float(input('Informe o Passivo Circulante: R$ '))

                            c_Liquido = ccLiquido(atvc, pc)
                            if c_Liquido is not None:
                                print(f'\nO valor da Capital Circulante Líquida é: R$ {c_Liquido:.2f}')
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue
                            
                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                    case 0:
                        break
                    case _:
                        input('Opção inválida. Aperte [ENTER] para continuar...')
        case 2:
            while True:

                limpar_tela()

                print("1 - Calcular o Retorno Sobre o Patrimonio Líquido (ROE).\n2 - Calcular os Lucros Antes de Juros, Impostos, Depreciação e Amortização (EBITDA).\n3 - Calcular a Margem de EBITDA.\n4 - Calcular o Retorno Sobre o Capital Investido (ROIC).\n0 - Voltar ao Menu Principal")
                
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
                                print(f'\nO valor do Retorno Sobre o Patrimonio Líquido (ROE) é: {r_Equity:.2f}%')
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue
                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                    
                    case 2:
                        try:
                            l_Operacional = float(input('\nInforme o Lucro Operacional: R$ '))
                            dp = float(input('Informe a Depreciação: R$ '))
                            am = float(input('Informe a Amortização: R$ '))

                            ebitda_calculado = eBITDA(l_Operacional, dp, am)
                            print(f'\nO valor do Lucros Antes de Juros, Impostos, Depreciação e Amortização (EBITDA) é: R$ {ebitda_calculado:.2f}')
                            input('Aperte [ENTER] para continuar...')
                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                    
                    case 3:
                        try:
                            ebitda_atual = 0
                            confirmation = input(f'Deseja utilizar o EBITDA R$ {ebitda_calculado:.2f} calculado anteriormente (Sim/Não)? ').lower()

                            if ((confirmation != "sim") and (confirmation != "não")):
                                input('Digite apenas Caracteres válidos.\nAperte [ENTER] para continuar...')
                                continue
                            elif confirmation == "sim":
                                ebitda_atual = ebitda_calculado
                            else:
                                try:
                                    ebitda_atual = float(input('Digite o valor do EBITDA: R$ '))
                                except ValueError:
                                    input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                    continue
                            
                            try:
                                receita_liquida = float(input('Informe Receita Líquida: R$ '))
                                margem_EBITDA = mEBITDA(ebitda_atual, receita_liquida)

                                if margem_EBITDA is not None:
                                    print(f'A Margem EBITDA calculada é: {margem_EBITDA:.2f}%')
                                    input('Aperte [ENTER] para continuar...')
                                else:
                                    continue
                            except ValueError:
                                input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                continue
                        except ValueError:
                            input('ERROR! Digite apenas caracteres válidos.\nAperte [ENTER] para continuar...')
                            continue
                    
                    case 4:
                        try:
                            check = input('Você já possui o NOPAT calculado (Sim/Não)? ').lower()
                            if ((check != "sim") and (check != "não")):
                                input('Caractere inválido. Digite o que se pede.\nAperte [ENTER] para continuar...')
                                continue
                            elif check == "sim":
                                nopat = float(input('Informe o NOPAT: R$ '))

                                try:
                                    pL = float(input('Informe o Patrimônio Líquido: R$ '))
                                    divBruta = float(input('Informe o Passivo Oneroso: R$ '))
                                    caixa = float(input('Informe o valor de Caixa e Equivalente: R$ '))
                                    pO = divBruta - caixa
                                    roic = returnOiC(nopat, pL, pO)
                                    if roic is not None:
                                        print(f'O valor relativo/percentual do ROIC é: {roic:.2f}')
                                        input('Aperte [ENTER] para continuar...')
                                    else:
                                        continue

                                except ValueError:
                                    input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                    continue
                            else:
                                try:
                                    ebitN = float(input('Informe o valor do EBIT: R$ '))
                                    isl = float(input('Informe os Impostos Sobre o Lucro: R$ '))
                                    cNOPAT = ebitN - isl

                                    try:
                                        check1 = input('Você já possui o valor calculado do Capital Investido (Sim/Não)? ').lower()
                                        if ((check1 != "sim") and (check1 != "não")):
                                            input('Digite apenas Caracteres válidos.\nAperte [ENTER] para continuar...')
                                            continue
                                        elif check1 == "sim":
                                            try:
                                                cINVESTIDO = float(input('Informe-o: R$ '))
                                                enROIC = encurtedROIC(cNOPAT, cINVESTIDO)

                                                if enROIC is not None:
                                                    print(f'O valor relativo/percentual do ROIC é: {enROIC:.2f}%')
                                                    input('Aperte [ENTER] para continuar...')
                                                else:
                                                    continue
                                            
                                            except ValueError:
                                                input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                                continue
                                        else:
                                            pass
                                    
                                    except ValueError:
                                        input('ERROR! Digite apenas caracteres válidos.\nAperte [ENTER] para continuar...')
                                        continue
                                
                                except ValueError:
                                    input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                    continue

                            try:
                                check2 = input('Você já possui o valor calculado do Capital Investido (Sim/Não)? ').lower()
                                if ((check2 != "sim") and (check2 != "não")):
                                    input('Digite apenas Caracteres válidos.\nAperte [ENTER] para continuar...')
                                    continue
                                elif check2 == "sim":
                                    try:
                                        cInvestido = float(input('Informe-o: R$ '))
                                        eROIC = encurtedROIC(nopat, cInvestido)

                                        if eROIC is not None:
                                            print(f'O valor relativo/percentual do ROIC é: {eROIC:.2f}%')
                                            input('Aperte [ENTER] para continuar...')
                                        else:
                                            continue
                                    
                                    except ValueError:
                                        input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                        continue
                                else:
                                    try:
                                        pl = float(input('Informe o Patrimônio Líquido: R$ '))
                                        po = float(input('Informe o Passivo Oneroso: R$ '))

                                        roic = returnOiC(nopat, pl, po)
                                        if roic is not None:
                                            print(f'O valor relativo/percentual do ROIC é: {roic:.2f}')
                                            input('Aperte [ENTER] para continuar...')
                                        else:
                                            continue

                                    except ValueError:
                                        input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                                        continue
                            
                            except ValueError:
                                input('ERROR! Digite apenas caracteres válidos.\nAperte [ENTER] para continuar...')
                                continue
                        
                        except ValueError:
                            input('ERROR! Digite apenas caracteres válidos.\nAperte [ENTER] para continuar...')
                            continue

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
                
                match userOption:
                    case 1:
                        try:
                            ct = float(input('Digite o Capital de Terceiros (Passivo Total): R$ '))
                            cp = float(input('Digite o Capital Próprio (Patrimônio Líquido): R$ '))

                            r_CTCP = relacaoCTCP(ct, cp)
                            if r_CTCP is not None:
                                print(f'O valor relativo/percentual da Relação CT/CP é de {r_CTCP:.2f}%.')
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue
                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                            continue
                    case 2:
                        try:
                            pc = float(input('Digite o Passivo Circulante: R$ '))
                            pnc = float(input('Digite o Passivo Não Circulante: R$ '))

                            composicao_Endividamento = comp_ENDIVIDAMENTO(pc, pnc)
                            if composicao_Endividamento is not None:
                                print(f'O valor relativo/percentual da Composição do Endividamento é {composicao_Endividamento:.2f}%.')
                                input('Aperte [ENTER] para continuar...')
                            else:
                                continue
                        except ValueError:
                            input('ERROR! Digite apenas números com um "." para casas decimais.\nAperte [ENTER] para continuar...')
                            continue
                    case 0:
                        break
                    case _:
                        input('Opção inválida! Aperte [ENTER] para continuar...')
        case 0:
            print('Encerrando o programa...')
            break
        case _:
            input('Opção inválida. Aperte [ENTER] para continuar...')