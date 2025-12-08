from collections import defaultdict

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

start = (0, l[0].index('S'))

splitter_coords = set()
for i, r in enumerate(l):
    for j, c in enumerate(r):
        if c == '^':
            splitter_coords.add((i, j))

tachyons = defaultdict(int)
tachyons[start] = 1

def iterate_tachyon(coords):
    row, col = coords
    new_row = row + 1

    if (new_row, col) in splitter_coords:
        new_coordss = [(new_row, col - 1), (new_row, col + 1)]
    else:
        new_coordss = [(new_row, col)]
    return new_coordss


for _ in range(h):
    new_tachyons = defaultdict(int)
    for coords in tachyons:
        mult = tachyons[coords]
        new_coordss = iterate_tachyon(coords)
        for coords in new_coordss:
            new_tachyons[coords] += mult
    tachyons = new_tachyons

n_timelines = 0
for mult in tachyons.values():
    n_timelines += mult

print(n_timelines)