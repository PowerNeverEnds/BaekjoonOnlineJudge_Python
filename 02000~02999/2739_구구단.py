import sys
input=sys.stdin.readline
N = int(input().rstrip())
for _ in range(1,10):
    print("{0} * {1} = {2}".format(N, _, N*_))

