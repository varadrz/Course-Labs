from itertools import product

def generate_binary_tree_visual(alphabet, max_length):
    levels = []

    # Generate strings grouped by length
    for n in range(max_length + 1):
        level = []
        for p in product(alphabet, repeat=n):
            level.append(''.join(p) if p else 'ε')
        levels.append(level)

    # Width for spacing calculation
    max_width = 2 ** max_length * 2

    for i, level in enumerate(levels):
        num_nodes = len(level)
        space_between = max_width // (num_nodes + 1)

        # Print the nodes
        line = ''
        for val in level:
            line += val.center(space_between)
        print(line.center(max_width))

        # Print connecting lines if not last level
        if i < len(levels) - 1:
            connector_line = ''
            for _ in range(num_nodes):
                connector_line += '/ \\'.center(space_between)
            print(connector_line.center(max_width))

# Usage
alphabet = ['0', '1']
max_length = 3
generate_binary_tree_visual(alphabet, max_length)
