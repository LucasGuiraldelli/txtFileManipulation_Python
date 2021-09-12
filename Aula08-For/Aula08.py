# for letra in 'aeiou':
#     print(letra)


# exemplo 01
for index in range(1,101):         # for(int i = 0; i <= 101; i++)    // o uso em outras linguagens seria assim para incremento
    print(type(index))             # mostra o tipo da variável
    print(index)

# exemplo 02
for index in range(100,2,-1):     # o terceiro digito dita quantos números serão pulados, ou seja,
    print(type(index))            # a variavel index está trabalhando num alcance de 100 a 2 decrementando de 1 em 1 número
    print(index)


# exemplo 03

media_aritmetica = 78.5
media_ponderada = 80.5

notas_turma = [56.7, 87.9, 100.0, 45.7]

for nota in notas_turma:
    if nota <= media_aritmetica:
        print(nota)

# exemplo 04

palavra = input('Palavra: ')
troca = ''

for letra in palavra:
    if letra in "aeiou":
        troca += '*'
    else:
        troca += letra
    print("Nova palavra %s" %troca)


# exemplo 05

x = int(input('Digite um número: '))

def épar(x):
    return x % 2 == 0


# exemplo 06

def fatorial(n):
    resultado = 1
    if n == 0 and n == 1:
        return resultado
    else:
        for valor in range(2, n + 1):
            resultado *= valor
    return  resultado

for i in range(6):
    print(fatorial(i))