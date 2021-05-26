import common

# find starting and end goal
def get_info(map):
	goal = (0,0)
	start = (0,0)
	for y in range(0,common.constants.MAP_HEIGHT):
		for x in range(0,common.constants.MAP_WIDTH):
			if(map[y][x] is 2):
				start = (y,x)

			if(map[y][x] is 3):
				goal = (y,x)
			
	return start,goal

def check_bounds(pos):

	if(pos[0]>-1 and pos[0]<common.constants.MAP_HEIGHT):
		if(pos[1]>-1 and pos[1]<common.constants.MAP_WIDTH):
			return True
	return False

def is_not_wall(pos,map):
	y = pos[0]
	x = pos[1]
	if(map[y][x]==1):
		return False
	return True
	

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

def df_search(map):
	found = False
	# print("NEW TEST")
	# print("BFS")
	# common.print_map(map)
	height = common.constants.MAP_HEIGHT
	width = common.constants.MAP_WIDTH
	start,goal = get_info(map)
	# print("map  size:",height,width)
	# print("start pos:" , start)
	# print("goal  pos:" , goal)

	visited = set() # List to keep track of visited nodes.
	queue = []     #Initialize a queue
	all_paths = {}

	queue.append(start)

# while still have unvisited nodes continue
	while queue:
		s = queue.pop() # get last state
		if(is_goal(s,goal)):						
					finish(map,visited,all_paths)
					# common.print_map(map)
					return True
		# print (s, end = " ") 
		visited.add(s)

		for next_s in get_neighbours(s,map,True):
			if next_s not in visited:

				queue.append(next_s)
				all_paths[next_s] = s

				


	for vi in visited:
		y = vi[0]
		x = vi[1]
		map[y][x] = 4
	return found

def bf_search(map):
	found = False

	height = common.constants.MAP_HEIGHT
	width = common.constants.MAP_WIDTH
	start,goal = get_info(map)

	# print("NEW TEST")
	# print("BFS")
	# common.print_map(map)

	# print("map  size:",height,width)
	# print("start pos:" , start)
	# print("goal  pos:" , goal)

	visited = set() # List to keep track of visited nodes.
	queue = []     #Initialize a queue
	all_paths = {}

	queue.append(start)

# while still have unvisited nodes continue
	while queue:
		s = queue.pop(0) # get first state
		if(is_goal(s,goal)):						
					finish(map,visited,all_paths)
					return True
		# print (s, end = " ") 
		visited.add(s)

		for next_s in get_neighbours(s,map,False):
			if next_s not in visited:

				queue.append(next_s)
				all_paths[next_s] = s

				


	for vi in visited:
		y = vi[0]
		x = vi[1]
		map[y][x] = 4
	return found
