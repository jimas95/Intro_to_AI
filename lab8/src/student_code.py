import common

def part_one_classifier(data_train, data_test):

	exp = experiment1()
	exp.fit(data_train)
	exp.test_evaluation(data_test)
	return


def part_two_classifier(data_train, data_test):

	exp = experiment2()
	exp.fit(data_train)
	exp.test_evaluation(data_test)
	return


# perceptorn implementation for 2 classifiers
class experiment1:

	# initialize
	def __init__(self, learning_rate=0.03):
		self.lr = learning_rate
		self.activation_func = self._unit_step_func
		self.weights = [0,0,0]
        
	# learning functions 
	def fit(self,train_data):
		
		data_num = len(train_data)

		epoxh = 0 
		while(True):
			accuracy = 0
			for i in range(data_num):
				x , y, val = train_data[i] # split data to variables
				prediction = self.predict(x,y) # make prediction

				# if wrong update weights
				if(prediction!=val):
					self.update_weights(prediction,val,x,y)
				else:
					accuracy += 1
				
			# calculate accuracy
			accuracy = accuracy*100/data_num 
			epoxh += 1

			# break if we reached 100% accuracy
			if(accuracy > 99.999):
				print(f"Epoxh: {epoxh} accuracy --> {accuracy} %")
				break

			# debug print
			if(epoxh%400==0):
				print(f"Epoxh: {epoxh} accuracy --> {accuracy} %")
		

	# prediction functions, input is data values
	def predict(self,x,y):
		linear_output = self.weights[0] + self.weights[1] * x + self.weights[2] * y
		return self.activation_func(linear_output)
		
	# missclassifed data, update weights
	# predi is predictited value
	# val is the correct class
	# x,y values of sample
	def update_weights(self,predi,val,x,y):

		update = self.lr*(val-predi)
		self.weights[0] += update*1 # bias term
		self.weights[1] += update*x
		self.weights[2] += update*y


	# prediction on test data
	def test_evaluation(self,test_data):
		for index,data in enumerate(test_data):
			x,y,val = data
			prediction = self.predict(x,y)
			test_data[index][2] = prediction

		
	# based on prediction return 1 or 0 
	def _unit_step_func(self, x):
		if(x>=0):
			return 1
		return 0




# perceptorn implementation for 10 classifiers
class experiment2:

	# init functions
	# classifiers of weight should classifie class 0 to weights[0], 1 to weights[1],... n to weights[n]
	def __init__(self, learning_rate=0.01):
		self.lr = learning_rate
		self.activation_func = self._unit_step_func
		self.weights = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]] 
        

	def fit(self,train_data):
		
		data_num = len(train_data)
		epoxh = 0 
		while(True):
			accuracy = 0
			for i in range(data_num):
				x , y, val = train_data[i]
				prediction = self.predict(x,y)
				if(prediction!=val):
					self.update_weights(prediction,int(val),x,y)
				else:
					accuracy += 1
			
			accuracy = accuracy*100/data_num 
			epoxh += 1
			if(accuracy > 99.999):
				print(f"Epoxh: {epoxh} accuracy --> {accuracy} %")
				break
			if(epoxh%10==0):
				print(f"Epoxh: {epoxh} accuracy --> {accuracy} %")
		

	# prediction functions, input is data values
	# we choose class based on maximum value return by each classifier weights
	def predict(self,x,y):
		max_val = - 1000000
		index = -1 
		for i in range(10):
			output = self.weights[i][0] * x + self.weights[i][1] * y
			if output > max_val:
				max_val = output
				index = i
		return index
		

	# missclassifed data, update weights, we update only the one that missclassified and the one that should classify the correct value
	# predi is predictited value
	# val is the correct class
	# x,y values of sample
	def update_weights(self,predi,val,x,y):
		self.weights[val][0]   += self.lr*x
		self.weights[val][1]   += self.lr*y
		self.weights[predi][0] -= self.lr*x
		self.weights[predi][1] -= self.lr*y


	# prediction on test data
	def test_evaluation(self,test_data):
		for index,data in enumerate(test_data):
			x,y,val = data
			prediction = self.predict(x,y)
			test_data[index][2] = prediction

		
	# based on prediction return 1 or 0 
	def _unit_step_func(self, x):
		if(x>=0):
			return 1
		return 0


