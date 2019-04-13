#!/bin/python
b = {'João': 10, 'Márcio': 8, 'Paulo': 5, 'Douglas': 6}
j = 'Douglas' #Nome do aluno

if b[j] >= 8:
    print("Aluno " + j + " aprovado!")
elif b[j] >= 6:
    print("Aluno " + j + " recuperação!")
else:
    print("Aluno " + j + " reprovado!")
