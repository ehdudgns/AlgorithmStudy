import sys

def inputData():
	t = int(sys.stdin.readline().strip())
	for i in range(t):
		arr = [int(i) for i in sys.stdin.readline().split(" ")]
		arr = arr[1:]
		arr.sort()
		print(gcdSum(arr))

def gcdSum(arr):
	result = 0
	for i in range(len(arr)-1):
		for j in range(i+1,len(arr)):
			result += gcd(arr[i],arr[j])
	return result

def gcd(a,b):
	if a%b == 0:
		return b
	else:
		return gcd(b,a%b)

if __name__ =='__main__':
	inputData()