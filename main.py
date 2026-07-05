from equipes import adicionar_nomes, embaralhar_grupos, exibir_grupos
from chaveamento import receber_equipes, gerar_fase_de_grupos, gerar_mata_mata, gerar_pontos_corridos
from arquivos import listar_salvos, carregar_chaveamento

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
            print(cor_verde_negrito + 'Você escolheu formar equipes' + cor_finalizar)
            
            nomes = adicionar_nomes()

            while True:
                try:
                    tamanho = int(input(f'\n{cor_verde_negrito}Quantas pessoas por grupo? (2 a {len(nomes)}): {cor_ciano_negrito}'))
                    print(cor_finalizar)
                    if 2 <= tamanho <= len(nomes):
                        break
                    print(cor_vermelho_negrito + 'Valor inválido. tente novamente.' + cor_finalizar)
                except ValueError:
                    print(cor_fundo_vermelho + 'Digite um número inteiro.' + cor_finalizar)

            while True:
                grupos = embaralhar_grupos(nomes, tamanho)
                exibir_grupos(grupos)

                repetir = input(f'\n{cor_amarelo_negrito}Embaralhar novamente? (s/n): ').strip().lower()
                print(cor_finalizar)
                if repetir != 's':
                    break

        elif opcao == '2':
            print(cor_amarelo_negrito + 'Você escolheu gerar chaveamento' + cor_finalizar)
            print(cor_ciano_negrito + 'Escolha o modo de chaveamento: ' + cor_finalizar)
            print(f'{cor_ciano_negrito}[{cor_vermelho_negrito}1{cor_ciano_negrito}]{cor_vermelho_negrito} Mata-mata{cor_finalizar}')
            print(f'{cor_ciano_negrito}[{cor_verde_negrito}2{cor_ciano_negrito}]{cor_verde_negrito} Pontos corridos{cor_finalizar}')
            print(f'{cor_ciano_negrito}[{cor_azul_negrito}3{cor_ciano_negrito}]{cor_azul_negrito} Fase de grupos{cor_finalizar}')
            modo = input(f'{cor_amarelo_negrito}Modo: {cor_ciano_negrito}').strip()
            print(cor_finalizar)

            equipes = receber_equipes()

            while True:
                if modo == '1':
                    gerar_mata_mata(equipes)
                    break
                elif modo == '2':
                    gerar_pontos_corridos(equipes)
                    break
                elif modo == '3':
                    gerar_fase_de_grupos(equipes)
                    break
                else:
                    print('Digite apenas 1, 2 ou 3')

        
        elif opcao == '3':
            print(cor_azul_negrito + 'Você escolheu formar equipes e gerar chaveamento' + cor_finalizar)
            
            nomes = adicionar_nomes()

            while True:
                try:
                    tamanho = int(input(f'\n{cor_verde_negrito}Quantas pessoas por grupo? (2 a {len(nomes)}): {cor_ciano_negrito}'))
                    print(cor_finalizar)
                    if 2 <= tamanho <= len(nomes):
                        break
                    print(cor_vermelho_negrito + 'Valor inválido. tente novamente.' + cor_finalizar)
                except ValueError:
                    print(cor_fundo_vermelho + 'Digite um número inteiro.' + cor_finalizar)

            while True:
                grupos = embaralhar_grupos(nomes, tamanho)
                exibir_grupos(grupos)

                repetir = input(f'\n{cor_amarelo_negrito}Embaralhar novamente? (s/n): ').strip().lower()
                print(cor_finalizar)
                if repetir != 's':
                    break

            print('Escolha o modo de chaveamento: ')
            print('[1] Mata-mata')
            print('[2] Pontos corridos')
            print('[3] Fase de grupos')
            modo = input("Modo: ").strip()

            equipes = grupos

            while True:
                if modo == '1':
                    gerar_mata_mata(equipes)
                    break
                elif modo == '2':
                    gerar_pontos_corridos(equipes)
                    break
                elif modo == '3':
                    gerar_fase_de_grupos(equipes)
                    break
                else:
                    print('Digite apenas 1, 2 ou 3')

        elif opcao == '4':
            print(cor_magenta_negrito + 'Você escolheu ver o histórico' + cor_finalizar)

            print('Esses são os arquivos salvos: ')
            listar_salvos()

            arquivo = input('Digite o arquivo que deseja carregar: ')
            carregar_chaveamento(arquivo)




        elif opcao == '5':
            print(cor_vermelho_negrito + 'Saindo...' + cor_finalizar)
            break
        else:
            print(cor_fundo_vermelho + 'Opção inválida, tente novamente!' + cor_finalizar)
