n=int(input ())
m=list (map(int, input(). split()))
s=int (input())
for i in range (s) :
    x, y =map(int ,input(). split())
    x=x-1
    y=y-1
    if x>0:
        m[x-1]+=y
    if x<n-1:
        m[x+1]+=m[x]-(y+1)
    m[x]=0 
for l in m:
    print (l)