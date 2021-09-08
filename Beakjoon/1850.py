import sys

def gcd(a,b):
	if a%b == 0:
		ans = ""
		for i in range(b):
			ans+="1"
		return ans
	else:
		return gcd(b,a%b)

def inputData():
	a,b = [int(i) for i in sys.stdin.readline().split(" ")]
	if a > b:
		return a,b
	else:
		return b,a

if __name__ == '__main__':
	a,b = inputData()
	print(gcd(a,b))

