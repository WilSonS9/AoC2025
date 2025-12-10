import pyomo.environ as pyo

with open('inp.txt', 'r') as f:
    l = f.read().split('\n')

machines = []

for r in l:
    strings = r.split(' ')
    machine_requirements = tuple(map(int, strings[-1][1:-1].split(',')))
    buttons = []
    for button_s in strings[1:-1]:
        indices = tuple(map(int, button_s[1:-1].split(',')))
        vector = [1 if i in indices else 0 for i in range(len(machine_requirements))]
        buttons.append(vector)
    machines.append((machine_requirements, buttons))

n_presses_machine = []
for i, (goal, buttons) in enumerate(machines):
    print(f'servicing machine {i+1} / {len(machines)}...')
    n_buttons = len(buttons)

    model = pyo.ConcreteModel()
    model.x = pyo.Var(list(range(len(buttons))), domain=pyo.NonNegativeIntegers)
    model.OBJ = pyo.Objective(expr = sum([model.x[i] for i in range(n_buttons)]))
    model.goal_constraints = pyo.ConstraintList()

    for i in range(len(goal)):
        model.goal_constraints.add(expr = sum([model.x[j] * buttons[j][i] for j in range(n_buttons)]) == goal[i])

    solver = pyo.SolverFactory('glpk')
    result = solver.solve(model)
    n_presses = int(pyo.value(model.OBJ))
    n_presses_machine.append(n_presses)

print(sum(n_presses_machine))
