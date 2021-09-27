dik = {}
for n in range(int(input("Number of inputs: "))):
    (lambda name, score: dik.update({name: score}))(*input().split())
while True:
    inp = input("student: ")
    if inp in dik:
        print(f"{inp}'s score is {dik[inp]}")
    else:
        print('End')
        break
