with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

def get_max_str(s, n=12):
    if n == 0:
        return ''
    valid_digits = s if n == 1 else s[:-(n-1)] # need to have at least n-1 digits to the right

    max_val = max(map(int, valid_digits))
    i = valid_digits.index(str(max_val))

    return f'{max_val}' + get_max_str(s[i+1:], n-1)

joltages = []

for r in l:
    M = int(get_max_str(r))
    joltages.append(M)

print(sum(joltages))