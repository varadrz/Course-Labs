def print_binary_tree(result, max_length):
    levels = []
    index = 0
    for i in range(max_length + 1):
        level_size = 2 ** i if i != 0 else 1
        levels.append(result[index: index + level_size])
        index += level_size

    width = 80  # Adjust this for spacing

    for i, level in enumerate(levels):
        spacing = width // (2 ** (i + 1))
        line = ''
        for val in level:
            line += val.center(spacing * 2)
        print(line.center(width))

        # Connector lines (except after last level)
        if i < max_length:
            connectors = ''
            for _ in range(len(level)):
                connectors += '/ \\'.center(spacing * 2)
            print(connectors.center(width))
