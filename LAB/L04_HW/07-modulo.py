print(len(set(list(map(lambda n, m: [int(input(f'Input number {i+1}: ')) % m for i in range(n)], [int(input('N: '))], [int(input('M: '))]))[0])))
