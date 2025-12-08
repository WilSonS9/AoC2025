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

tachyons = set()
tachyons.add(start)

n_splits = 0

def iterate_tachyon(coords):
    global n_splits

    row, col = coords
    new_row = row + 1

    if (new_row, col) in splitter_coords:
        new_coordss = [(new_row, col - 1), (new_row, col + 1)]
        n_splits += 1
    else:
        new_coordss = [(new_row, col)]
    return new_coordss


for _ in range(h):
    new_tachyons = set()
    for coords in tachyons:
        new_coordss = iterate_tachyon(coords)
        for coords in new_coordss:
            new_tachyons.add(coords)
    tachyons = new_tachyons

print(n_splits)