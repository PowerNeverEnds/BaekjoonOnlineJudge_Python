import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    for _ in range((n-1)-i):
        print(" ",end='')
    for _ in range(i*2+1):
        print("*",end='')
    print()
