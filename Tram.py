n=int(input())
x=[]
y=[]
p=[]
for i in range (n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
for i in range(n-1):
    k=(y[i]-x[i+1])+y[i+1]
    p.append(k)
print(max(p))   