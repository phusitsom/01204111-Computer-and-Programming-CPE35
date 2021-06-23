code = {'2': 'a', '22': 'b', '222': 'c', '3': 'd', '33': 'e', '333': 'f', '4': 'g', '44': 'h', '444': 'i', '5': 'j',
        '55': 'k', '555': 'l', '6': 'm', '66': 'n', '666': 'o', '7': 'p', '77': 'q', '777': 'r', '7777': 's', '8': 't',
        '88': 'u', '888': 'v', '9': 'w', '99': 'x', '999': 'y', '9999': 'z', '0': ' '}
char = {}
for key in code:
    char[code[key]] = key


def text2keys(text):
    text = text.lower()
    s = ''
    for i in range(len(text)):
        if text[i] in char:
            s += char[text[i]]
            s += ' '
    return s


def keys2text(keys):
    k = keys.split()
    s = ''
    for i in range(len(k)):
        if k[i] in code:
            s += code[k[i]]
    return s


exec(input().strip())