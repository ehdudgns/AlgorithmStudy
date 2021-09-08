import sys

def inputData():
	global arr,N,M,x,y,cmd,command
	arr = []
	N,M,x,y,cmd = [int(i) for i in sys.stdin.readline().split(" ")]
	for _ in range(N):
		arr.append([int(i) for i in sys.stdin.readline().split(" ")])
	command = [int(i) for i in sys.stdin.readline().split(" ")]


def initMakeDice():
	global arr,dice
	dice = []
	

def moveDice(x,y):
	global arr,N,M
	if x > -1 and y > -1 and x < N and y < M:
		print(arr[x][y])


if __name__ == '__main__':
	global arr,x,y,cmd,command
	inputData()
	for i in command:
		moveDice(x,y)
		if i == 4:
			x += 1
		elif i == 3:
			x -= 1
		elif i == 2:
			y -= 1
		elif i == 1:
			y += 1

