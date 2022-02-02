print("Welcome to the computer quiz game")

playing = input("Do you want to give it a try? ").lower()

if playing != "yes":
    quit()

print("Great! Let's get started")
score = 0

answer = input("What does IDE stand for? ").lower()
if answer == "integrated development environment":
    print("Correct!")
    score += 1
else:
    print("Sorry that is wrong.")

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry that is wrong.")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Sorry that is wrong.")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Sorry that is wrong.")

answer = input("What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Sorry that is wrong.")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100)+ "%")
print("Thank you for playing!")