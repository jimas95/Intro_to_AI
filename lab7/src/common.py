class constants:
	WIDTH = 200
	HEIGHT = 200

class Line:
	def __init__(self):
		self.m=0
		self.b=0
		self.theta=0
		self.r=0
	
def init_space(heigh, width):
	return [[0 for x in range(width)] for x in range(heigh)]

def lock():
	while(1):
		print("This is makis,You should not do this! WRITE YOUR OWN CODE!")