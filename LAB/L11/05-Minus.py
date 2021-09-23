def minus(a,b):
    _result = [i for i in a if i not in b]
    return sorted(_result) if _result != [] else 'empty set'
print(f'A minus B:', minus(*[list(map(int, input(f'Input set {e}: ').split())) for e in ('A','B')]))