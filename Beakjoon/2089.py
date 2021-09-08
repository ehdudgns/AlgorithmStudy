import sys

num = int(sys.stdin.readline())

def changeNotation(num,n):
	global ans
	if num == 0:
		pass
	else:
		changeNotation(-(num//n),n)
		print(num%n,end ="")

if num == 0:
	print(0)
else:
	changeNotation(num,2)
	print()