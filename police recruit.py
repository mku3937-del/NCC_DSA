n=int(input())
l=list(map(int,input().split()))
p=0
c=0
for x in l:
    if x>0:
        p+=x
    else:
        if p>0:
            p+=x
        else:
            c-=x
print(c)                    