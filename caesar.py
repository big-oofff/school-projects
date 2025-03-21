def caesar(string, k):
    new = ""
    for char in string:
        if char.isalpha():  
            shift = k % 26  
            if char.islower():
                new += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                new += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            new += char  
    return new

print(caesar("Be sure to drink your Ovaltine!", 13))
