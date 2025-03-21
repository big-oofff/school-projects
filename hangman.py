import hang
import random
counter = 0
with open('words.txt', 'r') as fhand:
    words = fhand.read().split()

random_word = random.choice(words)
list_of_letters = [x for x in enumerate(list(random_word))]



print(hang.HANGMAN[0])
guesses = ["_ "] * len(random_word)
wrong_guesses = []
while counter <= 11:
    guessed_right = False
    if counter == 10:
        print(f"You lose! The word was {random_word}")
        break
    print("Guess the word: " + ''.join(guesses))
    guess = input("Enter guess, either as a letter or full word: ").lower()
    if len(guess) == 1:
        if guess in random_word:
            guessed_right = True
            for index, letter in list_of_letters:
                if guess == letter:
                    guesses[index] = letter + " "
    if guess == random_word or " ".join(random_word).strip() == "".join(guesses).strip():
        print(f"You win! You successfully guessed {random_word}")
        break
    if guessed_right == False:
        wrong_guesses.append(guess)
        counter += 1
        print(hang.HANGMAN[counter])
        print("Wrong answers: " + ",".join(wrong_guesses))

    
   






