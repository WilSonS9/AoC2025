with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

m = {}

for i, r in enumerate(l):
    for j, c in enumerate(r):
        m[(i, j)] = c

def count_adjacents(m, i, j):
    count = 0
    for di in range(-1, 2):
        for dj in range(-1, 2):
            if di == 0 and dj == 0:
                continue
            new_i, new_j = i + di, j + dj
            if new_i < 0 or new_i >= h or new_j < 0 or new_j >= w:
                continue
            count += m[(new_i, new_j)] == '@'
    return count

num_reachable = 0
for i in range(h):
    for j in range(w):
        num_reachable += m[(i, j)] == '@' and count_adjacents(m, i, j) < 4

print(num_reachable)