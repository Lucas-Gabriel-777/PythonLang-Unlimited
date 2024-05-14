#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo:Criar um programa que leia um número e mostre o dobro, o triplo e a raiz
# quadrada desse número

num = int(input('Me dê um número: '))
d = num * 2
t = num * 3
rq = num ** (1/2)
print('O dobro de {} é {}'.format(num,d))
print('O triplo é {}'.format(t))
print('E a raiz quadrada é {}'.format(rq))