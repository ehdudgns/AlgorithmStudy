import sys

def DFS(idx):

	global graph,visit

	if visit[idx] != 0:
		return
	else:
		print(idx)
		visit[idx] = 1
		idx = graph[idx][0]
		DFS(idx)


def setGraph(a,b):
	global graph
	if a in graph:
		graph[a].append(b)
	else:
		graph[a] = [b]

def inputData():
	n,m,start = [int(i) for i in sys.stdin.readline().split(" ")]
	global visit,graph 
	visit = [0]*(n+1)
	graph = {}
	for _ in range(m):
		idx,value = [int(i) for i in sys.stdin.readline().split(" ")]
		setGraph(idx,value)
		setGraph(value,idx)
		
	return start 

if __name__ == '__main__':
	startVertax = inputData()
	DFS(startVertax)