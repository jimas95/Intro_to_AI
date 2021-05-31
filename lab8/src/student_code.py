import common


def part_one_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 1
	exp = experiment1()
	exp.fit(data_train)
	exp.test_evaluation(data_test)
	return


def part_two_classifier(data_train, data_test):
	# PUT YOUR CODE HERE
	# Access the training data using "data_train[i][j]"
	# Training data contains 3 cols per row: X in 
	# index 0, Y in index 1 and Class in index 2
	# Access the test data using "data_test[i][j]"
	# Test data contains 2 cols per row: X in 
	# index 0 and Y in index 1, and a blank space in index 2 
	# to be filled with class
	# The class value could be a 0 or a 8
	exp = experiment2()
	exp.fit(data_train)
	exp.test_evaluation(data_test)
	return




class experiment1:

	def __init__(self, learning_rate=0.01, epoxes=1000):
		self.lr = learning_rate
		self.epoxes = epoxes
		self.activation_func = self._unit_step_func
		self.weights = [0,0,0]
        

	def fit(self,train_data):
		
		data_num = len(train_data)

		for epoxh in range(self.epoxes):
			accuracy = 0
			for i in range(len(train_data)):
				x , y, val = train_data[i]
				prediction = self.predict(x,y)
				if(prediction!=val):
					self.update_weights(prediction,val,x,y)
				else:
					accuracy += 1
				
			# print(f"Epoxh: {epoxh} accuracy --> {accuracy*100/data_num} %")
		print(f"Epoxh: {epoxh} accuracy --> {accuracy*100/data_num} %")


	def predict(self,x,y):
		linear_output = self.weights[0] + self.weights[1] * x + self.weights[2] * y
		return self.activation_func(linear_output)
		

	def update_weights(self,predi,val,x,y):
		update = self.lr*(val-predi)

		self.weights[0] += update*1
		self.weights[1] += update*x
		self.weights[2] += update*y


	def test_evaluation(self,test_data):
		for index,data in enumerate(test_data):
			x,y,val = data
			prediction = self.predict(x,y)
			test_data[index][2] = prediction

		

	def _unit_step_func(self, x):
		if(x>=0):
			return 1
		return 0





class experiment2:

	def __init__(self, learning_rate=0.01, epoxes=100):
		self.lr = learning_rate
		self.epoxes = epoxes
		self.activation_func = self._unit_step_func
		self.weights = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        

	def fit(self,train_data):
		
		data_num = len(train_data)

		for epoxh in range(self.epoxes):
			accuracy = 0
			for i in range(len(train_data)):
				x , y, val = train_data[i]
				prediction = self.predict(x,y)
				if(prediction!=val):
					self.update_weights(prediction,int(val),x,y)
				else:
					accuracy += 1
				
			# print(f"Epoxh: {epoxh} accuracy --> {accuracy*100/data_num} %")
		print(f"Epoxh: {epoxh} accuracy --> {accuracy*100/data_num} %")


	def predict(self,x,y):
		max_val = - 1000000
		index = -1 
		for i in range(10):
			output = self.weights[i][0] * x + self.weights[i][1] * y
			if output > max_val:
				max_val = output
				index = i
		return index
		

	def update_weights(self,predi,val,x,y):
		self.weights[val][0]   += self.lr*x
		self.weights[val][1]   += self.lr*y
		self.weights[predi][0] -= self.lr*x
		self.weights[predi][1] -= self.lr*y


	def test_evaluation(self,test_data):
		for index,data in enumerate(test_data):
			x,y,val = data
			prediction = self.predict(x,y)
			test_data[index][2] = prediction

		

	def _unit_step_func(self, x):
		if(x>=0):
			return 1
		return 0