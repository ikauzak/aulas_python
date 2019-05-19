#!/bin/python
def primo(num):
    for n in range(2,num):
        if num % n == 0:
            print(num, 'não é primo')
            break
        else:
            print(num, 'é primo')
            break

primo(4)
primo(5)
primo(18)
primo(223)

#Neste código estou verificando se os números que estão inseridos na função são números primos ou não.
#A análise é feita em condição if, caso o número seja divisível por 2 ou algum número até "num", ele não é um número primo.
