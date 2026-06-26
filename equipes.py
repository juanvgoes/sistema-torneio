import random
def adicionar_nomes():
    nomes = []
    print('===sorteador de grupos ===')
    print('digite os nomes um por um. Deixe em branco e pressione enter para finalizar . \n')
    while True:
        nome = input('nome: ').strip()
        if nome == '':
            break
        nomes.append(nome)
    return nomes

def embaralhar_grupos(nomes, tamanho_grupo):
    shuffle = nomes[:]
    random.shuffle(shuffle)
    grupos = []
    for i in range(0, len(shuffle), tamanho_grupo):
        grupos.append(shuffle[i:i + tamanho_grupo])
    return grupos

def exibir_grupos(grupos):
    print('\n=== Grupos Sorteados ===')
    for i, grupo in enumerate(grupos, start=1):
        print(f'Grupo {i}: {", ".join(grupo)}')

def main():
    nomes = adicionar_nomes()

    if len(nomes) < 2:
        print('Adicione pelo menos 2 pessoas para formar grupos.')
        return

    print(f'\n{len(nomes)} pessoa(s) adicionadas(s): {", ".join(nomes)}')

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

    print('\nAté mais!')

if __name__ == '__main__':
    main()
