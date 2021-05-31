import common
import math #note, for this lab only, your are allowed to import math

SIZE = 200

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	print("---------------------------------")

	# print(type(image))
	print(f"size --> {len(image)} , {len(image[0])}")
	
	detector = LineDetector(image)
	detector.detect()
	line = detector.myLine
	print("---------------------------------")


	# line=common.Line()
	# line.m=-1
	# line.b=300
	return line

def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"
	detector = CircleDetector(image)
	detector.detect()
	detected_cicles = detector.detected_cicles
	return detected_cicles
				


# class for detecting lines
class LineDetector:


	def __init__(self,image_):
		self.gridSize = 2000
		self.votes = common.init_space(self.gridSize,self.gridSize) # votes[b][m]
		self.myLine = common.Line()
		self.image = image_
		self.points = []
		self.size = len(image_)
		
		if(len(image_)!=len(image_[0])):
			print("we have a problem!")
		if(SIZE != self.size):
			print("we have a problem!!")
		

	# scan the gray image and keep points of interest	
	# we store only black pixels
	def scanImage(self):
		for y in range(self.size):
			for x in range(self.size):
				if(self.image[y][x]==0):
					self.points.append((x,y))
					# print(f"x,y {x},{y} --> {self.points[-1][0]},{self.points[-1][1]}")
		print(f"scanning image --> found {len(self.points)} points")					
		pass

	# update the voting image 
	# y = m*x + b
	def createHoughSpace(self):
		for i in range(self.gridSize):
				for point in self.points:
					x = point[0]
					y = point[1]
					m = self.uncast_m(i)
					b = y - m*x
					self.vote(m,b)



	def vote(self,m,b):
		b_val = int(self.cast_b(b))
		m_val = int(self.cast_m(m))
		if(b_val>-1 and b_val<self.gridSize):
			if(m_val>-1 and m_val<self.gridSize):
				self.votes[b_val][m_val] = self.votes[b_val][m_val] + 1

	def findLine(self):
		max_value = -1
		for b in range(self.gridSize):
			for m in range(self.gridSize):
				if(self.votes[b][m]>max_value):
					max_value = self.votes[b][m]
					self.myLine.b = self.uncast_b(b)
					self.myLine.m = self.uncast_m(m)
		print(f"best vote --> {max_value}")


	# range from -10 to 10 cast to 0 - 2000
	def cast_m(self,m_val):
		return (m_val+10)*100

	# range from 0 - 2000 cast to -10 to 10
	def uncast_m(self,m_val):
		return m_val/100 -10
	
	# range from -1000 to 1000 cast to 0 - 2000
	def cast_b(self,b_val):
		return b_val + 1000

	# range from 0 - 2000 cast to -1000 to 1000
	def uncast_b(self,b_val):
		return b_val - 1000


	
	# detect the line
	def detect(self):
		
		self.scanImage()
		self.createHoughSpace()
		self.findLine()




# class for detecting Circle
class CircleDetector:


	def __init__(self,image_):
		self.gridSize = 200
		self.radius = 30
		self.detected_cicles = 0 
		self.votes = common.init_space(self.gridSize,self.gridSize) # votes[a][b]
		self.image = image_
		self.points = []
		self.size = len(image_)
		
		if(len(image_)!=len(image_[0])):
			print("we have a problem!")
		if(SIZE != self.size):
			print("we have a problem!!")
		

	# scan the gray image and keep points of interest	
	# we store only black pixels
	def scanImage(self):
		for y in range(self.size):
			for x in range(self.size):
				if(self.image[y][x]==0):
					self.points.append((x,y))
					# print(f"x,y {x},{y} --> {self.points[-1][0]},{self.points[-1][1]}")
		print(f"scanning image --> found {len(self.points)} points")					
		pass

	# update the voting image 
	def createHoughSpace(self):
		stepTotal = 360*2
		dtheta = 2*math.pi/stepTotal
		for point in self.points:
			x = point[0]
			y = point[1]
			for theta in range(stepTotal):
				a = x + self.radius*math.cos(theta*dtheta)
				b = y - self.radius*math.sin(theta*dtheta)
				self.vote(a,b)



	def vote(self,a,b):
		a = int(a+1)
		b = int(b+1)
		if(a>-1 and a<self.gridSize):
			if(b>-1 and b<self.gridSize):
				self.votes[a][b] = self.votes[a][b] + 1

	def findCircles(self):
		max_value = -1
		for a in range(self.gridSize):
			for b in range(self.gridSize):
				if(self.votes[a][b]>max_value):
					max_value = self.votes[a][b]
		print(f"best vote --> {max_value}")

		for a in range(self.gridSize):
			for b in range(self.gridSize):
				if(self.votes[a][b]>(max_value-50) and self.votes[a][b]>600):
					# print(f"Circle --> votes: {self.votes[a][b]}")
					self.detected_cicles = self.detected_cicles + 1
	
	# detect the Circle
	def detect(self):
		
		self.scanImage()
		self.createHoughSpace()
		self.findCircles()

