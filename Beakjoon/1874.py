import sys

input = sys.stdin.readline

def inputData():
	global stackArr
	global ans
	check = True
	ans = ""
	cnt = 1
	N = int(input())
	stackArr = []
	for _ in range(N):
		tmp = int(input())
		topValue = top()
		while tmp > topValue:
			pushData(cnt)
			cnt += 1
			topValue = top()
		topValue = popData()
		while topValue > tmp:
			topValue = popData()
			if topValue == 0:
				check = False
				break
	if check:
		outputData(ans)
	else:
		print("NO")

def outputData(ans):
	tmp = ans.split(" ")
	for i in tmp:
		if i:
			print(i)

def top():
	global stackArr
	if stackArr:
		return stackArr[len(stackArr)-1]
	return 0

def pushData(n):
	global stackArr
	global ans
	stackArr.append(n)
	ans += "+ "

def popData():
	global stackArr
	global ans
	if stackArr:
		n = stackArr.pop()
		ans += "- "
		return n
	return 0

if __name__ == "__main__":
	inputData()
	
