with open('inp.txt', 'r') as f:
    l1, l2 = f.read().split('\n\n')

fresh = []
for r in l1.split('\n'):
    n1, n2 = map(int, r.split('-'))
    fresh.append((n1, n2))

ids = []
for r in l2.split('\n'):
    ids.append(int(r))

def is_in(n):
    for (n1, n2) in fresh:
        if n1 <= n and n <= n2:
            return True
    return False

num_fresh = 0
for id in ids:
    num_fresh += is_in(id)

print(num_fresh)
