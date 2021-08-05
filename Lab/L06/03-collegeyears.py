data = []
while True:
    id = int(input("Student ID : "))
    if id == 0:break
    data.append((id, int(input("years : "))))
sepyr = int(input("Separate year: "))
for id, yr in data:
    if yr >= sepyr: print(id)