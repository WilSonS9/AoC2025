from math import floor, ceil

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

cur = 50
n_times = 0
for i in l:
    new = cur
    if i[0] == 'R':
        new += int(i[1:])
    else:
        new -= int(i[1:])

    diff = new - cur
    op = floor if new > 0 else ceil # to properly count the number of completed windings
    n_times += abs(op(new / 100) - op(cur / 100))
    cur = new % 100

print(n_times)