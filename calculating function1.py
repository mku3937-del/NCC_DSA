n=int(input())
if n==0:
    print(0)
elif n%2==0:
    print(n//2)
elif n%2!=0:
    print(-1*((n+1)//2))