import os

def cria_board():
	board = [['','',''],['','',''],['','','']]
	print('\nTaboleiro:')
	return board


def imprimi_board(board):
	c = ['A', 'B', 'C']
	cont = 0
	print(' '*3, end='')
	for i in c:
		print(f'{i:^7}', end='')
	print()
	for j in board:
		print(f'{cont:^3}', end='')
		cont+=1
		for l in j:
			print(f'|{l:^5}|', end='')
		print()


def marca_jogada(board, player):
	board = board
	player = player
	l = int(input('Linha: '))
	c = int(input('Coluna: '))
	vj = verifica_jogada_valida(board, l, c)
	if vj == True:
		board[l][c] = player
		imprimi_board(board)
		os.system('clear')
		print('Ultima jogada:\n')
		imprimi_board(board)

	else:
		print('jogada invalida, tente novamente...')
		marca_jogada(board, player)


def verifica_jogada_valida(board ,l, c):
	valida = True
	if board[l][c] != '':
		valida = False
	return valida
		


def verifica_ganhador(board, pl1, pl2):
	vencedor = False
	if board.count('') == 9:
		print('Que o Jogo comece...')
	else:
		#### PL1
		if (board[0].count(pl1) == 3) or (board[1].count(pl1) == 3) or (board[2].count(pl1) == 3):
			print('Jogador 1 ganhou')
			vencedor = True
		elif (board[0][0] == pl1) and (board[1][0] == pl1) and (board[2][0]== pl1):
			print('Jogador 1 ganhou')
			vencedor = True
		elif (board[0][1] == pl1) and (board[1][1] == pl1) and (board[2][1]== pl1):
			print('Jogador 1 ganhou')
			vencedor = True
		elif (board[0][2] == pl1) and (board[1][2] == pl1) and (board[2][2]== pl1):
			print('Jogador 1 ganhou')
			vencedor = True
		elif (board[0][0] == pl1) and (board[1][1] == pl1) and (board[2][2] == pl1):
			print('Jogador 1 ganhou')
			vencedor = True
		elif (board[0][2] == pl1) and (board[1][1] == pl1) and (board[2][0] == pl1):
			print('Jogador 1 ganhou')
			vencedor = True	
		#### PL2
		elif board[0].count(pl2) == 3 or board[1].count(pl2) == 3 or board[2].count(pl2) == 3:
			print('Jogador 2 ganhou')
			vencedor = True
		elif (board[0][0] == pl2) and (board[1][0] == pl2) and (board[2][0]== pl2):
			print('Jogador 2 ganhou')
			vencedor = True
		elif (board[0][1] == pl2) and (board[1][1] == pl2) and (board[2][1]== pl2):
			print('Jogador 2 ganhou')
			vencedor = True
		elif (board[0][2] == pl2) and (board[1][2] == pl2) and (board[2][2]== pl2):
			print('Jogador 2 ganhou')
			vencedor = True
		elif (board[0][0] == pl2) and (board[1][1] == pl2) and (board[2][2] == pl2):
			print('Jogador 2 ganhou')
			vencedor = True
		elif (board[0][2] == pl2) and (board[1][1] == pl2) and (board[2][0] == pl2):
			print('Jogador 2 ganhou')
			vencedor = True
	return vencedor