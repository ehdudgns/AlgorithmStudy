import sys

input = sys.stdin.readline

tmp = input()

problem = 0

while 1:
	tmp = input().strip()
	if tmp == "고무오리":
		if problem == 0:
			problem += 2
		else:
			problem -= 1
	elif tmp == "문제":
		problem += 1
	elif tmp == "고무오리 디버깅 끝":
		break
if problem == 0:
	print("고무오리야 사랑해")
else:
	print("힝구")