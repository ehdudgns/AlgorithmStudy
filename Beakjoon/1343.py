import sys

def inputBoard() :
    board = sys.stdin.readline().strip()
    return board.split(".")

def replaceStringSolution() :
    board = sys.stdin.readline().strip()
    board = board.replace('XXXX','AAAA')
    board = board.replace('XX','BB')
    if 'X' in board:
        return -1
    else:
        return board

def mySolution() :
    ans = []
    board = inputBoard()
    for i in board :
        if len(i) % 2 == 1:
            return -1
        else:
            if len(i) == 0:
                ans.append("")
            else:
                ans.append(makePolyomino(i))
    return ".".join(ans)

def makePolyomino(arr):
    ans = ""
    length = len(arr)
    while length > 2:
        ans += "AAAA"
        length -= 4
    if length != 0 :
        return ans + "BB"
    return ans

if __name__ == "__main__":
    print(replaceStringSolution())

