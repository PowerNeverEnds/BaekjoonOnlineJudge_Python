import sys
input=sys.stdin.readline
def myAbs(a):
    return (a if a>=0 else -a);

for _ in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
##    print(x1,y1,r1,x2,y2,r2)
    if(x1==x2 and y1==y2):
        print(-1 if r1==r2 else 0)
    else:
        xx=(x1-x2)*(x1-x2)
        yy=(y1-y2)*(y1-y2)
        xy=xx+yy
        rpr=(r1+r2)*(r1+r2)
        rmr=(r1-r2)*(r1-r2)
##        print(xx,yy,xy,rpr,rmr)
        if(rpr<xy):
            print(0)
        elif(xy<rmr):
            print(0)
        elif(xy==rpr or xy==rmr):
            print(1)
        elif(rmr<xy and xy<rpr):
            print(2)
        else:
            print("?")
