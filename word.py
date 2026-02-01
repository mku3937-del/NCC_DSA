s=input()
c=0
d=0
for i in range(len(s)):
    if s[i]==s[i].upper():
        c+=1
    elif s[i]==s[i].lower():
        d+=1
if c>d:
    print(s.upper())
if c<=d:
    print(s.lower())           
    