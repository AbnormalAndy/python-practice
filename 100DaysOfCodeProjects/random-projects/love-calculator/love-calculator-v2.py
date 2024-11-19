def calculate_love_score(name_one, name_two):
    name = name_one + name_two

    total_true = 0
    total_love = 0

    if "t" in name:
        for letter in name:
            if letter == "t":
                total_true += 1
    if "r" in name:
        for letter in name:
            if letter == "r":
                total_true += 1
    if "u" in name:
        for letter in name:
            if letter == "u":
                total_true += 1
    if "e" in name:
        for letter in name:
            if letter == "e":
                total_true += 1
    if "l" in name:
        for letter in name:
            if letter == "l":
                total_love += 1
    if "o" in name:
        for letter in name:
            if letter == "o":
                total_love += 1
    if "v" in name:
        for letter in name:
            if letter == "v":
                total_love += 1
    if "e" in name:
        for letter in name:
            if letter == "e":
                total_love += 1

    print(f"{total_true}{total_love}")

"""
    for letter in name_one.lower():
        if letter == "t":
            total_true += 1
        if letter == "r":
            total_true += 1
        if letter == "u":
            total_true += 1
        if letter == "e":
            total_true += 1
        if letter == "l":
            total_love += 1
        if letter == "o":
            total_love += 1
        if letter == "v":
            total_love += 1
        if letter == "e":
            total_love += 1

    for letter in name_two.lower():
        if letter == "t":
            total_true += 1
        if letter == "r":
            total_true += 1
        if letter == "u":
            total_true += 1
        if letter == "e":
            total_true += 1
        if letter == "l":
            total_love += 1
        if letter == "o":
            total_love += 1
        if letter == "v":
            total_love += 1
        if letter == "e":
            total_love += 1

    print(f"{total_true}{total_love}")
"""
