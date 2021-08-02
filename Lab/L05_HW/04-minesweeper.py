from itertools import chain;a = ((lambda x,y: [[0 for y in range(y)] for x in range(x)])(*map(int,input("Grid Size: ").split())))
for i, j in [map(int, input(f"Mine#{i+1}: ").split()) for i in range(int(input("Number of mine(s): ")))]:a[i][j] = "X"
for ls in a:ls.insert(0,0);ls.insert(len(ls),0)
lst0 = [0 for i in range(len(a[0]))];a.insert(0,lst0);a.insert(len(a),lst0)
for k, j in list(chain(*[(lambda i, x : [(i,j) for j in range(len(x)) if x[j] == "X"])(i,x) for i, x in enumerate(a) if "X" in x])):
    for e in range(k-1,k+2):
        a[e][j-1:j+2] = [list(map(lambda x: "X" if x == "X" else x+1,i)) if "X" in i else list(map(lambda x: x+1,i)) for i in [a[e][j-1:j+2]]][0]
print("\n".join([" ".join(subans) for subans in  list(zip(*[map(str,sublst) for sublst in [ x[1:-1] for x in a[1:-1]]]))]))