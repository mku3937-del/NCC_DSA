n=int(input())
c=0
for i in range(n):
    m=list(map(int,input().split()))
    if sum(m)>1:
        c+=1
print(c)        