FILE_NAME = input("Filename : ")

with open(FILE_NAME) as file:
    data = (lambda x: [dict(zip(x[0].split(','), tuple(map(int, row.split(',')))))
            for row in x[1:]])(file.read().splitlines())
    data = sorted(data, key=lambda x: x['No'])

tee = {
    8: 75000,
    4: 30000,
    1: 5000,
    float("-inf"): 1000,
}

gayray, gayray_list = False, []
for row in data:
    for key, val in tee.items():
        if row['Height'] > key:
            if row['Cost'] > val:
                if not gayray:
                    gayray = True
                gayray_list.append(str(row['No']))
            break
prtstring = '\n'.join(gayray_list) if gayray else None
print(f"Yes\n{prtstring}") if gayray else print("No")
