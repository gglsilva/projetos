# -*- coding: utf-8 -*-
from lib.interface import *
from lib.functions import *
from time import sleep


while True:
    resp = menu(['Dividir Boletos','Dividir PDF','Sair'])
    if resp == 1:
        path = str(input('Digite o path do arquivo:'))
        divide_pdf(path)
    elif resp == 2:
        path = str(input('Digite o path do arquivo:'))
        divide_pdf(path, nm = False)
    elif resp == 3:
        print('Saindo...')
        sleep(2)
        exit()
    else:
        print('Opção inválida')
        sleep(2)