n = input()
code4 = int(n[3] + n[10] + n[17] + n[24] + n[31])
code8 = int(n[7] + n[12] + n[17] + n[22] + n[27])
code5 = code4 + code8 + 10000
code3 = str(code5)[-4:-1]
code = int(code3[0]) + int(code3[1]) + int(code3[2])
codex = (code % 10)+1
ch = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
print(code3+ch[codex-1])
