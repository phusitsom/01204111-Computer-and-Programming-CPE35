print(" ".join((lambda inp: (lambda string: string[:-1] + ["and "+string[-1]] if len(inp.split()) > 1 else string)(
    ", ".join(inp.split()).split() if len(inp.split()) != 2 else inp.split()))(input("Input: "))))
