r, c = sorted([int(input(f"{t}: ")) for t in ['R', 'C']])
print(r * (r + 1) * (3 * c - r + 1) // 6)