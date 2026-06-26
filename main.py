from equipes import adicionar_nomes, embaralhar_grupos, exibir_grupos

cor_finalizar = '\033[m'
cor_ciano_negrito = '\033[1;36;38m'
cor_vermelho_negrito = '\033[1;31;38m'
cor_verde_negrito = '\033[1;32;38m'
cor_amarelo_negrito = '\033[1;33;38m'
cor_azul_negrito = '\033[1;34;38m'
cor_magenta_negrito = '\033[1;35;38m'
cor_branco_negrito = '\033[1;37;38m'
cor_fundo_vermelho = '\033[1;31;41m'

def menu():
    print(cor_ciano_negrito + '========= Sistema de Torneios =========' + cor_finalizar)
    print(cor_verde_negrito + '1. Formar equipes' + cor_finalizar)
    print(cor_amarelo_negrito + '2. Gerar chaveamento' + cor_finalizar)
    print(cor_azul_negrito + '3. Formar equipes e gerar chaveamento' + cor_finalizar)
    print(cor_magenta_negrito + '4. Ver histórico de chaveamentos' + cor_finalizar)
    print(cor_vermelho_negrito + '5. Sair' + cor_finalizar)
    opcao = input(cor_branco_negrito + 'Escolha uma opção: ' + cor_ciano_negrito)
    print(cor_finalizar)
    return opcao

if __name__ == '__main__':
    while True:
        opcao = menu()

        if opcao == '1':
            print(cor_verde_negrito + 'Você escolheu formar equipes')
            
            nomes = adicionar_nomes()

            while True:
                try:
                    tamanho = int(input(f'\nQuantas pessoas por grupo? (2 a {len(nomes)}): '))
                    if 2 <= tamanho <= len(nomes):
                        break
                    print('Valor inválido. tente novamente.')
                except ValueError:
                    print('Digite um número inteiro.')

            while True:
                grupos = embaralhar_grupos(nomes, tamanho)
                exibir_grupos(grupos)

                repetir = input('\nEmbaralhar novamente? (s/n): ').strip().lower()
                if repetir != 's':
                    break

        elif opcao == '2':
            print(cor_amarelo_negrito + 'Você escolheu gerar chaveamento')
        elif opcao == '3':
            print(cor_azul_negrito + 'Você escolheu formar equipes e gerar chaveamento')
        elif opcao == '4':
            print(cor_magenta_negrito + 'Você escolheu ver o histórico')
        elif opcao == '5':
            print(cor_vermelho_negrito + 'Saindo...' + cor_finalizar)
            break
        else:
            print(cor_fundo_vermelho + 'Opção inválida, tente novamente!' + cor_finalizar)
