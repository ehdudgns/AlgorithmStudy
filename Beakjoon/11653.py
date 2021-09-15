import sys
import math

input = sys.stdin.readline
print = sys.stdout.write

def primeFactorization(num):
	d = 2
	while d <= num:
		if num%d == 0:
			print(str(d)+"\n")
			num = num/d
		else:
			d += 1

N = int(input())

primeFactorization(N)
