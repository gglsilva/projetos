# -*- coding: utf-8 -*-
import os
from time import sleep
from lib.interface import *
from PyPDF2 import PdfFileWriter, PdfFileReader


def lista_arquivos(path):
    for arquivo in os.listdir(path):
        if arquivo.endswith('.pdf'):
            print(arquivo)
    

def abri_arquivo(path, arq):
    os.chdir(path)
    try:
        pdfFileObj = open(arq + '.pdf','rb')
        reader = PdfFileReader(pdfFileObj)
    except FileNotFoundError:
        print('Arquivo não encontrado')
        exit()
    except PermissionError:
        print('Permissão negada')
        exit()
    return reader, pdfFileObj


def nomear_arquivo(pdf, nm=True):
    print('')
    list_nomes = []
    if nm:
        for item in range(pdf.numPages):
            spg = pdf.getPage(item).extractText()
            spg[:1000]
            pg = spg.split('\n')
            nome = pg[2]
            numero = pg [10]
            concat = numero + ' - ' + nome
            print(concat)
            list_nomes.append(concat)
    else:
        for item in range(pdf.numPages):
            list_nomes.append('Page'+str(item))
    print(list_nomes)    
    return list_nomes


def salvando_arquivos(pdf, nomes):
    for item in range(pdf.numPages):
        output = PdfFileWriter()
        output.addPage(pdf.getPage(item))
        with open(nomes[item] + '.pdf', "wb") as outputStream:
            output.write(outputStream)         
    sleep(0.5)
    print('Concluido')


def divide_pdf(path, nm=True):
    print(linha())
    lista_arquivos(path)
    print(linha())
    arq = str(input('selecione um Arquivo: '))
    path_split = str(input('Digite o path para salvar os arquivos: '))
    print(linha())
    pdf = abri_arquivo(path, arq)
    if os.path.isdir(path_split):
        print('já existe uma pasta com esse nome!')
        print(linha())
    else:
        os.mkdir(path_split)
        os.chdir(path_split)
        print('Pasta criada com sucesso!')
        print('Divindo PDF dos boletos...')
        print(linha())
        sleep(2)
        nomes = nomear_arquivo(pdf[0], nm)
        salvando_arquivos(pdf[0], nomes)
    arquivo = pdf[1]
    arquivo.close()
    print('Arquivo fechado com sucesso!')
    sleep(1)
    