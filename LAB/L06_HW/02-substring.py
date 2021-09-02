(lambda t, ss: print(f"[{ss}]".join(t.split(ss))) if ss in t else print(
    "Not found"))(input("Text: "), input("Substring: "))
