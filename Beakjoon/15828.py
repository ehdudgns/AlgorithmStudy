import sys

input = sys.stdin.readline

def pushQueue(n,m):
	global queue
	if len(queue) < m:
		queue.append(n)

def popQueue():
	global queue
	if queue:
		queue.pop(0)

def outputData():
	global queue
	if queue:
		return " ".join(queue)
	return "empty"

def inputData():
	global queue
	bufSize = int(input())
	queue = []
	while 1:
		tmp = input().strip()
		if tmp == '-1':
			break
		elif tmp == '0':
			popQueue()
		else:
			pushQueue(tmp,bufSize)
	print(outputData())

if __name__ == '__main__':
	inputData()