import sys

def changeNotation(num,n):
	if num == 0:
		pass
	else:
		changeNotation(num//n,n)
		print(num%n,end=" ")

def reverserNotation(numStr,n):
	# print(numStr)
	result = 0
	length = len(numStr)
	for i in range(length):
		result += int(numStr[i])*pow(n,length-1-i)
	return result

def inputData():
	A,B = [int(i) for i in sys.stdin.readline().split(" ")]
	t = int(sys.stdin.readline())
	numArr = sys.stdin.readline().strip().split(" ")
	changeNotation(reverserNotation(numArr,A),B)
	print()
if __name__ == "__main__":
	inputData()