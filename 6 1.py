from functools import reduce

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

problem_matrix = []
ops = []
for r in l:
    elems = r.split()
    if elems[0] in ['+', '*']:
        ops = elems
    else:
        problem_matrix.append(list(map(int, elems)))

h = len(problem_matrix)
w = len(problem_matrix[0])

results = []
for i in range(w):
    op = ops[i]
    nums = [problem_matrix[j][i] for j in range(h)]
    if op == '+':
        results.append(sum(nums))
    else:
        results.append(reduce(lambda a, b: a * b, nums))

print(sum(results))
