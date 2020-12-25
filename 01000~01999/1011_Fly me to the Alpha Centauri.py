import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    x,y=map(int,input().split())
    d=y-x
    i=1
    cnt=0
    while(True):
        if(d<=i*2):
            break
        d-=i*2
        i+=1
        cnt+=2
    if(d!=0):
        cnt+= 1 if d<=i else 2
    print(cnt)
        
