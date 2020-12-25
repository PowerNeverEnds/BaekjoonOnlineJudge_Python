import sys
input=sys.stdin.readline
n=input().rstrip()
re=0
MOD=20000303
for _ in n:
    re=re*10+int(_);
    re%=MOD;

##i=len(n)%2+2
##re=int(n[0:i])
##while(i!=len(n)):
##   re=re*100+int(n[i:i+2])
##   re%=MOD;
##   i+=2
print(re)
