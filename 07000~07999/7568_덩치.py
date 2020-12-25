import sys
n=int(sys.stdin.readline().rstrip())
arr=[list(map(int,sys.stdin.readline().rstrip().split(" "))) for _ in range(n)]
cnt=[1]*n
for i in range(0,len(arr)):
    for j in range(0,len(arr)):
        if(arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]):
            cnt[i]+=1
for i in cnt:
    print(i)
    
