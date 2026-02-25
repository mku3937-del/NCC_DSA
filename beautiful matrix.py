for i in range(1, 6):
    row = list(map(int, input().split()))
    if 1 in row:
        row_pos = i
        col_pos = row.index(1) + 1
        moves = abs(row_pos - 3) + abs(col_pos - 3)
        print(moves)
        break
    