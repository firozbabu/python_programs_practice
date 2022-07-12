
'''

def max_heapify(arr,  index, heap_size): 
	largest_num = index 
	left_index = 2 * index + 1 
	right_index = 2 * index + 2	 
	if left_index < heap_size and arr[left_index] > arr[largest_num]: 
		largest_num = left_index 
	if right_index < heap_size and arr[right_index] > arr[largest_num]: 
		largest_num = right_index
	if largest_num != index: 
		arr[largest_num],arr[index] = arr[index],arr[largest_num]
		print(arr)
		max_heapify(arr, largest_num, heap_size) 
def heapSort(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        max_heapify(arr,i,n)
    print('heap sort')
    for i in range(n-1,-1,-1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, 0,i) 

arr = [4,0,1,15,79,28,35,68]
heapSort(arr)
print(arr)
'''

'''
#max_heap
def heapify(arr, n, i): 
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2 
	if l < n and arr[i] < arr[l]: 
		largest = l 
	if r < n and arr[largest] < arr[r]: 
		largest = r 
	if largest != i: 
		arr[i],arr[largest] = arr[largest],arr[i]
		print(arr)
		heapify(arr, n, largest) 
def heapSort(arr): 
	n = len(arr)  
	for i in range(n, -1, -1): 
		heapify(arr, n, i)
	print('heap sort')
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0) 
arr = [4,0,1,15,79,28,35,68]
heapSort(arr)
print(arr)
'''

#min_heap
def min_heapify(arr, n, i): 
	smallest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2 
	if l < n and arr[l] < arr[i]: 
		smallest = l
	if r < n and arr[r] < arr[smallest]: 
		smallest = r 
	if smallest != i: 
		arr[smallest],arr[i] = arr[i],arr[smallest]
		print(arr)
		min_heapify(arr, n, smallest) 
def heapSort(arr): 
	n = len(arr)  
	for i in range(n//2-1, -1, -1): 
		min_heapify(arr, n, i)
	print('heap sort')
	for i in range(n-1, 0, -1): 
		arr[i], arr[0] = arr[0], arr[i] 
		min_heapify(arr, i, 0) 
arr = [4,0,1,15,79,28,35,68]
heapSort(arr)
print(arr)






