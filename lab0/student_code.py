# heapify
def heapify(data, n, i):
	
   largest = i # largest value
   l_child = 2 * i + 1 # left child
   r_child = 2 * i + 2 # right child

   # if left child exists
   if l_child < n and data[i] < data[l_child]:
      largest = l_child
	  
   # if right child exits
   if r_child < n and data[largest] < data[r_child]:
      largest = r_child
	  
   # root
   if largest != i:
      data[i],data[largest] = data[largest],data[i] # swap
      # root.
      heapify(data, n, largest)



def order(data):
	
	# get size of data 
	n = len(data)

	# abandon if something is not right 
	if(n==0 or type(data)!=type([])):
		return 0

	# maxheap
	for i in range(n, -1, -1):
		heapify(data, n, i)

	# element extraction
	for i in range(n-1, 0, -1):
		data[i], data[0] = data[0], data[i] # swap
		heapify(data, i, 0)

	return data

