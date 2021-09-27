w = {}
for a in range(int(input("Input number of words: "))):
    inp = input()
    if inp[0] not in w:
        w.update({inp[0]: [1, [inp]]})
    else:
        w[inp[0]][0] += 1
        w[inp[0]][1].append(inp)
mxs = max(w, key=w.get)
words = "\n".join(w[mxs][1])
print(
    f"The popular character is {mxs}.\nThe character is used in {w[mxs][0]} words.\n{words}")
