n=int(input())
l=[]
c=1
for i in range(n):
    t=int(input())
    l.append(t)
for i in range (n-1):
    if l[i]!=l[i+1]:
        c+=1
print(c)        