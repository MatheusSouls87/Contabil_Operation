import os
from src.modules.liquidez_e_capital_de_giro.liquidez import liq_geral, liq_corrente, ccLiquido

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    limpar_tela()

    print("|-----------------------------------------|")
    print("|------(INDICADORES DA KEPLER WEBER)------|")
    print("|-----------------------------------------|\n")

    print('1 - Liquidez e Capital de Giro\n2 - Em desenvolvimento.\n0 - Sair do programa.')

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
            input('Opção em desenvolvimento. Aperte [ENTER] para continuar...')
        case 0:
            print('Encerrando o programa...')
            break
        case _:
            input('Opção inválida. Aperte [ENTER] para continuar...')