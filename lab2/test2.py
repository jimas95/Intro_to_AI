import student_code

class bcolors:
	RED    = "\x1b[31m"
	GREEN  = "\x1b[32m"
	NORMAL = "\x1b[0m"

def init_board():
	return [[0 for x in range(0,10)] for x in range(0,10)]
	
	
def set_board(board, data):
	for y in range(0,10):
		for x in range(0,10):
			board[y][x]=int(data[y*10+x])

def check_result(map1, map2):
	result=True
	
	for y in range(0,10):
		v=""
		for x in range(0,10):
			if (map1[y][x]==map2[y][x]):
				v+=bcolors.GREEN+str(map1[y][x])+bcolors.NORMAL+' '
			else:
				result = False
				v+=bcolors.RED+str(map1[y][x])+bcolors.NORMAL+' '
		print(v)
	if (result):
		print("Test Result: " + bcolors.GREEN+"Passed"+bcolors.NORMAL)
	else:
		print("Test Result: " + bcolors.RED+"Failed"+bcolors.NORMAL)
	print()
	return result
	
result=0	
	
data1 = (
"1000000001"
"0100000000"
"0010000000"
"0001000000"
"0000100000"
"0000011110"
"0000000000"
"0000000000"
"0000000000"
"0000000000")

result1 = (
"0000000001"
"0000001000"
"0100000000"
"0001000000"
"0000100000"
"0000000110"
"0000000000"
"1000000000"
"0010000000"
"0000010000"
)


all_passed = True
print("testing board 1")
board1 = init_board();
solution1 = init_board();
set_board(board1, data1)
set_board(solution1, result1)
df1 = student_code.gradient_search(board1)
if df1==True:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
elif df1==False:
	print( bcolors.GREEN+"test return good"+bcolors.NORMAL)
	result=result+1
else:
	print( bcolors.RED+"test return bad"+bcolors.NORMAL)
	result=0
result=result+check_result(solution1,board1)



if result==2:
	print( bcolors.GREEN+"all tests passed"+bcolors.NORMAL)
else:
	print( bcolors.RED+"test fail"+bcolors.NORMAL)

