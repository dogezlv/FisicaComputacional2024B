def simple_cellular_automaton(rules, initial_state, generations):
    current_state = initial_state
    print("Generation 0:", ''.join(map(str, current_state)))

    for generation in range(1, generations + 1):
        new_state = []
        for i in range(len(current_state)):
            left = current_state[i - 1] if i > 0 else current_state[-1]
            current = current_state[i]
            right = current_state[i + 1] if i < len(current_state) - 1 else current_state[0]
            new_state.append(rules[(left, current, right)])
        current_state = new_state
        print(f"Generation {generation}:", ''.join(map(str, current_state)))

rules = {
    (0, 0, 0): 0,
    (0, 0, 1): 1,
    (0, 1, 0): 1,
    (0, 1, 1): 1,
    (1, 0, 0): 0,
    (1, 0, 1): 1,
    (1, 1, 0): 1,
    (1, 1, 1): 0
}
initial_state = [0, 1, 0, 1, 1, 0, 0, 1]
generations = 10
simple_cellular_automaton(rules, initial_state, generations)
