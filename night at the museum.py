m=input()
c=0
s='a'
for x in m:
    d=abs(ord(x)-ord(s))
    a=min(d,26-d)
    c+=a
    s=x
print(c)