import itertools

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

red_tiles = []
green_tiles = set()

boundaries_y = {}
boundaries_x = {}

def connect(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    if y2 == y1:
        sgn = 1 if x2 > x1 else -1
        for xm in range(x1, x2 + sgn, sgn):
            if xm not in boundaries_y:
                boundaries_y[xm] = [y1, y1]
            cur_y_min, cur_y_max = boundaries_y[xm]
            boundaries_y[xm][0] = min(cur_y_min, y1)
            boundaries_y[xm][1] = max(cur_y_max, y1)
            green_tiles.add((xm, y1))
    else:
        sgn = 1 if y2 > y1 else -1
        for ym in range(y1, y2 + sgn, sgn):
            if ym not in boundaries_x:
                boundaries_x[ym] = [x1, x1]
            cur_x_min, cur_x_max = boundaries_x[ym]
            boundaries_x[ym][0] = min(cur_x_min, x1)
            boundaries_x[ym][1] = max(cur_x_max, x1)
            green_tiles.add((x1, ym))

prev_tile = None

for r in l:
    tile = tuple(map(int, r.split(',')))
    x, y = tile

    red_tiles.append(tile)

    if prev_tile is None:
        prev_tile = tile
        continue

    connect(prev_tile, tile)

    prev_tile = tile

connect(red_tiles[-1], red_tiles[0])


red_tiles = set(red_tiles)

def visualize():
    for y in range(8):
        s = ''
        for x in range(12):
            coord = (x, y)
            if coord in red_tiles:
                s += 'O'
            elif coord in green_tiles:
                s += 'X'
            else:
                s += '.'
        print(s)

def get_area(tile1, tile2):
    dx = abs(tile1[0] - tile2[0]) + 1
    dy = abs(tile1[1] - tile2[1]) + 1
    return dx * dy

def valid_ray(ray):
    for tile in ray:
        x, y = tile
        y_min, y_max = boundaries_y[x]
        x_min, x_max = boundaries_x[y]
        if y < y_min or y > y_max or x < x_min or x > x_max:
            return False
    return True

def valid_rectangle(tile1, tile2):
    x1, y1 = tile1
    x2, y2 = tile2
    sgn_x = 1 if x2 > x1 else -1
    sgn_y = 1 if y2 > y1 else -1

    ray1 = []
    ray2 = []
    ray3 = []
    ray4 = []

    for xm in range(x1, x2 + sgn_x, sgn_x):
        ray1.append((xm, y1))
        ray2.append((xm, y2))
    
    for ym in range(y1, y2 + sgn_y, sgn_y):
        ray3.append((x1, ym))
        ray4.append((x2, ym))
    
    rays = [ray1, ray2, ray3, ray4]
    for ray in rays:
        if not valid_ray(ray):
            return False
    return True

M = 0
arg = None
for tile1, tile2 in list(itertools.combinations(red_tiles, 2)):
    print(tile1)
    if not valid_rectangle(tile1, tile2):
        continue
    area = get_area(tile1, tile2)
    M = max(M, area)

print(M)