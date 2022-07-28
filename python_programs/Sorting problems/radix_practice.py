def radixcount(inputarray,placevalue):
	countarray = [0]*10
	size = len(arr)
	for i in range(size):
		countarray[(inputarray[i]//placevalue)%10] +=1
	for j in range(1,10):
		countarray[j] += countarray[j-1]
	outputarray = [0]*size
	i = len(arr)-1
	while i>=0:
		curr = inputarray[i]
		placeele = (curr//placevalue)%10
		countarray[placeele]-=1
		outputarray[countarray[placeele]]=curr
		i-=1
	return outputarray
def radix(arr):
	m = max(arr)
	d = 1
	while m:
		d+=1
		m//=10
	placevalue=1
	while d>0:
		arr = radixcount(arr,placevalue)
		placevalue*=10
		d-=1
	return arr
arr = [5,3,0,2,4,1,6,3,5,1,9,6,7,1,3,94]
print(radix(arr))
