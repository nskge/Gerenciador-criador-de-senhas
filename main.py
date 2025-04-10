import secrets
import string
import json
import hashlib
from pymongo import MongoClient


arquivo = "senhas.json"
mongourl = "INSIRA O LINK DO SEU DB"
client = MongoClient(mongourl)
db = client["senhas"]
collection = db["senhas_geradas"]
def carregar_senhas():
    try:
        with open(arquivo, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def gerar_senha(tamanho=16, com_pontuacao=False):
    caracteres = string.ascii_letters + string.digits
    if com_pontuacao:
        caracteres += string.punctuation
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho))


def guardar_senha(senha_segura, descsenha, senhahash, lista_senhas):
    lista_senhas.append({"senha": senha_segura, "descricao": descsenha, "hash": senhahash})
    with open(arquivo, "w") as f:
        json.dump(lista_senhas, f, indent=4)
    collection.insert_one({"Senha": senha_segura, "descrição": descsenha, "hash": senhahash})


def imprime_senhas(lista_senhas):
    senhas_str = "Senhas salvas: \n" + 20 * "-"
    for senha in lista_senhas:
        print(senha)

def MostrarSenhaJson():
            try:
                with open(arquivo, "r") as f:
                    senhas_carregadas = json.load(f)
                    
                print(json.dumps(senhas_carregadas, indent=4))
                
            except (FileNotFoundError, json.JSONDecodeError):
                print("Nenhuma senha foi salva ainda.")
    


def gerar_e_guardar_senha(lista_senhas, com_pontuacao=False):
    try:
        tamanho_senha = int(input("Digite o tamanho da senha (máximo 16): "))
        if tamanho_senha > 16:
            print("O tamanho máximo permitido é 16.")
            return
        descSenha = input("Caso deseje, adicione uma descrição para a senha:  ")
        senha_segura = gerar_senha(tamanho_senha, com_pontuacao)
        senhaencod = senha_segura.encode('utf-8')
        hashobj = hashlib.sha256(senhaencod)
        senhahash = hashobj.hexdigest()
        
        while True:
            print(f"Sua senha segura: {senha_segura}  Descrição: {descSenha} Hash: {senhahash}")
            print("Deseja guardar a senha? y/n")
            escGuardar = input()
            if escGuardar == "y":
                guardar_senha(senha_segura, descSenha, senhahash, lista_senhas)               
                break
            elif escGuardar == "n":
                break
            else:
                print("Valor digitado não serve como resposta.")
    except ValueError:
        print("Valor digitado não é um número inteiro.")


def menu():
    lista_senhas = carregar_senhas()

    while True:
        print("Bem-vindo(a) ao gerenciador de senhas. O que deseja fazer?\n" + 50 * "-")
        print("1. Gerar senha segura")
        print("2. Gerar senha segura com pontuação")
        print("3. Listar senhas salvas")
        print("4. Mostrar senhas no JSON")
        print("5. Remover senha/BD e Json(em construção)")
        print("6. Sair do programa.")
        
        escolha = input()

        if escolha == "1":
            gerar_e_guardar_senha(lista_senhas)
            input("Pressione Enter para voltar ao menu inicial!")
        elif escolha == "2":
            gerar_e_guardar_senha(lista_senhas, com_pontuacao=True)
            input("Pressione Enter para voltar ao menu inicial!")
        elif escolha == "3":
            imprime_senhas(lista_senhas)
            input("Pressione Enter para voltar ao menu inicial!")
        elif escolha == "4":
                MostrarSenhaJson()
                input("Pressione Enter para voltar ao menu inicial!")
        elif escolha == "6":
            print("Saindo do gerenciador..")
            break
        
        else:
            print("Valor digitado não serve como resposta ou esta em construção.")

if __name__ == "__main__":
    menu()
