LIST = list(map(int, input().split()))
while(True):
    cmd_name, value = input().split()
    value = int(value)
    if cmd_name == "A":
        LIST.append(value)
    elif cmd_name == "S":
        print(LIST[value])
    elif cmd_name == "R":
        LIST.pop(value)
    elif cmd_name == "E":
        print(' '.join(map(str, LIST)))
        break
