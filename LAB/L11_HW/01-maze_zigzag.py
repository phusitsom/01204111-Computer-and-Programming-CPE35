def generate_zigzag(n):
    _range, _blank_list = range(n), [[None for __ in range(n)] for _ in range(n)]
    for n, (x,y) in enumerate(sorted(((x, y) for x in _range for y in _range),key= lambda v: (sum(v), -v[1] if sum(v)%2 else v[1]))):
        _blank_list[x][y] = n+1
    return list(zip(*list(zip(*list(zip(*_blank_list[::-1]))[::-1]))[::-1]))
for x in generate_zigzag(int(input())):
    for y in x: print(f'{y:3.0f}',end=' ')
    print()