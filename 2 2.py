from primefac import primefac

with open('inp.txt', 'r') as f:
    l = f.read().split(',')

def is_n_repeat(n, s):
    'check if s is an `n`-repeat (can be split into `n` equal chunks)'
    chunk_length = len(s) // n
    test = s[:chunk_length] # compare each successive chunk with this test string
    for m in range(1, n):
        if s[m * chunk_length : (m+1) * chunk_length] != test:
            return False
    return True

ids = []

for r in l:
    i1, i2 = map(int, r.split('-'))
    for x in range(i1, i2+1):
        s = str(x)
        # only need to check chunk numbers n equal to prime factors of the string length
        # if n is not a divisor of the length of s, then s will not split into n chunks
        # otherwise, if n = n_1 * n_2 (n_1, n_2 > 1) is a compound divisor of the string length, it has to be either an n_1-repeat or an n_2-repeat
        # repeat this argument on n_1 and n_2 and we get that we only need to check the prime factors of the length of s
        for n in primefac(len(s)):
            if is_n_repeat(n, s):
                ids.append(int(x))
                break

print(sum(ids))