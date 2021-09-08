import sys


def inputData():
	global result,notation
	notation = {}
	for i in range(10):
		notation[str(i)] = i
	for i in range(26):
		notation[chr(ord('A')+i)] = i+10
	N,B = sys.stdin.readline().split(" ")
	mainRun(N,B)

def mainRun(N,B):
	length = len(N)-1
	ans = 0
	for i in N:
		ans += notation[i]*pow(int(B),length)
		length -= 1
	print(ans)

if __name__ == '__main__' :
	inputData()


