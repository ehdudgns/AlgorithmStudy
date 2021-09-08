import sys

def inputData():

	global notation,result
	result = []
	notation = []
	for i in range(10):
		notation.append(str(i))
	for i in range(26):
		notation.append(chr(ord('A')+i))

	N,B = [int(i) for i in sys.stdin.readline().split(" ")]
	runMainFunc(N,B)
	ans = "".join(result)
	print(ans)
def runMainFunc(n,b):
	global notation,result

	if n < b:
		result.append(notation[n])
		return notation[n]
	else:
		runMainFunc(n//b,b)
		result.append(notation[n%b])
	

if __name__=='__main__':
	inputData()