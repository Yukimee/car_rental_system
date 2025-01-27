number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[2][2])  # result = 9 (role and column)
print(number_grid[2][1])  # result = 8 (role and column)

for row in number_grid:
    print(row)

for row in number_grid:
    for col in row:
        print(col)  # print 1 all the way down to 0


for row in number_grid:
    for col in row:
        print(row)
