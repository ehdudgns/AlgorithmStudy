import sys

inputData = sys.stdin.readline().strip()

tmp = int("0o" + inputData, 8)

print(str(bin(tmp)).split("0b")[1])
