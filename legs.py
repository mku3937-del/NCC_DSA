n=int(input())
for i in range (n):
    m=int(input())
    if m<6:
        print(1)
    elif m%4==0:  
        print((m//4))     
    else:
        print((m//4)+1)  