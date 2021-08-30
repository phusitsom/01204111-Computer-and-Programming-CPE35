dik = {}
for n in range(int(input("Number of inputs: "))):
    name = input("Input name: ")
    score = float(input("Input score: "))
    if score is None: pass
    try: dik.update({name:[score]}) if name not in dik else dik.update({name:(dik[name] + [score])})
    except: pass
for key in dik:dik[key] = sum(dik[key])/(len(dik[key]))
val_list = [x for x in dik.values()]
maxitem = [x for x in dik.items()][val_list.index(max(val_list))]
print(f"Top score is {maxitem[0]}: {maxitem[1]:.2f}")
