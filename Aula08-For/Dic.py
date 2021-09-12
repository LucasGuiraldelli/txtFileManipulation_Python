# Dicts or Dictionary

lista1 = [1, 2, 3, 4]         # Todos os elementos de uma lista são manipulados através de índices numéricos

# Key -> Valor

dict1 = {'Key1': 2, 'num': 23}              # Estrutura formada por chave e valor     # Exemplo = 'Chave1': 100
dict2 = dict()


dict1['Chave1'] = lista1                   # Adiciona a 'Chave1' e os valoresda lista1 para o dict1


# Exercicio Exemplo

# Baseado em uma lista de 150 valores inteiros
# Criar um algoritmo que retorne cada um dos números existentes na lista
# e a quantidade de vezes que ele aparece nela
# { numero : qtde_numeros }

import random as rand

list_numbers = []
for number in range(0, 1500):
    list_numbers.append(rand.randint(3, 45678))

numbers_quantity = {}
for number in list_numbers:
    if number in numbers_quantity:
        numbers_quantity[number] += 1
    else:
        numbers_quantity[number] = 1
print(numbers_quantity)


# Files (Open/Read or Write/Close)      ->   manipulação de arquivos de texto

# prestar atenção no segundo parâmetro "w", dita o formato de abertura do arquivo

filew = open("wfile.log", "w", encoding="utf-8")                  # cria arquivo (caso não exista)
filer = open("wfile.log", "r", encoding="utf-8")

status = False
for line in filer.readlines():                                   # Lê e compara as linhas do arquivo
    if line.find("Escrita") != -1:
        status = True

list_elements = [23, 23, 23, 24]

if not status:
    filew.write("\n".join([str(item) for item in list_elements]))       # converte os itens da lista em str para ser lida no processo join()

filew.close()
filer.close()

