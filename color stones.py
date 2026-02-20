s=input()
t=input()
c=0
r=0
for j in range(len(t)):
        if s[r]==t[j]:
            c+=1
            r+=1
print(c+1)        