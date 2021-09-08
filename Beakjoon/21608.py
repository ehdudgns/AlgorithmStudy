import sys

def inputData():
	global classRoom
	global N
	N = int(sys.stdin.readline().strip())
	classRoom = []
	for _ in range(N):
		tmp = [0]*N
		classRoom.append(tmp)
	for _ in range(N*N):
		tmp = [int(i) for i in sys.stdin.readline().split(" ")]
		seatAssignment(tmp)
	print(N)

def seatAssignment(student):
	global classRoom
	global N
	if classRoom[1][1] == 0:
		classRoom[1][1] = student[0]
	
	for i in range(N):
		for j in range(N):
			if classRoom[i][j] != 0:
				continue
			else:
				if 0 <= i-1 and 0 <= j-1 and i+1 < N-1 and j+1 < N-1:
					
	


if __name__ == "__main__":
	global classRoom
	inputData()
	print(classRoom)
