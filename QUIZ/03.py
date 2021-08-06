string = input('Enter a sentence or pharse and then press ENTER\n').strip()
typ = int(input('Enter output type (only 1..5:) '))

n = int(len(string)**0.5)+1
prtlist = [string[i:i+n] for i in range(0,n**2,n)]

for i, item in enumerate(prtlist):
    if len(item) != n:
        item += ("*"*(n-len(item)))
        prtlist[i] = item
if typ == 1: None
elif typ == 2:
    prtlist = ["".join(tup) for tup in list(zip(*prtlist))]
elif typ == 3:
    prtlist = [st[::-1] for st in prtlist][::-1]
elif typ == 4:
    prtlist = ["".join(tup) for tup in list(zip(*[st[::-1] for st in prtlist][::-1]))]

print("   " + "  ".join(list(map(str,range(1,n+1)))))
for i, w in enumerate(prtlist):
    print(" " + str(i+1) + " " + "  ".join(prtlist[i]))