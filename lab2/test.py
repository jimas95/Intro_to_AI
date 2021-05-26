import student_code


student_code.QUEENS = 8 


def init_board():
	return [[0 for x in range(0,student_code.QUEENS)] for x in range(0,student_code.QUEENS)]
	
	
def set_board(board, data):
	for y in range(0,student_code.QUEENS):
		for x in range(0,student_code.QUEENS):
			board[y][x]=int(data[y*student_code.QUEENS+x])



num = student_code.get_queensNum()
if(num == 8 ):
    print("test 1 passed")
   



data1 = (
"11111111"
"00000000"
"00000000"
"00000000"
"00000000"
"00000000"
"00000000"
"00000000")


data2 = (
"01000010"
"00000000"
"10000000"
"00100000"
"00001000"
"00010000"
"00000100"
"00000001")



data3 = (
"00000000"
"00000000"
"00000000"
"00010000"
"10001000"
"01000101"
"00100010"
"00000000")

board = init_board()
set_board(board, data1)
queens_pos = student_code.get_queens(board)
correct = True
for queen in queens_pos:
    if(queen!=0):
        correct == False
    
if (correct):
    print("test 2 passed")
else:
    print("test 2 fail")

score = student_code.get_score(queens_pos)

if(score==28):
    print("test 2.1 passed")
else:
    print("test 2.1 fail")
    print(score)




#######################

set_board(board, data2)
queens_pos = student_code.get_queens(board)
queens_cor = [2,0,3,5,4,6,0,7]

for i in range(student_code.QUEENS):
    if(queens_pos[i]!=queens_cor[i]):
        correct == False
    
if (correct):
    print("test 3 passed")
else:
    print("test 3 fail")


score = student_code.get_score(queens_pos)

if(score==5):
    print("test 3.1 passed")
else:
    print("test 3.1 fail")
    print(score)



#####################


set_board(board, data3)
queens_pos = student_code.get_queens(board)
queens_cor = [4,5,6,3,4,5,6,5]

for i in range(student_code.QUEENS):
    if(queens_pos[i]!=queens_cor[i]):
        correct == False
    
if (correct):
    print("test 4 passed")
else:
    print("test 4 fail")


score = student_code.get_score(queens_pos)

if(score==17):
    print("test 4.1 passed")
else:
    print("test 4.1 fail")
    print(score)


queens_cor = [0,5,6,3,4,5,6,5]
score = student_code.get_score(queens_cor)

if(score==18):
    print("test 4.2 passed")
else:
    print("test 4.2 fail")
    print(score)

queens_cor = [1,5,6,3,4,5,6,5]
score = student_code.get_score(queens_cor)

if(score==14):
    print("test 4.3 passed")
else:
    print("test 4.3 fail")
    print(score)

queens_cor = [2,5,6,3,4,5,6,5]
score = student_code.get_score(queens_cor)

if(score==14):
    print("test 4.4 passed")
else:
    print("test 4.4 fail")
    print(score)

queens_cor = [4,5,6,5,4,5,6,5]
score = student_code.get_score(queens_cor)

if(score==18):
    print("test 4.5 passed")
else:
    print("test 4.5 fail")
    print(score)


set_board(board, data3)
student_code.print_score_board(board)
student_code.print_score_board(board)
score_board = student_code.get_board_score(board)
move,score = student_code.get_best_move(score_board)
print(move)
print(score)

set_board(board, data3)
student_code.gradient_search(board)
student_code.print_board(board)
score = student_code.get_score(student_code.get_queens(board))
print("score --> ", score)