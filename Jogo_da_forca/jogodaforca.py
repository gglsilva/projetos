import os
import string
from random import choice


dica = 'Fruta'
LETTERS = string.ascii_letters
palavra_secreta = []
letras_certas = []
letras_digitadas = []


def escolhe_palavra():
    arq = open('palavras.txt')
    palavras = arq.readlines()
    palavra = list(choice(palavras).upper())
    palavra = palavra[:-1]
    arq.close()
    return palavra


def pede_letra():
    letra = ' '
    while letra not in LETTERS.upper(): 
        letra = str(input('\nDigite uma letra ')).strip().upper()[0]
        letras_digitadas.append(letra)
    return letra


def inicia_acertos(palavra_secreta):
    letras_certas = []
    for i in range(len(palavra_secreta)):
        letras_certas.append('_,')
    return letras_certas


def marcar_acerto(chute, letras_certas, palavra_secreta):
    posição = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_certas.pop(posição)
            letras_certas.insert(posição, chute)
        posição += 1


def imprimi_acertos(letras_certas):
    print('Palavra: ', end='')
    for i in letras_certas:
        print(i, end='')


def imprimi_forca():
    print('  ____')
    print(' /   |')
    print('|    o')
    print('|   /|\\')
    print('|   / \\')
    print('|_____')


def imprimi_digitadas(letras_digitadas):
    print('Letras Digitadas: ', end='')
    for i in letras_digitadas:
        print(i, end=', ')
    print('\n')
