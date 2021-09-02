text = input("Text: ")
substring = input("Substring: ")
for old, new in sorted({ostr: f"[{rp}]" for ostr, rp in [(text[i:i+len(substring)], "".join([s if s == substring[j] else '?' for j, s in enumerate(text[i:i+len(substring)])])) for i in range(len(text)-len(substring)+1)] if rp.count("?") <= 1}.items(), key=lambda x: x[1], reverse=True):
    text = text.replace(old, new)
    if "?" not in new:
        break
print(text)
