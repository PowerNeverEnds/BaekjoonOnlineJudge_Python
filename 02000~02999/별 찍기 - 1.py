import sys
input=sys.stdin.readline
n = int(input())
for _ in range(n):
    for _ in range(_+1):
        print("*",end='')
    print()
