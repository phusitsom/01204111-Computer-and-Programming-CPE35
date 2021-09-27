N = 10


def Nplus(v):
    global N
    N += v


def Nminus(v):
    global N
    N -= v


def Ntimes(v):
    global N
    N *= v


def Ndivided(v):
    global N
    N /= v


Nplus(5)
Nminus(3)
Ntimes(6)
Ndivided(3)
print(f'{N:.0f}')

c = input()
if c == '1':
    Nplus(12)
    print(f'{N:.0f}')
if c == '2':
    Nminus(6)
    print(f'{N:.0f}')
if c == '3':
    Ntimes(2)
    print(f'{N:.0f}')
if c == '4':
    Ndivided(6)
    print(f'{N:.0f}')
