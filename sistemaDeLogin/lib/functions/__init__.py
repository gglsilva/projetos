# -*- coding: utf-8 -*-

def login(user, senha):
    with open('register.txt', 'r') as arquivo:
        for linha in arquivo:
            dados = linha.split(', ')
            if dados[1] == user and dados[2] == senha:
                print('\033[32mLogin efetuado com sucesso!\033[m')
                break
            else:
                print('Usuário ou senha incorretos!')
                break
    

def cadastra(user, senha):
    with open('register.txt', 'r+') as arquivo:
        n_linhas = len(arquivo.readlines())
        if n_linhas == 0:
            arquivo.write(str(n_linhas + 1) + ', ' + user + ', ' + senha)  
        else:
            n_linhas += 1
            arquivo.write(str(n_linhas) + ', ' + user + ', ' + senha)
    print('Cadastro efetuado com sucesso!')   
