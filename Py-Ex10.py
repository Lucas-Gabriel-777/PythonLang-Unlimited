#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar

#dr = Dinheiro em Reais
#dd = Dineiro em Dólar

dr = float(input('Quanto você tem em dinheiro para converter? '))
#Preço do dólar em 13-05-2024: 5,16

dd = (dr // 5.16)
print('Com {} Reais você pode comprar {} Dólar(es)'.format(dr,dd))