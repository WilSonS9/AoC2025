with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

tiles = set()

for r in l:
    x, y = map(int, r.split(','))
    tiles.add((x, y))

def get_area(tile1, tile2):
    dx = abs(tile1[0] - tile2[0]) + 1
    dy = abs(tile1[1] - tile2[1]) + 1
    return dx * dy

M = 0
arg = None
for tile1 in tiles:
    for tile2 in tiles:
        area = get_area(tile1, tile2)
        M = max(M, area)

print(M)
