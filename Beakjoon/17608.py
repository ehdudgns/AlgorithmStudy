import sys

input = sys.stdin.readline

def stackTop():
	global stack
	length = len(stack) - 1
	if stack:
		return stack[length]
	return 0

if __name__ =='__main__':
	global stack
	stack = []
	origin = []
	N = int(input())
	for _ in range(N):
		tmp = int(input())
		origin.append(tmp)
	origin.reverse()
	for i in origin:
		if stackTop() < i:
			stack.append(i)
	print(len(stack))


