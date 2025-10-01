def charfreq(text):
    Hw2 = {}
    for ch in text:
        if ch.isalpha():
            if ch in Hw2:
                Hw2[ch] = Hw2[ch] + 1
            else:
                Hw2[ch] = 1
    return Hw2

userinp = input("Enter string: ")
parts = userinp.split(",")

for part in parts:
    part = part.strip()
    result = charfreq(part)
    for key in result:
        print(key, "=", result[key], end=", ")
    print()