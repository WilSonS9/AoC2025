from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

h = len(l)
w = len(l[0])

columns = []

prev_col = -1 # where the last column ended
for j in range(w):
    col_chars = [l[i][j] for i in range(h)]
    if all(map(lambda c: c == ' ', col_chars)):
        column = [l[i][prev_col+1:j] for i in range(h)]
        columns.append(column)
        prev_col = j

# add final column
column = [l[i][prev_col+1:w] for i in range(h)]
columns.append(column)

ops = [column[-1].rstrip() for column in columns]

def filter(c):
    return '' if c == ' ' else c

results = []
for column, op in zip(columns, ops):
    nums = column[:-1]
    nums_w = len(nums[0])

    # each column consists of `nums_w` columns of characters
    # for each such column, concatenate the characters in that column top-to-bottom, filtering out whitespace characters
    strings_ceph = [''.join([filter(num[j]) for num in nums]) for j in range(nums_w)]
    nums_ceph = list(map(int, strings_ceph))

    if op == '+':
        results.append(sum(nums_ceph))
    else:
        results.append(reduce(lambda a, b: a * b, nums_ceph))

print(sum(results))
