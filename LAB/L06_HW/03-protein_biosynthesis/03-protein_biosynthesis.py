print(f"""{int(len((lambda x: x[:x.index([aa for aa in [x[i*3:(i+1)*3] for i in range(-(-len(x)//3))] if aa in ['ATT','ACT','ATC']][0])])((lambda x: x[x.index("TAC"):])(input("DNA: "))))/3)} Amino acid(s)""")