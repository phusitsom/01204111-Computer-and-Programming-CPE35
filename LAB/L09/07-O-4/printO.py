
def showO(inp):
    e = -(-inp//2)

    prtstr = ''
    
    for i in range(e):
        space = (e-i-1)
        prtstr += " "*space+("O"*(i+1))+"O"*i+" "*space
        prtstr += "\n"
    for i in range(e-2,-1,-1):
        space = (e-i-1)
        prtstr += " "*space+("O"*(i+1))+"O"*i+" "*space
        prtstr += "\n"
        
    for i in range(inp):
        for j in zip(*prtstr.splitlines()*inp):
            print(''.join(j))