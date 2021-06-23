def no_lowercase(t):
    for i in range(len(t)):
        if 'a' <= t[i] <= 'z':
            return False
    return True


def no_uppercase(t):
    for i in range(len(t)):
        if 'A' <= t[i] <= 'Z':
            return False
    return True


def no_number(t):
    for i in range(len(t)):
        if '0' <= t[i] <= '9':
            return False
    return True


def no_symbol(t):
    for i in range(len(t)):
        if t[i] in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '~', '`', ',', '"', "'", ':',
                    ']', '[', '?', '/', ';', ':', '{', '}']:
            return False
    return True


def character_repetition(t):
    for i in range(len(t) - 3):
        if t[i] == t[i + 1] == t[i + 2] == t[i + 3]:
            return True
    return False


def number_sequence(t):
    n = '0123456789'
    for i in range(len(t) - 3):
        if t[i] in n and t[i + 1] in n and t[i + 2] in n and t[i + 3] in n:
            if (int(t[i]) + 3) % 10 == (int(t[i + 1]) + 2) % 10 == (int(t[i + 2]) + 1) % 10 == (int(t[i + 3])) % 10:
                return True
            if (int(t[i])) % 10 == (int(t[i + 1]) + 1) % 10 == (int(t[i + 2]) + 2) % 10 == (int(t[i + 3]) + 3) % 10:
                return True
    return False


def letter_sequence(t):
    k = t.upper()
    for i in range(len(k) - 3):
        if 65 <= ord(k[i]) <= 65 + 26:
            if (ord(k[i]) + 0) % 65 == (ord(k[i + 1]) + 1) % 65 == (ord(k[i + 2]) + 2) % 65 == (ord(k[i + 3]) + 3) % 65:
                return True
            if (ord(k[i]) + 3) % 65 == (ord(k[i + 1]) + 2) % 65 == (ord(k[i + 2]) + 1) % 65 == (ord(k[i + 3]) + 0) % 65:
                return True
    return False


def keyboard_pattern(m):
    key1 = '!@#$%^&*()_+'
    key2 = 'QWERTYUIOP'
    key3 = 'ASDFGHJKL'
    key4 = 'ZXCVBNM'
    t = m.upper()
    for i in range(len(t) - 3):
        if t[i] in key1 and t[i + 1] in key1 and t[i + 2] in key1 and t[i + 3] in key1:
            c1 = key1.index(t[i])
            c2 = key1.index(t[i + 1])
            c3 = key1.index(t[i + 2])
            c4 = key1.index(t[i + 3])
            if c1 == c2 + 1 == c3 + 2 == c4 + 3 or c1 + 3 == c2 + 2 == c3 + 1 == c4:
                return True
        if t[i] in key2 and t[i + 1] in key2 and t[i + 2] in key2 and t[i + 3] in key2:
            c1 = key2.index(t[i])
            c2 = key2.index(t[i + 1])
            c3 = key2.index(t[i + 2])
            c4 = key2.index(t[i + 3])
            if c1 == c2 + 1 == c3 + 2 == c4 + 3 or c1 + 3 == c2 + 2 == c3 + 1 == c4:
                return True
        if t[i] in key3 and t[i + 1] in key3 and t[i + 2] in key3 and t[i + 3] in key3:
            c1 = key3.index(t[i])
            c2 = key3.index(t[i + 1])
            c3 = key3.index(t[i + 2])
            c4 = key3.index(t[i + 3])
            if c1 == c2 + 1 == c3 + 2 == c4 + 3 or c1 + 3 == c2 + 2 == c3 + 1 == c4:
                return True
        if t[i] in key4 and t[i + 1] in key4 and t[i + 2] in key4 and t[i + 3] in key4:
            c1 = key4.index(t[i])
            c2 = key4.index(t[i + 1])
            c3 = key4.index(t[i + 2])
            c4 = key4.index(t[i + 3])
            if c1 == c2 + 1 == c3 + 2 == c4 + 3 or c1 + 3 == c2 + 2 == c3 + 1 == c4:
                return True
    return False


passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors) == 0:
    print("OK")
else:
    for i in errors:
        print(i)