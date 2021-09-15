import sys

input = sys.stdin.readline


def DFS(graph,start,visited):
	stack = [start]
	while stack:
		n = stack.pop()
		if not visited[n]:
			tmp = list(reversed(graph[n]))
			stack += tmp
			visited[n] = True
			print(n,end='')

def BFS(graph,start,visited):
	queue = [start]
	visited[start] = True
	while queue:
		n = queue.pop(0)
		print(n,end='')
		for i in graph[n]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
	
N,M,V = [int(i) for i in input().split(" ")]
graph = {}
for i in range(N+1):
	graph[i] = []
for _ in range(M):
	a,b = [int(i) for i in input().split(" ")]
	if len(graph[a]) != 0:
		graph[a].append(b)
	else:
		graph[a] = [b]
	if len(graph[b]) !=0 :
		graph[b].append(a)
	else:
		graph[b] = [a]
Dvisited = [False]*(N+1)
DFS(graph,V,Dvisited)
print()
Bvisited = [False]*(N+1)
BFS(graph,V,Bvisited)
print()