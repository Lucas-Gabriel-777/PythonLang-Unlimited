#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo: Criar um programa que leia algo pelo teclado e mostre informações sobre o texto
tema = input('Digite qualquer coisa: ')
print('O texto digitado foi {} e sua classe primitiva é {}.'.format(tema, type(tema)))
print('É alfa-numérico:', tema.isalnum())
print('É alfabético:', tema.isalpha())
print('Está em minúsculo:',tema.islower())
print('Está em maiúsculo:',tema.isupper())
print('É composto por espaços:',tema.isspace())
print('É decimal:',tema.isdecimal())