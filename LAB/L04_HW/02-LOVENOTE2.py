inp = input("Input name: ")
for i in range(len(inp)):
    print(
        f"{inp.replace(inp[i], inp[i].upper())} {inp[::-1].replace(inp[::-1][i], inp[::-1][i].upper())}")
