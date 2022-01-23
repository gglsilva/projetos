# -*- coding: utf-8 -*-
from lib.functions import *
from lib.interface import *

while True:
    resp = menu(['Login', 'Cadastra-se', 'Sair'])
    if resp == 1:
        user = str(input('Usuário: '))
        senha = str(input('Senha: '))
        login(user, senha)
    elif resp == 2:
        user = str(input('Usuário: '))
        senha = str(input('Senha: '))
        cadastra(user, senha)
    elif resp == 3:
        break
