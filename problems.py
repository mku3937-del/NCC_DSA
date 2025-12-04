a=int(input())
b=int(input())
c=int(input())
if a>0:
    x=a*b
else:
    x=a-b
if c%2==0:
    y=c+x
else:
    y=c-x
if y<0:
    y=(-1*y)
print(y)    
    