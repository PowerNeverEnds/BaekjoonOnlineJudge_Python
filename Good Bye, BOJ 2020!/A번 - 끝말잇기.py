import sys
input = sys.stdin.readline
N = int(input())
strList = input().rsplit()
ch=strList[0][0]
bo=1
for _ in strList:
    if(_[0]==ch):
        pass
    else:
        bo=0
        break
print(bo)
