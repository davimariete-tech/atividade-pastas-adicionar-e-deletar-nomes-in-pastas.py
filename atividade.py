import os
import time
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}\nE-mail: {self.email}\nTelefone: {self.telefone}")

def verificar_lista_vazia(lista_clientes):
    if not lista_clientes:
        print("\nNão há clientes cadastrados.")
        return True
    return False

def adicionar_cliente(lista_clientes):
    print("\n--Adicionar novo cliente--")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")

    novo_cliente = Cliente(nome=nome, email=email, telefone=telefone)
    lista_clientes.append(novo_cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

def encontrar_cliente_por_nome(lista_clientes, nome_buscar):
    nome_buscar_lower = nome_buscar.lower()
    for cliente in lista_clientes:
        if cliente.nome.lower() == nome_buscar_lower:
            return cliente
    return None

def mostrar_todos_clientes(lista_clientes):
    if verificar_lista_vazia(lista_clientes):
        return

    print("\n--Lista de clientes--")
    for cliente in lista_clientes:
        cliente.mostrar_dados()

def atualizar_cliente(lista_clientes):
    print("\n--- Atualizar dados do cliente ---")

    if verificar_lista_vazia(lista_clientes):
        return

    nome_buscar = input("\nDigite o nome do cliente que deseja atualizar: ")
    cliente_para_atualizar = encontrar_cliente_por_nome(lista_clientes, nome_buscar)

    if cliente_para_atualizar:
        print("\nCliente encontrado!")

        print("\nDigite os novos dados ou deixe em branco para manter o valor atual.")

        print(f"Nome atual: {cliente_para_atualizar.nome}")
        novo_nome = input("Novo nome: ")

        print(f"E-mail atual: {cliente_para_atualizar.email}")
        novo_email = input("Novo e-mail: ")

        print(f"Telefone atual: {cliente_para_atualizar.telefone}")
        novo_telefone = input("Novo telefone: ")

        if novo_nome:
            cliente_para_atualizar.nome = novo_nome
        if novo_email:
            cliente_para_atualizar.email = novo_email
        if novo_telefone:
            cliente_para_atualizar.telefone = novo_telefone

        print("\nDados atualizados com sucesso!")
    else:
        print(f"\nCliente com nome '{nome_buscar}' não encontrado.")

def menu():
    lista_clientes = []

    while True:
        os.system("cls")  
        print("1. Adicionar Cliente")
        print("2. Mostrar Todos os Clientes")
        print("3. Encontrar Cliente")
        print("4. Atualizar Cliente")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            adicionar_cliente(lista_clientes)
            time.sleep(2)

        elif opcao == '2':
            mostrar_todos_clientes(lista_clientes)
            input("\nPressione Enter para continuar...")

        elif opcao == '3':
            nome_buscar = input("Digite o nome do cliente: ")
            cliente = encontrar_cliente_por_nome(lista_clientes, nome_buscar)
            if cliente:
                cliente.mostrar_dados()
            else:
                print("\nCliente não encontrado.")
            input("\nPressione Enter para continuar...")

        elif opcao == '4':
            atualizar_cliente(lista_clientes)
            input("\nPressione Enter para continuar...")

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida!")
            time.sleep(1)

menu()
