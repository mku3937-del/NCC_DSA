n=int(input())
l=0
m=[]
for i in range(n):
    a,b=map(int,input().split())
    l=l-a+b
    m.append(l)
print(max(m))    
