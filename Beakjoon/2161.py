import sys

input = sys.stdin.readline

def inputData():
	global card
	card = []
	n = int(input())
	for i in range(n,0,-1):
		card.append(i)

def mainRun():
	global card
	while len(card) > 1:
		print(card.pop(),end = " ")
		card = [card.pop()] + card
	print(card[0])


if __name__ == '__main__':
	inputData()
	mainRun()