import common


# return true if game is over (Tie)
# check if the board if tie (full)
def is_tie(board):
	res = True
	for item in board:
		if(item==0):
			res = False
	return res


# max value of minimax
def max_value(state):
	v = - 1000000

	# check state
	result = common.game_status(state)

	# if someone won or its a tie return
	if(result == common.constants.X):
		return 10
	if(result == common.constants.O):
		return -10
	if(is_tie(state)):
		return 0

	for y in range(3): # open all possible moves 
		for x in range(3):
		# play new move
			cell_num = common.get_cell(state,y,x)
			if(cell_num==0):
				new_state = state.copy()
				common.set_cell(new_state,y,x,common.constants.X)
				v = max(v,min_value(new_state)) # estimate
	return v

# min value of minimax
def min_value(state):
	v = 1000000

	# check state
	result = common.game_status(state)

	# if someone won or its a tie return
	if(result == common.constants.X):
		return 10
	if(result == common.constants.O):
		return -10
	if(is_tie(state)):
		return 0


	for y in range(3): # open all possible moves 
		for x in range(3):
		# play new move
			cell_num = common.get_cell(state,y,x)
			if(cell_num==0):
				new_state = state.copy()
				common.set_cell(new_state,y,x,common.constants.O)
				v = min(v,max_value(new_state)) # estimate
	return v



def minmax_tictactoe(board, turn):

	result = common.constants.NONE
	if(turn==common.constants.X):
		result = max_value(board)

	if(turn==common.constants.O):
		result = min_value(board)
	
	if(result==10):
		return common.constants.X
	elif(result==-10):
		return common.constants.O
	return common.constants.NONE
	



def max_valueAB(state,alpha,beta):
	v = - 1000000
	# check state
	result = common.game_status(state)

	# if someone won or its a tie return 
	if(result == common.constants.X):
		return 10
	if(result == common.constants.O):
		return -10
	if(is_tie(state)):
		return 0

	for y in range(3): # open all possible moves 
		for x in range(3):
		# play new move
			cell_num = common.get_cell(state,y,x)
			if(cell_num==0):
				new_state = state.copy()
				common.set_cell(new_state,y,x,common.constants.X)
				v = max(v,min_valueAB(new_state,alpha,beta)) # estimate
				if(v>=beta):
					return v
				alpha = max(alpha,v)	
	return v

def min_valueAB(state,alpha,beta):
	v = 1000000

	# check state
	result = common.game_status(state)

	# if someone won or its a tie return 
	if(result == common.constants.X):
		return 10
	if(result == common.constants.O):
		return -10
	if(is_tie(state)):
		return 0


	for y in range(3): # open all possible moves 
		for x in range(3):
		# play new move
			cell_num = common.get_cell(state,y,x)
			if(cell_num==0):
				new_state = state.copy()
				common.set_cell(new_state,y,x,common.constants.O)
				v = min(v,max_valueAB(new_state,alpha,beta)) # estimate
				if v<=alpha :
					return v
				beta = min(beta,v)
				
	return v


def abprun_tictactoe(board, turn):
	# init variables 
	result = common.constants.NONE
	alpha = -100000 
	beta = 100000

	if(turn==common.constants.X):
		result = max_valueAB(board,alpha,beta)

	if(turn==common.constants.O):
		result = min_valueAB(board,alpha,beta)
	
	if(result==10):
		return common.constants.X
	elif(result==-10):
		return common.constants.O
	return common.constants.NONE
	