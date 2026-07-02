import random
import arquivos

def receber_equipes():
    equipes = []
    print('Digite o nome das equipes e deixe em branco para finalizar')
    while True:
        nome = input(f'Equipe {len(equipes) + 1} ').strip()
        if nome == '':
            if len(equipes) < 2:
                print('É preciso ter pelo menos 2 equipes')
                continue
            break
        equipes.append(nome)
    return equipes

def equipe_isenta(equipes):
    if len(equipes) % 2 != 0:
        isenta = random.choice(equipes)
        equipes.remove(isenta)
        print(f'Como o número de equipes é ímpar. {isenta} passou direto como equipe isenta')
        return equipes, isenta
    return equipes, None

def escolher_vencedor(equipe_a, equipe_b):
    while True:
        print(f'({equipe_a} X {equipe_b})')
        opcao = input('Qual das equipes ganhou [1] ou [2]? ')
        if opcao == '1':
            return equipe_a
        elif opcao == '2':
            return equipe_b
        else:
            print('Opção inválida')

def gerar_mata_mata(equipes, salvar=True):
    rodada = 1
    historico = []

    while len(equipes) > 1:
        print(f'Rodada {rodada}')

        equipes, isenta = equipe_isenta(equipes)
        
        vencedores = []
        confrontos_rodada = []
        for c in range(0, len(equipes), 2):
            equipe_a = equipes[c]
            equipe_b = equipes[c + 1]
            print(f'confronto: {equipe_a} VS {equipe_b}')
            vencedor = escolher_vencedor(equipe_a, equipe_b)
            print(f'{vencedor} Avança')
            vencedores.append(vencedor)
            confrontos_rodada.append({
                'equipe_a': equipe_a,
                'equipe_b': equipe_b,
                'vencedor': vencedor
            })
        if isenta:
            vencedores.append(isenta)

        historico.append({
            'rodada': rodada,
            'confrontos': confrontos_rodada,
            'isenta': isenta
        })
        
        equipes = vencedores
        rodada += 1 
        
    campeao = equipes[0]
    print(f'O campeão foi {campeao}')

    if salvar:
            resultado = {
                'modalidade': 'mata-mata',
                'campeão': campeao,
                'rodadas': historico
            }
            arquivos.salvar_chaveamento(resultado)

    return campeao
    
def gerar_fase_de_grupos(equipes):
    quantidade_equipes = len(equipes)

    while True:
        try:
            num_grupos = int(input(f'Quantos grupos você quer formar? Você tem {quantidade_equipes} equipes '))
            if num_grupos < 2:
                print('é necessário ter ao menos 2 grupos')
            elif num_grupos > quantidade_equipes // 2:
                print(f'Com {quantidade_equipes} equipes, o máximo de grupos é {quantidade_equipes // 2}')
            else:
                break
        except ValueError:
            print('Digite um número inteiro.')

    equipes_embaralhadas = equipes[:]
    random.shuffle(equipes_embaralhadas)

    grupos = []
    for i in range(num_grupos):
        grupo = equipes_embaralhadas[i::num_grupos]
        grupos.append(grupo)

    historico_grupos = []
    classificados = []

    for idx, grupo in enumerate(grupos):
        letra = chr(65 + idx)
        print(f'Grupo {letra}: {grupo}')

        tabela = {equipe: {'pontos': 0, 'jogos': 0, 'vitorias': 0, 'empates': 0, 'derrotas': 0}
                  for equipe in grupo}
        jogos_grupo = []

        for i in range(len(grupo)):
            for j in range(i + 1, len(grupo)):
                equipe_a = grupo[i]
                equipe_b = grupo[j]
                print(f'{equipe_a} VS {equipe_b}')
                print(f'1 para {equipe_a}. 2 para {equipe_b}. 3 empate')

                while True:
                    opcao = input('Resultado: ').strip()
                    if opcao in ('1', '2', '3'):
                        break
                    else:
                        print('Opção invalida, digite 1, 2 ou 3')

                tabela[equipe_a]['jogos'] += 1  # ← correção 2
                tabela[equipe_b]['jogos'] += 1  # ← correção 2

                if opcao == '1':
                    tabela[equipe_a]['pontos'] += 3
                    tabela[equipe_a]['vitorias'] += 1
                    tabela[equipe_b]['derrotas'] += 1
                    resultado = equipe_a
                elif opcao == '2':
                    tabela[equipe_b]['pontos'] += 3
                    tabela[equipe_b]['vitorias'] += 1
                    tabela[equipe_a]['derrotas'] += 1
                    resultado = equipe_b
                else:
                    tabela[equipe_a]['pontos'] += 1
                    tabela[equipe_b]['pontos'] += 1
                    tabela[equipe_a]['empates'] += 1
                    tabela[equipe_b]['empates'] += 1
                    resultado = 'empate'

                jogos_grupo.append({'equipe_a': equipe_a, 'equipe_b': equipe_b, 'resultado': resultado})

        classificacao_grupo = sorted(tabela.items(), key=lambda x: x[1]['pontos'], reverse=True)

        print(f" {'Pos':<4} {'Equipe':<20} {'Pts':<5} {'V':<4} {'E':<4} {'D':<4}")
        for pos, (equipe, stats) in enumerate(classificacao_grupo, start=1):
            marca = " ✓" if pos <= 2 else ""
            print(f"  {pos:<4} {equipe:<20} {stats['pontos']:<5} {stats['vitorias']:<4} "
                  f"{stats['empates']:<4} {stats['derrotas']:<4}{marca}")

        avancos = min(2, len(classificacao_grupo))
        classificados_grupo = [classificacao_grupo[i][0] for i in range(avancos)]
        classificados.extend(classificados_grupo)

        historico_grupos.append({
            'grupo': letra,
            'equipes': grupo,
            'tabela': tabela,
            'jogos': jogos_grupo,
            'classificados': classificados_grupo
        })

    campeao = gerar_mata_mata(classificados, salvar=False)

    resultado = {
        'modalidade': 'fase-de-grupos',
        'campeao': campeao,
        'grupos': historico_grupos
    }
    arquivos.salvar_chaveamento(resultado)

    return campeao


if __name__ == '__main__':
    # só pra testar se precisar
    print('Escolha um modo para testar:')
    print('[1] Mata-mata')
    print('[2] Pontos corridos')
    print('[3] Fase de grupos')
    modo = input("Modo: ").strip()
 
    equipes = receber_equipes()
 
    if modo == '1':
        gerar_mata_mata(equipes)
    elif modo == '2':
        gerar_pontos_corridos(equipes)
    else:
        gerar_fase_de_grupos(equipes)
