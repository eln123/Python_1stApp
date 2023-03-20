print("Welcome to my computer quiz!")

#inside input, you put a prompt
#prompt is the term for what appears before user starts typing
#whatever you put in quotes is the prompt

playing = input("Do you want to play? ")
# you put a space after the question mark,
# otherwise, in your terminal, when the user starts
# typing, the stuff they type will appear next to the question mark
#whatever the user types in response to the prompt,
# is stored in playing

if playing != "yes":
   quit()
else:
    print('hi')

score = 0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!')
    score += 1
else : 
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else : 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
    score += 1
else : 
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
    score += 1
else : 
    print("Incorrect!")


print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%" + " questions correct!")

text = "tEst is over"
print(text.lower())
print(text.upper())

