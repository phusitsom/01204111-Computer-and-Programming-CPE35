import re
with open(input('File name: ')) as file:
    fr = file.read()

regex_lego = r"[^0-9\n]+[\n]+[^0-9]+|[^0-9\n]+[^0-9]+"
regex_order = r"[0-9]"

lego = re.findall(regex_lego, fr)
order = re.findall(regex_order, fr)

gen = list((int(i), j) for i, j in zip(order, lego))

gen = sorted(gen, key=lambda x: x[0])

print("".join([l[1] for l in gen]))
