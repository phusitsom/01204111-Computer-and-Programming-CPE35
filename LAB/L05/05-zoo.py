dik = {}
for n in range(int(input("How many animals are there in the zoo? : "))):
    (lambda name, score: dik.update({name: score}))(*input().split())
for n in range(int(input("How many questions do you want to ask? : "))):
    (lambda x: print(dik[x]) if x in dik else print(
        "Sorry we don't have that animal."))(input())
