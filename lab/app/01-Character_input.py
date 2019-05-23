#!/bin/python3
nome = input("Insira seu nome: ")
print("Seu nome é " + nome)

idade = int(input("Insira sua idade: "))

n = int(input("Quantidade de vezes que o resultado será printado em tela: "))

nidade = int((100 - idade) + 2019)

print( n * "Você completerá 100 anos em {}\n" .format(nidade))
