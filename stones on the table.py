n=int(input())
s=input()
stones=0
for i in range(n-1):
    if s[i]==s[i+1]:
        stones+=1
print(stones)        