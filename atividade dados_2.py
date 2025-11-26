import os
os.system("cls")  # no Linux troque para "clear"


lista_clientes = []

print("Create - Adicionar/Inserir")
nome = "Marta"
lista_clientes.append(nome)
print(f"O nome '{nome}' foi inserido com sucesso.\n")

print("Read - Ler/Mostrar")
print(lista_clientes, "\n")

print("Update - Atualizar/Alterar")
nome_para_atualizar = "Marta"

if nome_para_atualizar in lista_clientes:
    nome_novo = "Marta Silva"
    indice = lista_clientes.index(nome_para_atualizar)
    lista_clientes[indice] = nome_novo
    print(f"O nome '{nome_para_atualizar}' foi atualizado para '{nome_novo}'.")
else:
    print(f"O nome '{nome_para_atualizar}' não foi encontrado.")

print(lista_clientes, "\n")

print("Delete - Excluir/Remover")
nome_para_excluir = "Marta Silva"



while True:
    print("""
         




          
          
          
          """)