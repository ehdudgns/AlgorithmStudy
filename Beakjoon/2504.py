import sys

input = sys.stdin.readline

def inputData():
	n = input()
	a = n.replace('()','2')
	b = a.replace('[]','3')
	return b

def pushStack(n):
	global stack
	if n == '(' or n == '[':
		stack.append(n)
	else:
		stack.append(int(n))

def popStack(currentIndex):
	global stack
	if len(stack) > 1:
		n = stack.pop()
		if n == '(' or n == '[':
			stack.append(n)
			return 0
		n = int(n)
		topValue = stack.pop()
		if topValue == '(' and currentIndex == ')':
			return 2*n
		elif topValue == '[' and currentIndex == ']':
			return 3*n
		elif topValue != '(' and topValue != '[':
			tmp = n + int(topValue)
			pushStack(tmp)
			return popStack(currentIndex)
	return 0


def mainRun():
	global stack
	stack = []
	n = inputData().strip()
	ans = 0
	for i in n:
		if i == ')' or i == ']':
			tmp = popStack(i)
			if tmp == 0:
				stack = []
				break
			pushStack(tmp)
		elif i == '{' or i == '}':
			continue
		else:
			pushStack(i)
	if stack:
		if '(' in stack or '[' in stack:
			ans = 0
		else:
			ans = sum(stack)
	else:
		ans = 0
	print(ans)




if __name__ == '__main__':
	mainRun()