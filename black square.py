l=list(map(int,input().split()))
s=input()
c=[]
for x in s:
    m=int(x)
    c.append(l[m-1])
print(sum(c))