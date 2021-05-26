from typing import ValuesView
import common

SIZE = 6 

def drone_flight_planner (map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	print("********************************************************")
	print("I am the master")
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# 

	# create my bot
	bot = PLANNER(map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount)
	bot.print_data()
	bot.learn()
	bot.print_data()
	



	print("This is the end!")
	print("********************************************************")

	return 100000000



class PLANNER:
	def __init__(self,map,policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
		self.map=map
		self.policies=policies
		self.values=values
		self.delivery_fee=delivery_fee
		self.battery_drop_cost= 0
		# self.battery_drop_cost= -battery_drop_cost
		self.dronerepair_cost= -dronerepair_cost
		self.discount=discount


		# init board
		self.banned_location = []
		for y in range(SIZE):
			for x in range(SIZE):
				# what is my square ? 
				squareVal = self.map[y][x]
				
				if(squareVal==common.constants.CUSTOMER):
					self.values[y][x] = self.delivery_fee
					self.policies[y][x] = common.constants.EXIT
					self.banned_location.append([y,x])
				if(squareVal==common.constants.RIVAL):
					self.values[y][x] = self.dronerepair_cost
					self.policies[y][x] = common.constants.EXIT
					self.banned_location.append([y,x])





	# my main loop
	def learn(self):
		k = 0
		while(True):
			res = self.update()
			if(res and k>3):
				break

			k = k + 1 
			print(f"Learn --> k{k}")
			self.print_the_values()
			if(k>600):#break condition
				break



	def update(self):
		# calculate new value board
		old_values = list(self.values)
		for y in range(SIZE):
			for x in range(SIZE):
				if(self.map[y][x]!=common.constants.RIVAL and self.map[y][x]!=common.constants.CUSTOMER): # prohibits updating the target goal or the death goal
					VK1_val,VK1_action = self.get_new_VK(x,y)
					self.values[y][x]   = VK1_val
					self.policies[y][x] = VK1_action

		# check if we have converge
		result = self.check_converge(old_values,self.values)
		return result






	# check if the updated values are relative the same or not
	# return True if the values have converged
	def check_converge(self,values_old,values_new):
		for y in range(SIZE):
			for x in range(SIZE):
				diff = abs(values_old[y][x] - values_new[y][x])
				if(diff>0.01):
					print("plaka me kaneis ?")
					return False
		print("eee ti se kanw mpaglama ")
		return True


	# return the new best V_k+1 and the action
	def get_new_VK(self,x,y):
		best_val = -99999999
		best_action = -1 

		# for every action
		for action in range(1,9):
			value = self.get_reward(x,y,action)
			# print(f"possible value {y},{x}--> {value}")
			if(value>best_val): # TO DO implement a better one with priority on ties
				best_val = value
				best_action = action
		
		if(best_action==-1):
			print("ERROR ERROR")

		return best_val,best_action

	# will return the score/value based on where the drone is and what action does
	# implements the SUM (T*[R+gamma*V])
	def get_reward(self,x,y,action1):

		score = 0 
		if(action1==common.constants.EXIT):
			print("WTF ? This should happen!")
			print("WTF ? This should happen!")

		action2,action3 = self.get_unliky_actions(action1)

		if(action1>common.constants.EOFF):
			score = 0.80*self.get_score(x,y,action1,True)+\
					0.10*self.get_score(x,y,action2,True)+\
					0.10*self.get_score(x,y,action3,True)
		else:

			score = 0.70*self.get_score(x,y,action1,False)+\
					0.15*self.get_score(x,y,action2,False)+\
					0.15*self.get_score(x,y,action3,False)

		return score 

	# based on action return the new coordinate position
	def move(self,x,y,action):
		new_x = x
		new_y = y
		if(action==common.constants.SOFF or action==common.constants.SON):
			new_y = y + 1
		if(action==common.constants.WOFF or action==common.constants.WON):
			new_x = x - 1
		if(action==common.constants.NOFF or action==common.constants.NON):
			new_y = y - 1
		if(action==common.constants.EOFF or action==common.constants.EON):
			new_x = x + 1

		return self.check_coords(new_x,new_y)


	# corrent new coordinates if they are out of bounds
	def check_coords(self,x,y):
		if x >= SIZE:
			x = SIZE -1 
		if x<0:
			x = 0 

		if y >= SIZE:
			y = SIZE -1 
		if y<0:
			y = 0 
		return x,y

	def get_score(self,x,y,action,power):
		# return reward + gamma*Value_of_new_pos
		# self.
		pos_x,pos_y = self.move(x,y,action)
		score = self.get_R(power) + self.discount*self.values[pos_y][pos_x] 
		return score

	# return the reward that will get for this action ( basically only the cost of movement)
	def get_R(self,power):
		battery_cost = self.battery_drop_cost
		reward = 0 
		if(power):
			battery_cost = 2*self.battery_drop_cost
		return battery_cost 
		

	# based on action you get returned the 2 possible actions due to uncertainty
	def get_unliky_actions(self,action):
		if(action==common.constants.EXIT):
			print("Error ! ")
			print("Error ! ")
			print("Error ! action is exit ?")
			return 0,0

		# off case
		if(action==common.constants.SOFF):
			return common.constants.WOFF,common.constants.EOFF

		if(action==common.constants.WOFF):
			return common.constants.NOFF,common.constants.SOFF

		if(action==common.constants.NOFF):
			return common.constants.WOFF,common.constants.EOFF

		if(action==common.constants.EOFF):
			return common.constants.NOFF,common.constants.SOFF


		#  on case
		if(action==common.constants.SON):
			return common.constants.WON,common.constants.EON

		if(action==common.constants.WON):
			return common.constants.NON,common.constants.SON

		if(action==common.constants.NON):
			return common.constants.WON,common.constants.EON

		if(action==common.constants.EON):
			return common.constants.NON,common.constants.SON



	def print_data(self):
		print("MAP")
		for y in range(6):
			v=""
			for x in range(6):
				v+=str(self.map[y][x]) + ","
			v+='\t'		
			print(v)
		
		print("-------")
		print("policies")

		for y in range(6):
			v=""
			for x in range(6):
				v+=str(self.policies[y][x]) + ","
			v+='\t'		
			print(v)
		
		print("-------")
		print("values")

		for y in range(6):
			v=""
			for x in range(6):
				v+=str(self.values[y][x]) + ","
			v+='\t'		
			print(v)

		print("-------")

		print("okei now costs:")
		print(f"delivery \t\t--> {self.delivery_fee}")
		print(f"battery_drop_cost \t--> {self.battery_drop_cost}")
		print(f"dronerepair_cost \t--> {self.dronerepair_cost}")
		print(f"discount \t\t--> {self.discount}")

	def print_the_values(self):
		print("Vals")
		for y in range(6):
			v=""
			for x in range(6):
				# v+=str(self.values[y][x]) + ","
				v+="{0:.2f}".format(self.values[y][x])+ ",  "
			v+='\t'		
			print(v)
		
		print("-------")