import sys
input = sys.stdin.readline
n = int(input())
for i in range(n):
    for _ in range(n*2):
        print(" " if (i+_)%2 else "*",end='')
    print()
