#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Criar um programa que leia um número pelo teclado e mostre
# a sua tabuada

n = int(input('Número para cálculo de tabuada: '))
c = m = 1
while c <= 10:
    m = n * c
    print('{} X {} = {}'.format(n,c,m))
    c+=1