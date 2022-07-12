


graphs = {
	'A':['B','C'],
	'B':['G','E','C'],
	'C':['D','F'],
	'D':['E'],
	'E':['G'],
	'F':['D']}

'''
g = {
	'A':['B','C'],
	'B':['C','D'],
	'C':['D'],
	'D':['C'],
	'E':['F'],
	'F':['C']
	}
'''


'''
this one is for single path find
'''



'''
def fi(graphs,start,end,path = []):
	print(path)
	path = path+[start]
	if start==end:
		return path
	if not (start in graphs):
		return None
	for node in graphs[start]:
		if node not in path:
			newpath  = fi(graphs,node,end,path)
			if newpath:
				return newpath
	return None
print(fi(graphs,'A','G'))

'''


#this one is for find all paths
def fi(graphs,start,end,path=[]):
    path = path+[start]
    if start == end:
        return [path]
    if not ( start in graphs):
        return []
    paths = []
    for node in graphs[start]:
        if node not in path:
            newpaths = fi(graphs,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
print(fi(graphs,'A','G'))

'''
#reference for for loop and return statement until the for loop completed

def f():
    for i in range(9):
        if False:
            return i
    return i,False # returns at last iteration
print(f())
'''
