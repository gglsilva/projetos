import string
import argparse
import random

from click import parser

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATIONS = string.punctuation

def gerador_senhas(letras=8, numeros=4, pontuacao=2):
    # Declaração de impressão simples para o terminal.
    """
	Gerar senhas de acordo com as quantidades de letra, números e
    pontuaçãoes desejadas.
	"""
    valor = ''
    valor += selecionando_caracter(letras, LETTERS)
    valor += selecionando_caracter(numeros, NUMBERS)
    valor += selecionando_caracter(pontuacao, PUNCTUATIONS)
    return embaralhar(valor)   # transforma a lista novamente em uma string


def selecionando_caracter(tamanho, caracter):
    valor = ''
    for item in range(tamanho):
        valor += random.choice(caracter)
    return valor


def embaralhar(texto):
    texto = list(texto)
    random.shuffle(texto)
    return ''.join(texto)


def salva_em_arquivo(servico, usuario, senha):
    arquivo = open('senhas.txt', 'a')
    arquivo.write("Identificador: {}\n".format(servico))
    arquivo.write("Usuario: {}\n".format(usuario))
    arquivo.write("Senha: {}\n".format(senha))
    arquivo.write("-=-"*20)
    arquivo.write("\n")
    arquivo.close()
    print('senha salva')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Gerador de senhas aleatorias')
    parser.add_argument('--letras', type=int, default=8, help='Quantidade de letras')
    parser.add_argument('--numeros', type=int, default=4, help='Quantidade de numeros')
    parser.add_argument('--pontuacao', type=int, default=2, help='Quantidade de caracteres especiais')
    args = parser.parse_args()
    print(gerador_senhas(letras=args.letras, numeros=args.numeros, pontuacao=args.pontuacao))
