QUEENS = 10

# print the board 
def print_board(board):
	print("This is my board!")
	for col in board:		
		print(col)

# return if queen2 hits queen1
# input tuple(x,y)
def is_hit(queen1,queen2):
	
	if(queen1[1]==queen2[1]):
		# print("ERROR2")
		return True
	
	# check diagonal if y1-x1 == y2-x2 then its a hit
	diff1 = queen1[1]-queen1[0]
	diff2 = queen2[1]-queen2[0]
	if(diff1==diff2):
		# print("ERROR3",diff1,diff2)
		return True

	diff1 = queen1[1]+queen1[0]
	diff2 = queen2[1]+queen2[0]
	if(diff1==diff2):
		# print("ERROR4",diff1,diff2)
		return True

	# no hit
	return False
	
#  return the number of queens 
def get_queensNum():
	return QUEENS


# retrive the position of queens from the board
def get_queens(board):

	queens_pos = [0]*QUEENS
	for i in range(QUEENS):
		for j in range(QUEENS):
			if(board[i][j]==1):
				queens_pos[j] = i

	return queens_pos



# return the score (pair of queen hits) for a set of queen positions
def get_score(queens_pos):
	score = 0 
	for i in range(QUEENS):
		pos1 = (i,queens_pos[i])
		for k in range(i+1,QUEENS):
			pos2 = (k,queens_pos[k])
			if(is_hit(pos1,pos2)):
				score = score +1
			# print("pos1-->",pos1,"pos2-->",pos2,"score --> ",score)

	return score


# prints the board with the scores 
def print_score_board(board):
	score_board = get_board_score(board)
	print_board(score_board)


# calculate the score board ( how main pairs of hits) 
# input is the board
def get_board_score(board):
	queens_pos_real = get_queens(board)
	# score_board = board.copy()
	score_board = []
	for i in range(QUEENS):
		temp = []
		for j  in range(QUEENS):
			temp.append(0)
		score_board.append(temp)

	for i in range(QUEENS):
		queens_pos = queens_pos_real.copy()
		for j  in range(QUEENS):
			queens_pos[i] = j
			score = get_score(queens_pos)
			score_board[j][i] = score
	return score_board

# finds the best move given the score board
# we select the minimum number 
# if there is a tie select the min x, min y
def get_best_move(board_score):
	index_x = 100000
	index_y = 100000
	best_score = 100000

	for x in range(QUEENS):
		for y in range(QUEENS):
			score = board_score[y][x]

			if(x==index_x and y < index_y):
				index_x = x						
				index_y = y
			if(score==best_score):
				if(x<index_x):
					index_x = x
					index_y = y

			if(score<best_score):
				index_x = x
				index_y = y
				best_score = score

	# print("best-->",best_score)
	# print("move-->",index_x,index_y)

	return (index_x,index_y),best_score


def gradient_search(board):

	# while score does not improve
	while(True):

		# get queens position
		queens_pos = get_queens(board)
		score = get_score(queens_pos)

		# find board score
		board_score = get_board_score(board)

		# find best possible move
		move,next_score = get_best_move(board_score)

		# play the move
		board[move[1]][move[0]] = 1

		# if score same with previous score end it
		if(next_score==score):
			break

		# reset old position of queen
		y = queens_pos[move[0]]
		board[y][move[0]] = 0

		# if score == 0 end it, we won
		if(next_score==0):
			break


	final_score = get_score(get_queens(board))
	if(final_score==0):
		print("We Won!")
		return True
	return False
