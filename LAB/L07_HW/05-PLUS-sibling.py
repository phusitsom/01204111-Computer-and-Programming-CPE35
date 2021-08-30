parentData = {}

n = int(input())

for _ in range(n):
    inp = input()
    splittedInput = inp.split()

    subject = splittedInput[0]
    relation = splittedInput[2]
    object = splittedInput[-1]

    if relation in ['mother', 'father']:

        if object not in parentData:
            parentData.setdefault(object, [])

        parentData[object].append(subject)

inp = input()
splittedInput = inp.split()

object1, object2 = splittedInput[1], splittedInput[3]
parent1, parent2 = parentData.get(object1), parentData.get(object2)

isSib = False

if parent1 is not None and parent2 is not None:
    for p in parent1:
        if p in parent2:
            isSib = True
            break

if isSib:
    print("Yes")
else:
    print("No")
