import sys

input = sys.stdin.readline

N,M = [int(i) for i in input().split(" ")]

a = [int(i) for i in input().split(" ")]

maxValue = max(a)

def findHeights(value):
	ans = 0
	for i in a:
		if (i-value)>0:
			ans += (i-value)
	return ans

def findBS(mx,mn,f):
	ans = 0
	while 1:
		mid = (mx + mn)//2
		if mx < mn:
			break
		if findHeights(mid) >= f:
			mn = mid + 1
		else:
			mx = mid - 1
	return mx

print(findBS(maxValue,1,M))