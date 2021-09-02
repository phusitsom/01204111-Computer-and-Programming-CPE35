ew, arrow, stick = int(input()), input('Arrow : '), input('Stick : ')
for i in range(ew):
    print(' ' * (ew - (i + 1)), arrow * (2*i+1))
for i in range(ew):
    print(' ' * (ew-1), stick)
