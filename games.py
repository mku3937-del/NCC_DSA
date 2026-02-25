n=int(input())
count=0
home=list()
guest=list()
for _ in range(n):
    x,y=list(map(int,input().split()))
    home.append(x)
    guest.append(y)
for i in range(n):
    count += guest.count(home[i])
print(count)