inp = input("Input: ")
if len(inp.split()) != 2:
    string = ", ".join(inp.split()).split()
else: 
    string = inp.split()
if len(inp.split()) > 1:
    string[-1] = "and "+string[-1]
print(" ".join(string))