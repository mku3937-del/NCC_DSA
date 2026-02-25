k,r=map(int,input().split())
for i in range(1,11):
    if i*k%10==0 or i*k%10==r:
        print(i)
        break
    