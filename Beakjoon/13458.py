import sys

def input():
	N = int(sys.stdin.readline())
	candidateArr = [int(i) for i in sys.stdin.readline().split(" ")]
	B,C = [int(i) for i in sys.stdin.readline().split(" ")]
	return N,candidateArr,B,C

def findPeson(a,b,c):
	if (a-b) > 0 :
		if (a-b) % c == 0:
			return (a-b) // c
		else:
			return (a-b) // c + 1
	else :
		return 0

def run(N,arr,b,c):
	answer = 0
	for i in range(N):
		answer += findPeson(arr[i],b,c)
	answer += N
	return answer

if __name__ == "__main__":
	N,candidateArr,B,C = input()
	
	print(run(N,candidateArr,B,C))