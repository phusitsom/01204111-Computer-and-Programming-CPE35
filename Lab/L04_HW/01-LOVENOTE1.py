inp = input("Input name: ")
for i in range(len(inp)):
    print(inp[:i] + inp[i].upper() + inp[i+1:])