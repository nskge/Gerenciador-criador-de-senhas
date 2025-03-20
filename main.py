import secrets
import string
import os
import json


 
arquivo = "senhas.json"
try:
    with open(arquivo, "r") as f:
        listaSenhas = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    listaSenhas = []
def gerar_senha(tamanho=16):
    os.system('cls||clear')
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha
def gerar_senhapont(tamanho=16):
    os.system('cls||clear')
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def guardarSenha(senha_segura, descsenha):                   
        listaSenhas.append({"senha": senha_segura, "descricao": descsenha})
        with open(arquivo, "w") as f:
            json.dump(listaSenhas, f, indent=4)               
def imprimeSenha():
    os.system('cls||clear')
    print("senhas salvas: \n"+ 20*"-")
    i = 0
    while (i< len(listaSenhas)):
            print(listaSenhas[i])
            i += 1


a = True

while(a):
    
    os.system('cls||clear')
    print("Bem vindo(a) o gerenciador de senhas do San, o que deseja?\n" + 50*"-")
    print("1. Gerar senha segura")
    print("2. Gerar senha segura com pontuação")
    print("3. Listar senhas salvas")
    print("4. Mostrar senhas em Json")

    print("5. Sair do programa.")



    escolha = input() 
    
    if (escolha == "1"):
        os.system('cls||clear')
        try:
                tamanho_senha = int(input("Digite o tamanho da senha(16max): "))
                descSenha = input("Caso deseje adicione uma descrição a senha:  ")
                senha_segura = gerar_senha(tamanho_senha)       
                while (True):
                    print(f"Sua senha segura:{senha_segura}  descrição: {descSenha}")
                    print("Deseja guardar a senha? y/n")
                    escGuardar = input()
                    if (escGuardar == "y"):
                        guardarSenha(senha_segura,descSenha)
                        break
                    elif(escGuardar == "n"):
                        break
                    else:
                        os.system('cls||clear')
                        print("valor digitado não serve como resposta.")
        except ValueError:            
            print("valor digitado nn é um numero inteiro")
            input()
            os.system('cls||clear')
                  
        
            
    elif (escolha == "2"):
        os.system('cls||clear')
        try:
                tamanho_senha = int(input("Digite o tamanho da senha(16max): "))
                descSenha = input("Caso deseje adicione uma descrição a senha:  ")
                senha_segura = gerar_senhapont(tamanho_senha)       
                while (True):
                    print(f"Sua senha segura:{senha_segura}  descrição: {descSenha}")
                    print("Deseja guardar a senha? y/n")
                    escGuardar = input()
                    if (escGuardar == "y"):
                        guardarSenha(senha_segura,descSenha)
                        break
                    elif(escGuardar == "n"):
                        break
                    else:
                        os.system('cls||clear')
                        print("valor digitado não serve como resposta.")
        except ValueError:            
            print("valor digitado nn é um numero inteiro")
            input()
            os.system('cls||clear')


    elif (escolha == "3"):              
        imprimeSenha()
        print(30*"-")
        input("pressione enter para voltar ao menu inicial!")
    elif (escolha == "4"):
        os.system('cls||clear')
        try:
            with open(arquivo, "r") as f:
                senhas_carregadas = json.load(f)
            print(json.dumps(senhas_carregadas, indent=4))
            input("pressione enter para voltar ao menu inicial!")
        except (FileNotFoundError, json.JSONDecodeError):
            print("Nenhuma senha foi salva ainda.")
            input("Pressione Enter para voltar ao menu inicial!")
        
    elif escolha == "5":
        a = False
        print("Saindo do gerenciador..")
        break
    elif escolha != int:
        print("valor digitado não serve como resposta.")
        os.system('cls||clear')
    else:        
        print("valor digitado não serve como resposta.")
        os.system('cls||clear')








