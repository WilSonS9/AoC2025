from functools import cache

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

machines = []

for r in l:
    strings = r.split(' ')
    machine_requirements = tuple(map(lambda c: c == '#', strings[0][1:-1]))
    buttons = []
    for button_s in strings[1:-1]:
        indices = tuple(map(int, button_s[1:-1].split(',')))
        buttons.append(indices)
    machines.append((machine_requirements, buttons))

@cache
def press_button(state, button):
    new_state = tuple(map(lambda p: not p[1] if p[0] in button else p[1], enumerate(state)))
    return new_state

n_presses_machine = []
for (goal, buttons) in machines:
    initial_state = tuple([False for _ in goal])
    visited = set()
    q = [(initial_state, 0)]
    while True:
        state, n_presses = q.pop(0)
        if state in visited:
            continue
        elif state == goal:
            n_presses_machine.append(n_presses)
            break
        visited.add(state)
        for button in buttons:
            next_state = press_button(state, button)
            q.append((next_state, n_presses + 1))

print(sum(n_presses_machine))
