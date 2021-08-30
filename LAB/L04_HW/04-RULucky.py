inp = input()
if inp[1] == "8":
    inp = [x for x in inp]
    exp = sum(map(int,inp))
    if exp%13 == 0 and exp<56:
        lux = "bad" 
    else: lux = "good"
elif inp[1] == "9":
    badnums = list(map(str,[20,13,18,80,31,93]))
    for badnum in badnums:
        if badnum in inp:
            lux = "bad" 
            break
        elif badnum == badnums[-1]:
            lux = "good" 
            break
print(f"Have {lux} luck.")
            
