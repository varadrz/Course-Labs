from itertools import product

def generate_strings(alphabet, max_length):
    all_strings = []
    for n in range(max_length + 1):
        for p in product(alphabet, repeat=n):
            all_strings.append(''.join(p) if p else 'ε')  # Use ε for the empty string
    return all_strings


alphabet = ['0', '1']
max_length = 3
result = generate_strings(alphabet, max_length)

print("Generated strings over Σ = {0,1} of length ≤ 3:")
for s in result:
    print(s)
