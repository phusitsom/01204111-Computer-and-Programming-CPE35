(lambda LNM: print(f"Min cost of {LNM[2]} days = {min(list(map(sum,[tuple(LNM[0][i:i+LNM[2]]) for i in range(LNM[1]-LNM[2]+1)])))}"))(
    (lambda N, M: ([int(input(f"cost of day {i+1} = ")) for i in range(N)], N, M))(int(input("N = ")), int(input("M = "))))
