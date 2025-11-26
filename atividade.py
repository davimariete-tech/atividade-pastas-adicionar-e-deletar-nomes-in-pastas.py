import os
os.system("cls")

from dataclasses import dataclass

@dataclass 
class Funcionario:
    nome: str
    data_de_adm: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_de_nascimento: str
    endereco: str


# Listas separadas
lista_funcionarios = []
lista_clientes = []

QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

# Cadastro de funcionários
for i in range(QUANTIDADE_FUNCIONARIOS):
    print(f"\n--- FUNCIONÁRIO {i+1} ---")
    funcionario = Funcionario(
        nome=input("Informe o nome: "),
        data_de_adm=input("Informe data de admissão: "),
        matricula=input("Informe o número de matrícula: "),
        endereco=input("Informe o endereço: ")
    )
    lista_funcionarios.append(funcionario)

print()

# Cadastro de clientes
for i in range(QUANTIDADE_CLIENTES):
    print(f"\n--- CLIENTE {i+1} ---")
    cliente = Cliente(
        nome=input("Informe o nome: "),
        data_de_nascimento=input("Informe a data de nascimento: "),
        endereco=input("Informe o endereço: ")
    )
    lista_clientes.append(cliente)

print()

# Salvando em arquivo CSV
arquivo_nome = "dados_funcionario.csv"

with open(arquivo_nome, "a", encoding="utf-8") as arquivo:
    arquivo.write("FUNCIONARIOS:\n")
    for f in lista_funcionarios:
        arquivo.write(f"{f.nome},{f.data_de_adm},{f.matricula},{f.endereco}\n")

    arquivo.write("\nCLIENTES:\n")
    for c in lista_clientes:
        arquivo.write(f"{c.nome},{c.data_de_nascimento},{c.endereco}\n")

print("\nDados salvos com sucesso!")

# ==================================================
#      LENDO O ARQUIVO E EXIBINDO OS REGISTROS
# ==================================================

lista_todos_funcionarios = []

try:
    with open(arquivo_nome, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

        print("\n--- LENDO DADOS DO ARQUIVO ---")

        for linha in linhas:
            linha = linha.strip()

            # Ignora títulos
            if linha == "FUNCIONARIOS:" or linha == "" or linha == "CLIENTES:":
                continue

            # Divide os dados
            dados = linha.split(",")

            # Detecta automaticamente se é funcionário ou cliente pelo número de campos
            if len(dados) == 4:  # Funcionário
                nome, data_adm, matricula, endereco = dados
                lista_todos_funcionarios.append(
                    Funcionario(nome, data_adm, matricula, endereco)
                )

            elif len(dados) == 3:  # Cliente
                nome, data_nasc, endereco = dados
                lista_todos_funcionarios.append(
                    Cliente(nome, data_nasc, endereco)
                )

    # Exibe tudo lido
    print("\n--- DADOS CARREGADOS DO ARQUIVO ---")
    for item in lista_todos_funcionarios:
        print(item)

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")
