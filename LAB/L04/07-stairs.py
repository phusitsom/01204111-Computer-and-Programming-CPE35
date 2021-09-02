def draw(m):
    for it, letter in enumerate(m):
        print(letter*(it+1))


while True:
    inp = input()
    if inp[0] == "0":
        print("Good Bye.")
        break
    else:
        draw(inp.split())
