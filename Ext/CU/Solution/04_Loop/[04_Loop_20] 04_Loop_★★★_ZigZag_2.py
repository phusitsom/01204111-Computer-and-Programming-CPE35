n = input()
count = 0
while n != 'Zig-Zag' and n != 'Zag-Zig':
    if count == 0:
        a, b = [int(e) for e in n.split()]
        count += 1
        min1 = a
        max1 = a
        min2 = b
        max2 = b
    else:
        if count % 2 == 0:
            a, b = [int(e) for e in n.split()]
            count += 1
        else:
            b, a = [int(e) for e in n.split()]
            count += 1
    min1 = min(min1, a)
    max1 = max(max1, a)
    min2 = min(min2, b)
    max2 = max(max2, b)
    n = input()
if n == 'Zig-Zag':
    print(min1, max2)
else:
    print(min2, max1)