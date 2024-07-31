import csv
import os
from time import sleep

class Usuario:
    def __init__(self, nome, idade=None, email=None, telefone=None):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

class GerenciadorUsuarios:
    def __init__(self):
        self.arquivo = os.path.join(os.path.dirname(__file__), 'usuarios.csv')
        if not os.path.exists(self.arquivo):
            with open(self.arquivo, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['nome', 'idade', 'email', 'telefone'])

    def adicionar_usuario(self, nome, idade, email, telefone):
        usuario = Usuario(nome, idade, email, telefone)
        with open(self.arquivo, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([usuario.nome, usuario.idade, usuario.email, usuario.telefone])
        print("😎USUÁRIO ADICIONADO COM SUCESSO!")

    def listar_usuarios(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r', newline='') as f:
                reader = csv.DictReader(f)
                print("=" * 100)
                print("LISTA DE USUÁRIOS:")
                print("-" * 100)
                for row in reader:
                    print("*" * 100)
                    print(f"NOME: {row['nome']}, IDADE: {row['idade']}, EMAIL: {row['email']}, TELEFONE: {row['telefone']}")
                    print("*" * 100)
                print("=" * 100)
        else:
            print("😒NENHUM USUÁRIO CADASTRADO.")

    def atualizar_usuario(self, nome_antigo, novo_nome, nova_idade, novo_email, novo_telefone):
        usuarios = []
        with open(self.arquivo, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['nome'] == nome_antigo:
                    row['nome'] = novo_nome if novo_nome else row['nome']
                    row['idade'] = nova_idade if nova_idade else row['idade']
                    row['email'] = novo_email if novo_email else row['email']
                    row['telefone'] = novo_telefone if novo_telefone else row['telefone']
                usuarios.append(row)

        with open(self.arquivo, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['nome', 'idade', 'email', 'telefone'])
            writer.writeheader()
            writer.writerows(usuarios)
        print("😙USUÁRIO ATUALIZADO COM SUCESSO!")

    def excluir_usuario(self, nome):
        usuarios = []
        with open(self.arquivo, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['nome'] != nome:
                    usuarios.append(row)

        with open(self.arquivo, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['nome', 'idade', 'email', 'telefone'])
            writer.writeheader()
            writer.writerows(usuarios)
        print("🗑USUÁRIO EXCLUÍDO COM SUCESSO!")

def exibir_menu():
    print("\nMENU:")
    print("1. ADICIONAR USUÁRIO")
    print("2. LISTAR USUÁRIOS")
    print("3. ATUALIZAR USUÁRIO")
    print("4. EXCLUIR USUÁRIO")
    print("5. SAIR")

def main():
    gerenciador = GerenciadorUsuarios()

    while True:
        exibir_menu()
        opcao = input("😎ESCOLHA UMA OPÇÃO:\n>>> ")

        if opcao == "1":
            nome = input("😎DIGITE O NOME:\n>>> ")
            idade = input("😎DIGITE A IDADE (pressione Enter para deixar em branco):\n>>> ")
            email = input("😎DIGITE O EMAIL (pressione Enter para deixar em branco):\n>>> ")
            telefone = input("😎DIGITE O TELEFONE (pressione Enter para deixar em branco):\n>>> ")
            gerenciador.adicionar_usuario(nome, idade, email, telefone)
        elif opcao == "2":
            gerenciador.listar_usuarios()
        elif opcao == "3":
            nome_antigo = input("😎DIGITE O NOME A SER ATUALIZADO:\n>>> ")
            novo_nome = input("😎DIGITE O NOVO NOME (pressione Enter para deixar em branco):\n>>> ")
            nova_idade = input("😎DIGITE A NOVA IDADE (pressione Enter para deixar em branco):\n>>> ")
            novo_email = input("😎DIGITE O NOVO EMAIL (pressione Enter para deixar em branco):\n>>> ")
            novo_telefone = input("😎DIGITE O NOVO TELEFONE (pressione Enter para deixar em branco):\n>>> ")
            gerenciador.atualizar_usuario(nome_antigo, novo_nome, nova_idade, novo_email, novo_telefone)
        elif opcao == "4":
            nome = input("😎DIGITE O NOME DO USUÁRIO A SER EXCLUÍDO:\n>>> ")
            gerenciador.excluir_usuario(nome)
        elif opcao == "5":
            print("🚀SAINDO...")
            sleep(3)
            break
        else:
            print("😡OPÇÃO INVÁLIDA. TENTE NOVAMENTE!")

if __name__ == "__main__":
    main()
