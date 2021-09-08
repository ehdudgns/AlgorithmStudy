import sys

def printPrimeNumber(m,n):
	prime = [0]*1000001
	prime[1] = 1
	for i in range(2,n+1):
		if prime[i] == 1:
			pass
		else:
			j = 2
			while i*j <= n:
				if prime[i*j] == 0:			
					prime[i*j] = 1
				j+=1
	for i in range(m,n+1):
		if prime[i] == 0:
			print(i)

M,N = [int(i) for i in sys.stdin.readline().split(" ")]
printPrimeNumber(M,N)