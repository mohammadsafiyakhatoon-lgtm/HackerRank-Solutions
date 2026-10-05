n=int(input())
a=list(map(int,input().split()))
total=sum(a)
answer=10**9
def solve(i,count,s):
    global answer
    if i==n:
        if abs(2*count-n)<=1:
            answer=min(answer,abs(total-2*s))
        return
    solve(i+1,count+1,s+a[i])
    solve(i+1,count,s)
solve(0,0,0)
print(answer)
