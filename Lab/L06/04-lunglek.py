N, M = int(input("N = ")), int(input("M = "))
L = [int(input(f"cost of day {i+1} = ")) for i in range(N)]
print(f"Min cost of {M} days = {min(list(map(sum,[tuple(L[i:i+M]) for i in range(N-M+1)])))}")