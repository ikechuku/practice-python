theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

fullBoard = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R',
'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R',
'low-L': 'low-L', 'low-M': 'low-R', 'low-R': 'low-R'}


def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


def instruc(board):
	print('HOW TO PLAY THE GAME \n' )
	print('____________________ \n')
	print('iput the position you wish to play your turn as shown below \n' )
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-----+-----+-----')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-----+-----+-----')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'] + '\n')
	print('player X will play first \n')



instruc(fullBoard)



turn = 'X'
for i in range(9):	
	printBoard(theBoard)
	print('Turn for ' + turn + '. Move on which space?')
	move = input()
	if theBoard[move] == ' ':
		theBoard[move] = turn

		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
	else:
		print("you can't play there!, try Again")
	
printBoard(theboard)



