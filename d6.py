#Write a program that asks the user what the temperature is and 
# prints out “Boy, it is hot!” if the temperature is 90 degrees or more.
temp = int(input("What is the temperature? "))
if temp >= 90:
    print("Boy, it is hot!")
#Write a program that asks the user who their favorite singer is.  
# If they say “Taylor Swift”, respond with “Mine too!”.  
# Otherwise respond with “So and so is cool.  But I like Taylor Swift!”
singer = input("Who is your favorite singer? ")
if singer.lower() == "taylor swift":
    print("Mine too!")
else:
    print(f"{singer} is cool. But I like Taylor Swift!")
#Write a program that asks the user for their grade as an integer. 
#  Print out the correct letter grade for their input.  
# For example, 87 would print out 
# “B”...  
# (This may be a little trickier than you think.  Make sure to try different values…)
grade = int(input("Please enter grade: "))
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
#Write a program that asks the user for 4 test scores.  
# Drop the lowest test score and return the average score of the remaining test scores.
test_scores = []
for i in range(1,5):
    test_scores.append(int(input("Enter test score " + str(i) + ": ")))
test_scores.remove(min(test_scores))
print("Your lowest score is " + str(min(test_scores)) + " and your average is" + sum(test_scores) / len(test_scores))
#**bonus** - You are a zookeeper in charge of two monkeys, Maurice and Fred, 
# create two boolean variables a_smile and b_smile to indicate if each is smiling.
#  Ask the person watching their cage if they are smiling or not.  
# Print ‘We are in trouble’ if they are both smiling or if neither of them is smiling. 
#  Print ‘No worries’ if only one of them is smiling.
maurice_smile = True
fred_smile = True
m = input("Is Maurice smiling? ")
if m.lower() == "no":
    maurice_smile = False
f = input("Is fred smiling? ")
if f.lower() == "no":
    fred_smile = False
if not (maurice_smile and fred_smile) or (maurice_smile and fred_smile):
    print("We are in trouble")
else:
    print("No worries")

