import common


# find starting and end goal
def get_info(map):
	goal = (0,0)
	start = (0,0)
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if(map[y][x] == 2):
				start = (y,x)

			if(map[y][x] == 3):
				goal = (y,x)
			
	return start,goal

def check_bounds(pos):

	if(pos[0]>-1 and pos[0]<common.constants.MAP_HEIGHT):
		if(pos[1]>-1 and pos[1]<common.constants.MAP_WIDTH):
			return True
	return False

# check if a cell is a wall
# return False is  wall
# return true if is not wall
def is_not_wall(pos,map):
	y = pos[0]
	x = pos[1]
	if(map[y][x]==1):
		return False
	return True
	
# return possible movements
def get_neighbours(pos,map,flag):

	pos1 = (pos[0],pos[1]+1)
	pos2 = (pos[0]+1,pos[1])
	pos3 = (pos[0],pos[1]-1)
	pos4 = (pos[0]-1,pos[1])

	pos_pos = []


	if(check_bounds(pos1) and is_not_wall(pos1,map)):
		pos_pos.append(pos1)
	if(check_bounds(pos2) and is_not_wall(pos2,map)):
		pos_pos.append(pos2)

	if(check_bounds(pos3) and is_not_wall(pos3,map)):
		pos_pos.append(pos3)

	if(check_bounds(pos4) and is_not_wall(pos4,map)):
		pos_pos.append(pos4)

	if flag:
		 pos_pos.reverse()
	return pos_pos

# check if we reached goal
def is_goal(pos,goal):
	return pos==goal

# return manhatan distance
def get_dist(pos,goal):
	return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])


def finish(map,visited,all_paths):
	start,goal = get_info(map)

	for vi in visited:
		y = vi[0]
		x = vi[1]
		map[y][x] = 4

	parent = all_paths[goal]
	while(parent != start):
		y = parent[0]
		x = parent[1]
		map[y][x] = 5
		parent = all_paths[parent]
	
	y = start[0]
	x = start[1]
	map[y][x] = 5
	y = goal[0]
	x = goal[1]
	map[y][x] = 5

#  heristic of A start
def get_next_move(moves,goal,all_paths,start):
	distance = []
	for move in moves:
		dist = 0
		# add curent distance 
		if(len(all_paths)>1): 
			parent = all_paths[move]
			while(parent != start):
				dist = dist + 1
				parent = all_paths[parent]

		dist = dist + get_dist(move,goal)

		distance.append(dist)
	# find min distance
	min_dist = min(distance)
	my_index = []
	
	# check ties
	for i in range(len(distance)):
		if(distance[i]==min_dist):
			my_index.append(i)
	
	# print("---------")
	# print(moves)
	# print(distance)
	# print(my_index)
	min_xx = 10000
	final_index = -1
	for i in my_index:
		move = moves[i]
		if(min_xx==move[1]):
			if(moves[final_index][0]>move[0]):
				final_index = i
				min_xx = moves[i][1]

		if(min_xx>move[1]):
			final_index = i
			min_xx = move[1]

	# print("move --> ",moves[final_index])

	return moves.pop(final_index)

def astar_search(map):
	found = False
	height = common.constants.MAP_HEIGHT
	width = common.constants.MAP_WIDTH
	start,goal = get_info(map)

	visited = set() # List to keep track of visited nodes.
	queue = []     #Initialize a queue
	all_paths = {}

	queue.append(start)

# while still have unvisited nodes continue
	# for i in range(10):
	while queue:
		# s = queue.pop() # get last state
		s = get_next_move(queue,goal,all_paths,start)
		if(is_goal(s,goal)):						
					finish(map,visited,all_paths)
					# common.print_map(map)
					return True
		# print (s, end = " ") 
		visited.add(s)

		for next_s in get_neighbours(s,map,True):
			if next_s not in visited:
				if next_s not in queue:
					queue.append(next_s)
					all_paths[next_s] = s

				


	for vi in visited:
		y = vi[0]
		x = vi[1]
		map[y][x] = 4
	return found

