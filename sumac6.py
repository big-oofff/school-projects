from itertools import permutations

def is_one_lump_sequence(seq):
    n = len(seq)
    if sorted(seq) != list(range(1, n + 1)):
        return False  # Must be a permutation of 1 to n
    
    peak_found = False
    peak_index = -1
    for i in range(1, n - 1):
        if seq[i - 1] < seq[i] > seq[i + 1]:
            peak_found = True
            peak_index = i
        elif peak_found and seq[i] < seq[i + 1]:
            return False  # Sequence must not increase again after peak
    
    return peak_found and seq[0] < seq[1] and peak_index != -1  # Ensure initial increase and valid peak

def is_snake(pairs, n):
    adjacency = {i: set() for i in range(1, n + 1)}
    for a, b in pairs:
        adjacency[a].add(b)
        adjacency[b].add(a)
    
    visited = set()
    start = pairs[0][0]
    current = start
    
    for _ in range(n):
        if current in visited:
            return False
        visited.add(current)
        next_nodes = [node for node in adjacency[current] if node not in visited]
        if not next_nodes:
            return len(visited) == n
        current = next_nodes[0]
    
    return len(visited) == n

def find_one_lump_snakes(n):
    valid_snakes = []
    for seq in permutations(range(1, n + 1)):
        if not is_one_lump_sequence(seq):
            continue
        pairs = [(i + 1, seq[i]) for i in range(n)]
        if is_snake(pairs, n):
            valid_snakes.append(pairs)
    
    return valid_snakes

# Find one-lump snakes for n = 4 to 11
for n in range(4, 11):
    snakes = find_one_lump_snakes(n)
    print(f"One-lump snakes for n={n} (Total: {len(snakes)}):")
    for snake in snakes:
        print(snake)
    print()
