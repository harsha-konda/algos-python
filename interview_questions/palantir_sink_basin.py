def labelTopology(elevationList):
	height,elevations = elevationList[0],elevationList[1:]

	elevationList = [[-1 for _ in range(height)] for _ in range(height)]

	for k in range(len(elevations)):
		i = k // height
		j = k%height
		elevationList[i][j] = elevations[k]

	store = {}

	for i in range(height):
		for j in range(height):
			store[(i,j)] = (i,j)


	def union(node,parent):
		parent1 = find(node) 
		parent2 = find(parent)
		store[parent1] = parent2


	def find(node):
		if store[node] == node:
			return node
		return find(store[node])

	def indexOfMin(node):
		if i > 0 and elevationList[i-1][j] < elevationList[node[0]][node[1]]:
			node = (i-1,j)

		if j > 0 and elevationList[i][j-1] < elevationList[node[0]][node[1]]:
			node = (i,j-1) 

		if i < height-1 and elevationList[i+1][j] < elevationList[node[0]][node[1]]:
			node = (i+1,j)

		if j < height -1  and elevationList[i][j+1] < elevationList[node[0]][node[1]]:
			node = (i,j+1)
		return node


	for i in range(height):
		for j in range(height):
			minNode = indexOfMin((i,j))
			union((i,j),minNode)
	


	for i in range(height):
		print([find((i,j)) for j in range(height)])

	sinks = {}
	for value in store.values():
		value = find(value)
		if value not in sinks:
			sinks[value] = 0
		sinks[value]+=1
	print(sinks)

if __name__ == '__main__':
	labelTopology([3,1,5,2,2,4,7,3,6,9])
	labelTopology([5, 1, 0, 2, 5, 8, 2, 3, 4, 7, 9, 3, 5, 7, 8, 9, 1, 2, 5, 4, 3, 3, 3, 5, 2, 1])
