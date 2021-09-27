union = lambda a,b: sorted(list(set(a+b)))
print(f'A union B:', union(*[list(map(int, input(f'Input set {e}: ').split())) for e in ('A','B')]))