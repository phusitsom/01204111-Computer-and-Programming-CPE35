inp = int(input('N = '))
daylst = [int(input(f"cost of day {i} = ")) for i in range(1, inp+1)]
sumlst = []
for i in range(len(daylst)-2):
    try:
        sumlst.append(sum(daylst[i:i+3]))
    except:
        break
print(f"Min cost of 3 days = {min(sumlst)}")
