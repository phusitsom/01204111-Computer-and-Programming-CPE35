print("\n".join((lambda inp: [inp[:i] + inp[i].upper() + inp[i+1:] for i in range(len(inp))])(input("Input name: "))))
