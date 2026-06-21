import os #operation system
from src.desempenho_do_imobilizado.producao_por_imobilizado import prod_imobilizado

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    limpar_tela()

    print('1 - Desempenho do Imobilizado\n2 - Em desenvolvimento.\n0 - Sair do programa.')

    try:
        userPut = int(input('Escolha o que deseja operar: '))
    except ValueError:
        input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
    
    match userPut:
        case 1:            
            while True:

                limpar_tela()

                print('1 - Produção por Imobilizado.\n2 - Em desenvolvimento.\n3 - Em desenvolvimento.\n0 - Voltar ao Menu Principal.')

                try:
                    option = int(input('Escolha o que deseja operar: '))
                except ValueError:
                    input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
                    continue

                match option:
                    case 1:
                        cp = float(input('Digite o custo de produção: R$ '))
                        ail = float(input('Digite o Ativo Imobilizado Líquido: R$ '))
                        
                        p_mob = prod_imobilizado(cp, ail)
                        if p_mob is not None:
                            print(f'O valor da Produção por Imobilizado é: R$ {p_mob}')
                            input('Aperte [ENTER] para continuar...')
                        else:
                            continue
                
                    case 2:
                        input('Opção em desenvolvimento. Aperte [ENTER] para continuar...')
                    case 3:
                        input('Opção em desenvolvimento. Aperte [ENTER] para continuar...')
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