trf = True

while trf:
    word = input("Enter word: ")

    for ch in word:
        print(ch)
        c = ch.lower()

        if ch.isupper():
            case_info = "Uppercase"
        elif ch.islower():
            case_info = "Lowercase"
        else:
            case_info = "Not a letter"

        match c:
            case "a" | "e" | "i" | "o" | "u":
                print(f"{ch} is a vowel and {case_info}")
            case "x":
                trf = False
            case _:
                if case_info == "Not a letter":
                    print(f"{ch} is not a letter")
                else:
                    print(f"{ch} is a consonant and {case_info}")