def myMin(a,b):
    return a if a<=b else b

import sys
input=sys.stdin.readline
n=int(input())
c2=0
c5=0
for _ in range(1,n+1):
    while(_%2==0):
        _/=2
        c2+=1
    while(_%5==0):
        _/=5
        c5+=1
print(myMin(c2,c5))

