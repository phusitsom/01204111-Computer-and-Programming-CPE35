text = input("Text: ")
substring = input("Substring: ")

if substring in text:
    print(text.replace(substring, f"[{substring}]"))
else:

    repl_str = {}

    for i in range(len(text)-len(substring)+1):

        iter_str = text[i:i+len(substring)]
        tmp_str = ''

        for j, char in enumerate(iter_str):

            if char == substring[j]:

                tmp_str += char

            else:
                tmp_str += '?'

        if not tmp_str.count('?') > 1:
            repl_str.update({iter_str: f"[{tmp_str}]"})

    for old, new in repl_str.items():
        text = text.replace(old, new)

    print(text)
