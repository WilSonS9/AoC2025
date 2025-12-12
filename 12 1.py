with open('inp.txt', 'r') as f:
    l = f.read().split('\n\n')

shapes_s = l[:-1]
regions_s = l[-1]

shapes = []
regions = []

for s in shapes_s:
    shape = []
    for i, r in enumerate(s.split('\n')[1:]):
        for j, c in enumerate(r):
            if c == '#':
                shape.append((i, j))
    shapes.append(tuple(shape))

for r in regions_s.split('\n'):
    size_s, reqs_s = r.split(': ')
    size_x, size_y = map(int, size_s.split('x'))
    reqs = list(map(int, reqs_s.split(' ')))
    regions.append((size_x, size_y, reqs))

def area(shape):
    return len(shape)

n_valid_regions = 0
for (size_x, size_y, reqs) in regions:
    region_area = size_x * size_y
    n_presents = sum(reqs)
    min_area = sum([n * area(shapes[i]) for i, n in enumerate(reqs)])

    if region_area >= 9 * n_presents: # each present can have its own 3x3 grid, no need to worry about overlaps
        n_valid_regions += 1
    elif region_area < min_area: # implies that any packing of our presents into our region contains overlaps, not allowed!
        continue
    else: # no special cases in input!
        print('special case, needs further investigation....')

print(n_valid_regions)
