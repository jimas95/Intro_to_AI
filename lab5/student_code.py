import common

#helpful, but not needed
class variables:
	counter=0


# check if sudoku is full and valid
def is_win(sudoku):	
	for y in range(9):
		for x in range(9):
			value = sudoku[y][x]
			
			if(value==0):
				# print("wait what ?")
				return False

			sudoku[y][x] = 0
			if(value!=0 and common.can_yx_be_z(sudoku,y,x,value)):
				sudoku[y][x] = value
				pass
			else:
				sudoku[y][x] = value
				# print("wait what ?")
				# print(y,x,value)
				return False
	
	print("is win!")
	return True

# ckeck if sudoku is valid ( return True if is not valid)
def is_valid(sudoku):	
	for y in range(9):
		for x in range(9):
			value = sudoku[y][x]
			sudoku[y][x] = 0
			if(value!=0):
				if(common.can_yx_be_z(sudoku,y,x,value)):
					sudoku[y][x] = value
				else:
					# print(y,x,value)
					sudoku[y][x] = value
					# print("is NOT Valid!")
					return False

	# print("is Valid!")
	return True




def print_board(sudoku):
	print("My board --> ")
	for line in sudoku:
		print(line)


def backtrack(sudoku,variable):

	# DEBUG 
	# print_board(sudoku)

	# if variable.counter>325:
	# 	return True

	# increase counter
	variable.counter = variable.counter + 1

	# check is sudoku is finished 
	if(is_win(sudoku)):
		return True

	

	# play next move
	for y in range(9):
		for x in range(9):
			if(sudoku[y][x]==0):

				# try all possible moves
				for pos_move in range(9):
					if(common.can_yx_be_z(sudoku,y,x,pos_move+1)): # check is sudoku is invalid
						sudoku[y][x] = pos_move + 1
						res = backtrack(sudoku,variable)
						if(res):
							return True
						else:
							sudoku[y][x] = 0
				if(sudoku[y][x]==0):
					return False


	return False

def forwardtrack(sudoku,variable,domain):

	# DEBUG 
	# print_board(sudoku)

	# if variable.counter>325:
	# 	return True

	# increase counter
	variable.counter = variable.counter + 1

	# check is sudoku is finished 
	if(is_win(sudoku)):
		return True

	

	# play next move
	for y in range(9):
		for x in range(9):
			if(sudoku[y][x]==0):

				# try all possible moves
				for pos_move in range(9):
					if(common.can_yx_be_z(sudoku,y,x,pos_move+1)): # check is sudoku is invalid
						

						# update domain
						# domCopy = domain.copy()
						domCopy = update_domain(domain,y,x,pos_move+1)
						# domain = domCopy.copy()
						# check if domain is okei
						# if(check_domain(domain)==False):
						# 	print("opa ! ")

						# if(check_domain(domCopy)==False):
						# 	print("lakis")

						if(check_domain(domCopy)):
							# print("opa ! ")

							# play the move
							sudoku[y][x] = pos_move + 1

							res = forwardtrack(sudoku,variable,domCopy)
							if(res):
								return True
							else:
								sudoku[y][x] = 0
						# else:
							# domain = domCopy.copy()

				if(sudoku[y][x]==0):
					return False


	return False


# if there is a problem in domain return false
def check_domain(domain):
	for line in domain:
		for var in line:
			if(len(var)==0):
				return False
	return True


def deep_copy(domain):
	mycp = []
	for y in range(9):
		mycp1 = []
		for x in range(9):
			mycp1.append(list(domain[y][x]))
		mycp.append(list(mycp1))
	return mycp


#  update values based on new input 
def update_domain(domain,y,x,z):
	domain_temp = deep_copy(domain.copy())
	for i in range(9):
		if (x!=i):
			try:
				domain_temp[y][i].remove(z)
			except ValueError:
				pass  # do nothing!

		if (y!=i):
			try:
				domain_temp[i][x].remove(z)
			except ValueError:
				pass  # do nothing!

		if(y!=(int(y/3)*3+int(i/3)) and x!=(int(x/3)*3+i%3)): 
			try:
				domain_temp[int(y/3)*3+int(i/3)][int(x/3)*3+i%3].remove(z)
			except ValueError:
				pass  # do nothing!
	return domain_temp


def init_domain():
	return [[[1,2,3,4,5,6,7,8,9] for x in range(9)] for x in range(9)]
	

def sudoku_backtracking(sudoku):
	# set counter
	variables.counter = 0

	# call backtracker
	backtrack(sudoku,variables)

	return variables.counter

def sudoku_forwardchecking(sudoku):

	# set counter
	variables.counter = 0
	
	# call forward tracking
	domain = init_domain()
	for y in range(9):
		for x in range(9):
			if(sudoku[y][x]!=0):
				domain = update_domain(domain,y,x,sudoku[y][x])

	forwardtrack(sudoku,variables,domain)
	
	return variables.counter
