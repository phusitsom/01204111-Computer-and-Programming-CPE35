n = int(input())
first_name = ["Robert", "William", "James", "John", "Margaret", "Edward", "Sarah", "Andrew", "Anthony", "Deborah"]
nick_name = ["Dick", "Bill", "Jim", "Jack", "Peggy", "Ed", "Sally", "Andy", "Tony", "Debbie"]
name = []
for i in range(n):
    x = input()
    if x in first_name:
        for j in range(len(first_name)):
            if first_name[j] == x:
                name.append(nick_name[j])
    elif x in nick_name:
        for j in range(len(nick_name)):
            if nick_name[j] == x:
                name.append(first_name[j])
    else: name.append('Not found')
for i in range(len(name)):
    print(name[i])