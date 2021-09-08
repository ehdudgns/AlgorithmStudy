import sys

value = sys.stdin.readline().strip()
value = "0b"+value
a = int(value,2)
b = str(oct(a)).split("0o")[1]
print(b)