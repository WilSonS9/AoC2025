with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

cur = 50
n_times = 0
for i in l:
    if i[0] == 'R':
        cur += int(i[1:])
    else:
        cur -= int(i[1:])
    cur = cur % 100
    n_times += int(cur == 0)

print(n_times)