FILE_NAME, data = input("File name: "), {}
with open(FILE_NAME) as file:
    lines = list(map(lambda x: x.split(), file.read().splitlines()))

for item in lines:
    key = item[0]
    vals = list(map(int, item[1:]))

    vals.pop(vals.index(max(vals)))
    vals.pop(vals.index((min(vals))))

    data.update({key: sum(vals)})
max_score = max(data.values())

print(max_score)
for name, score in data.items():
    print(name) if score == max_score else None
