n=int(input())
for i in range(n):
    w=input()
    if len(w)>10:
        m=w[0]
        p=w[-1]
        o=str(len(w)-2)
        print(m+o+p)
    else:
        print(w)    