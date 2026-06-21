import os #operation system
from src.desempenho_do_imobilizado import prod_imobilizado

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:

    limpar_tela()

    print('1 - Desempenho do Imobilizado\n')

    try:
        userPut = int(input('Escolha o que deseja operar: '))
    except ValueError:
        input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
    
    match userPut:
        case 1:
            limpar_tela()

            print('1 - Produção por Imobilizado.\n2 - Em desenvolvimento.\n3 - Em desenvolvimento.\n0 - Voltar ao Menu Principal.')

            try:
                option = int(input('Escolha o que deseja operar: '))
            except ValueError:
                input('ERROR! Digite um número. Aperte [ENTER] para continuar...')
                continue
            
            while True:
                match option:
                    case 1:
                        cp = double(input('Digite o custo de produção: R$ '))
                        try:
                            ail = double(input('Digite o Ativo Imobilizado Líquido: R$ '))
                        except ValueError:
                            input('ERROR! Divisão por zero. Aperte [ENTER] para continuar...')
                            continue

                        p_mob = prod_imobilizado(cp, ail)
                        print(f'O valor da Produção por Imobilizado é: R$ {p_mob}')
                
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