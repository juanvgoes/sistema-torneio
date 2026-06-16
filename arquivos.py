import json
import os

def salvar_chaveamento(dados):
    if not os.path.exists("historico"):
        os.mkdir("historico")

    nome_arquivo = input("Digite um nome para salvar o arquivo: ")
    caminho = f"historico/{nome_arquivo}.json"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Chaveamento salvo com sucesso!")


def listar_salvos():
    if not os.path.exists("historico"):
        print("Nenhum histórico encontrado.")
        return []

    arquivos = os.listdir("historico")

    if len(arquivos) == 0:
        print("Nenhum histórico salvo.")
    else:
        print("\nArquivos salvos:")
        for arquivo in arquivos:
            print("-", arquivo)

    return arquivos


def carregar_chaveamento(nome_arquivo):
    caminho = f"historico/{nome_arquivo}"

    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        print("Arquivo carregado com sucesso!")
        return dados

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
