import jogodavelha as jv

def main():
	ganhador = False
	novo_jogo = jv.cria_board()
	jv.imprimi_board(novo_jogo)
	print('\nJogador 1:')
	pl1 = str(input('Escolha [X ou O] para jogar: ')).strip().upper()[0]
	print('_'*30)
	pl2 = ''
	if pl1 == 'X':
		pl2 = 'O'
	else:
		pl2 = 'X'
	print(f'Jogador 1: |{pl1}|\njogador 2: |{pl2}|')
	print('_'*30)
	vez = 0
	while ganhador != True:
		ganhador = jv.verifica_ganhador(novo_jogo, pl1, pl2)
		#os.system('clear')
		if (ganhador == False) and (vez == 0):
			print('Jogador 1:')
			jv.marca_jogada(novo_jogo, pl1)
			vez += 1
		elif (ganhador == False) and (vez == 1):
			print('Jogador 2:')
			jv.marca_jogada(novo_jogo, pl2)
			vez -= 1
		print('=-'*20)
		print()
	print('Volte sempre!')


if __name__ == '__main__':
    print('='*40)
    print('{:^40}'.format('Bem vindo ao jogo da Velha!'))
    print('='*40)
    main()
