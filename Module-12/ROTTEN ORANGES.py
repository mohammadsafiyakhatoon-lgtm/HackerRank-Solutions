from collections import deque
n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
q=deque()
f=0
for i in range(n):
    for j in range(m):
        if a[i][j]==2:q.append((i,j))
        if a[i][j]==1:f+=1
t=0
d=[(-1,0),(1,0),(0,-1),(0,1)]
while q and f:
    for _ in range(len(q)):
        i,j=q.popleft()
        for x,y in d:
            ni,nj=i+x,j+y
            if 0<=ni<n and 0<=nj<m and a[ni][nj]==1:
                a[ni][nj]=2
                f-=1
                q.append((ni,nj))
    t+=1
print(t if f==0 else -1)
