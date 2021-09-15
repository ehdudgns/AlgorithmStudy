import sys
import math

def isPrime(num):
	if num == 1:
		return False
	for i in range(2,int(math.sqrt(num))+1):
		if num % i == 0:
			return False
	return True

def goldbach(n):
	for i in range(2,n):
		if isPrime(i):
			if isPrime(n-i):
				print(str(n) + " = " + str(i) + " + " + str(n-i))
				return
	print("Goldbach's conjecture is wrong.") 

while 1:
	tmp = int(sys.stdin.readline())
	if tmp == 0:
		break
	goldbach(tmp)