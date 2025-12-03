with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def get_max_right(s, i):
    s_right = s[i+1:]
    return max(map(int, s_right))

joltages = []

for r in l:
    M = 0
    for i, c in enumerate(r[:-1]):
        d1 = c
        d2 = get_max_right(r, i)
        val = int(f'{d1}{d2}')
        M = max(M, val)
    joltages.append(M)

print(sum(joltages))