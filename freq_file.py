import string
d = {}
user_word = input("Enter Word: ").lower()
with open('story.txt', 'r') as fhand:
    text = fhand.read().lower()
    text = text.replace("—", " ").replace("-", " ")
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    for word in words:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
print(d)
if user_word in d:
    if d[user_word] == 1:
        print(f"The word '{user_word}' appears {d[user_word]} time.")
    else:
        print(f"The word '{user_word}' appears {d[user_word]} times.")
else:
    print(f"The word '{user_word}' does not appear.")
