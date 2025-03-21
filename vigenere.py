def vigenere(string, keyword):
    i = 0
    new = ""
    shifts = {}
    keyword = keyword.lower()
    for letter in keyword:
        if letter not in shifts:
            shifts[letter] = (ord(letter) - 97) % 26  
    print(shifts)
    for char in string:
        if char.isalpha():
            shift = shifts[keyword[i % len(keyword)]]
            print(shift)
            if char.islower():
                new += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                new += chr((ord(char) - 65 + shift) % 26 + 65)
            i += 1        
        else:
            new += char

    return new
print(vigenere("g", "zloha"))


