def is_gridChallenge(grid):
    grid = [sorted(row) for row in grid]
    t = tuple(zip(*grid))
    if all([row[i] <= row[i + 1] for row in t for i in range(len(row) - 1)]):
        return 'YES'
    return 'NO'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = is_gridChallenge(grid)

        print(result)
        print(grid)