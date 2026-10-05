n,m=map(int,input().split())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
top=0
bottom=n-1
left=0
right=m-1
while top <= bottom and left <= right:
    for j in range(left, right + 1):
        print(a[top][j], end=" ")
    top+=1
    for i in range(top, bottom + 1):
        print(a[i][right], end=" ")
    right-=1
    for j in range(right, left - 1, -1):
        print(a[bottom][j], end=" ")
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        print(a[i][left], end=" ")
    left+=1
