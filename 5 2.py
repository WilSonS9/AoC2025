with open('inp.txt', 'r') as f:
    l1, l2 = f.read().split('\n\n')

def add_to_fresh(n1, n2, fresh, indent=0):
    ''' Main idea: Assume `fresh` consists of disjoint intervals

    To add an interval disjoint from the rest of `fresh`, just append `(n1, n2)`

    Otherwise, take the first interval *I* in `fresh` which intersects `(n1, n2)` and compute their union, which will be some new interval `(m1, m2)`.
    Then, replace `(n1, n2)` and *I* with `(m1, m2)` and add it recursively to the list of all other intervals
    '''

    # print(f'{indent * "  "}adding {(n1, n2)} to {fresh}')

    is_disjoint = True
    for (l, h) in fresh:
        # (n1, n2) disjoint from all (l, h)
        if n2 < l or n1 > h:
            continue
        is_disjoint = False
        break

    if is_disjoint:
        # print(f'{indent * "  "}disjoint interval {(n1, n2)}')
        new_fresh = fresh + [(n1, n2)]
        return new_fresh
    
    new_fresh = []

    for (l, h) in fresh:
        # (l --- n1 --- n2 --- h)
        if l <= n1 <= n2 <= h:
            # print(f'{indent * "  "}trivial intersection {(n1, n2)} with {(l, h)}')
            n1 = l
            n2 = h
            # new_interval = (l, h), already in fresh
            return fresh

        intersect = False

        # ( n1 --- l --- n2 --- h )
        if n1 <= l <= n2 <= h:
            intersect = True
            # print(f'{indent * "  "}case 1 intersecting {(n1, n2)} with {(l, h)}')
            # new_interval = (n1, h)
            n1 = n1
            n2 = h
        # ( n1 --- l --- h --- n2 )
        elif n1 <= l <= h <= n2:
            intersect = True
            # print(f'{indent * "  "}case 2 intersecting {(n1, n2)} with {(l, h)}')
            # new_interval = (n1, n2)
            n1 = n1
            n2 = n2
        # (l --- n1 --- h --- n2)
        elif l <= n1 <= h <= n2:
            intersect = True
            # print(f'{indent * "  "}case 3 intersecting {(n1, n2)} with {(l, h)}')
            # new_interval = (l, n2)
            n1 = l
            n2 = n2
        else:
            # print(f'{indent * "  "}no intersecting {(n1, n2)} with {(l, h)}')
            new_fresh.append((l, h))

        # since (n1, n2) is not disjoint from fresh, it must intersect some existing interval
        if intersect:
            new_fresh = add_to_fresh(n1, n2, new_fresh, indent+1)

    return new_fresh

fresh = []
for r in l1.split('\n'):
    n1, n2 = map(int, r.split('-'))
    fresh = add_to_fresh(n1, n2, fresh)

num_ids = 0
for (n1, n2) in fresh:
    num_ids += n2 - n1 + 1

print(num_ids)
