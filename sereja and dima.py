n = int(input())
cards = list(map(int, input().split()))
sereja= 0
dima = 0
l = 0
r = n - 1
for i in range(n):
    if cards[l] > cards[r]:
        chosen = cards[l]
        l += 1
    else:
        chosen = cards[r]
        r -= 1
    if i % 2 == 0:
        sereja+= chosen
    else:
        dima += chosen

print(sereja, dima)
