with open('inp.txt', 'r') as f:
    l = f.read().split(',')

def is_repeat(x):
    s = str(x)
    if len(s) % 2 == 1:  # is it even possible to split x into 2 equal chunks?
        return False
    else:
        l2 = len(s) // 2
        return s[:l2] == s[l2:]

ids = []

for r in l:
    i1, i2 = map(int, r.split('-'))
    for x in range(i1, i2+1):
        if is_repeat(x):
            ids.append(int(x))

print(sum(ids))