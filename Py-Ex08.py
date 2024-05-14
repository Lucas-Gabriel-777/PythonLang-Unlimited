#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Criar um programa que leia uma medida em metros e a converta
# para centímetros e milímetros

m = float(input('Medida em metros a ser convertida: '))
c = m * 100
mi = m * 1000

print('{} Metros equivalem a {} centímetros e {} milímetros'.format(m,c,mi))