def menu():
    print('========= Sistema de Torneios =========')
    print('1. Formar equipes')
    print('2. Gerar chaveamento')
    print('3. Formar equipes e gerar chaveamento')
    print('4. Ver histórico de chaveamentos')
    print('5. Sair')
    opcao = input('Escolha uma opção: ')
    return opcao

if __name__ == '__main__':
    while True:
        opcao = menu()

        if opcao == '1':
            print('Você escolheu formar equipes')
        elif opcao == '2':
            print('Você escolheu gerar chaveamento')
        elif opcao == '3':
            print('Você escolheu formar equipes e gerar chaveamento')
        elif opcao == '4':
            print('Você escolheu ver o histórico')
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção inválida, tente novamente!')