from collections import Counter

data = None
safe_zone = 10000

with open("input.txt") as f:
    data = [(int(x), int(y)) for x, y in [c.split(", ") for c in f.read().splitlines()]]


max_x, max_y = (0, 0)
for coord in data:
    x, y = coord
    max_x = x if x > max_x else max_x
    max_y = y if y > max_y else max_x


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve():
    grid = [["."] * (max_x + 1) for _ in range(max_y + 1)]
    safe_coords = []
    flattened_grid = data.copy()
    for i, coord in enumerate(data):
        x, y = coord
        grid[y][x] = coord

    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            mds = {coord: manhattan(coord, (x, y)) for coord in data}
            if sum(mds.values()) < safe_zone:
                safe_coords.append((x, y))

            if value in data:
                continue

            nearest_distance = 10000
            nearest_point = (0, 0)
            for coord, md in mds.items():
                if md < nearest_distance:
                    nearest_distance = md
                    nearest_point = coord
            for coord, md in mds.items():
                if md == nearest_distance and coord != nearest_point:
                    nearest_distance = -1
            grid[y][x] = nearest_point if nearest_distance != -1 else "."
            flattened_grid.append(grid[y][x])

    infinite_points = set()
    for i, row in enumerate(grid):
        if i == 0 or i == len(grid) - 1:
            for v in row:
                infinite_points.add(v)
        infinite_points.add(row[0])
        infinite_points.add(row[-1])

    freq = Counter([x for x in flattened_grid if x not in infinite_points])
    mc = freq.most_common(1)

    return (mc[0][1], len(safe_coords))


results = solve()
print("Part 1:", results[0])
print("Part 2:", results[1])
