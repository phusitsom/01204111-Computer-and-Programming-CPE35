date = input()
d = date.split("/")
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print(month[int(d[1])-1], d[0] + ",", d[2])