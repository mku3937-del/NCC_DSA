n=int(input())
x=0
for i in range(n):
    m=input()
    if "++"in m:
        x+=1
    else:
        x-=1
print(x)   