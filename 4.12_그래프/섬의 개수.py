def dfs(grid, i, j):
    if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
        return

    grid[i][j] = 0

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)

def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid, i, j)

                count += 1

    return count

grid = list()
for _ in range(4):
    grid.append(list(map(int, input())))

print(numIslands(grid))
