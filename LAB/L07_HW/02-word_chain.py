sp = input("Text: ").split()
word = []
leni = []
st_i = 0
for i, e in enumerate(sp):
    try:
        leni.append(len([l for _i, l in enumerate(e) if l != sp[i+1][_i]]))
    except:
        continue
for i, l in enumerate(leni):
    if l > 2:
        word.append(sp[st_i:i+1])
        sp = sp[i+1:]
        st_i = i
word.append(sp)
print(
    f"{len(word)} Chain(s). Maximum length is {max([len(i) for i in word])} word(s).")
