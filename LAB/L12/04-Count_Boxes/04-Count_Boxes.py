threshold = ((1,(15, 10, 8)), (2, (25, 15, 12)), (3, (40, 50, 20)))
count = [None, 0, 0 ,0]
for n in range(1,int(input("N: "))+1):
    inp = [int(input(f"Order {n} {_t}: ")) for _t in ('A', 'B', 'C')]
    
    for box in threshold:
        if all([inp[i]<=box[1][i] for i in range(3)]):
            print(f"Box size {box[0]}")
            count[box[0]] += 1
            break
    else: print("Oversize product")

for i in range(1,4): print(f"Use Box size {i}: {count[i]}")