import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
	tmp = input().strip().split(" ")
	tmp.reverse()
	temp = " ".join(tmp)
	result = "Case #"+str(i+1)+": "+temp
	print(result)