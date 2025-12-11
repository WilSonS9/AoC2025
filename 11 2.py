from collections import defaultdict
from functools import cache

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

svr = 'svr'
fft = 'fft'
dac = 'dac'
out = 'out'

G = defaultdict(list)
for r in l:
    node, neighbours_s = r.split(': ')
    neighbours = neighbours_s.split(' ')
    G[node] = neighbours


@cache
def n_paths(src, trg, ignore):
    if src == trg:
        return 1
    s = 0
    for node in G[src]:
        if not node == ignore:
            s += n_paths(node, trg, ignore)
    return s

o1s1 = n_paths(svr, fft, dac)
o1s2 = n_paths(fft, dac, out)
o1s3 = n_paths(dac, out, fft)

o2s1 = n_paths(svr, dac, fft)
o2s2 = n_paths(dac, fft, out)
o2s3 = n_paths(fft, out, dac)

n_valid_paths = o1s1 * o1s2 * o1s3 + o2s1 * o2s2 * o2s3
print(n_valid_paths)
