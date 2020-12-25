import sys
a=int(sys.stdin.readline().rstrip())
for i in range(1,a+1):
    for j in range(0,i):
        print("*",end='')
    print()
