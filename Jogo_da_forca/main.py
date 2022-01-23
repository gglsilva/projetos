import jogodaforca as jf 


def main():
    print(f'Vamos começar, A dica é: {dica}')
    palavra_secreta = jf.escolhe_palavra()
    letras_certas = jf.inicia_acertos(palavra_secreta)
    enforcou = acertou = False
    erro = 0
    #print(f'A palavra é {palavra_secreta}')
    jf.imprimi_forca()
    while not enforcou and not acertou:
        chute = jf.pede_letra()
        #print('_'*20)
        if chute in palavra_secreta:
            jf.marcar_acerto(chute, letras_certas, palavra_secreta)
        else:
            erro += 1
            print(f'Quantidade de erros: {erro}')
        #jf.imprimi_digitadas(letras_digitadas)
        jf.imprimi_acertos(letras_certas)

        if letras_certas == palavra_secreta:
            print('\nVocê acertou, Parabéns!')
            acertou = True
        elif erro == 6:
            print('\nEnforcou, você perdeu!')
            enforcou = True
        print('\n','_'*30)
        

if __name__ == '__main__':
    print('='*40)
    print('{:^40}'.format('Bem vindo ao jogo da Forca!'))
    print('='*40)
    main()