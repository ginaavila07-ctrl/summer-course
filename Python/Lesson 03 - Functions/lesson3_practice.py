
#Problem 1
#Print numbers from 1 to 100.

for num in range(1,101):
    print(num)

#Replace numbers divisible by 3 with “Fizz”, by 5 with “Buzz”, and by both with “FizzBuzz”.
    if num % 3 == 0:
        print(f"fizz the number is {num}")
    elif num % 5 == 0:
        print(f"Buzz and the number is {num}")
    elif num % 3 == 0 and num % 5 == 0:
        print (f"Fizz and Bizz, number is diviable by both 3 and 5: {num}")
    else:
        print(num)


####################################################################################################################################

# Problem 2 — Rock, Paper, Scissors

com_choice = ("Rock").upper()

count = 1
#Prompt the user to choose rock, paper, or scissors.
# user_input = input("Lets paly a game, please enter Rock, Paper, or Scissor: ").upper()
#Randomly generate the computer’s choice.


import random

count = 1

won = False

while count <= 3:
    com_choice = random.choice(["ROCK", "PAPER", "SCISSORS"]) 

    user_input = input("Lets paly a game, please enter Rock, Paper, or Scissors: ").upper()
    
    if user_input not in ["ROCK", "PAPER", "SCISSORS"]:
        print("invaild response")
        print("please tyr again")
        continue

    elif com_choice == user_input:
        print("Tied")
        print("Please try again")

    elif com_choice == "ROCK" and user_input == "PAPER":
        print("You Won")
        won = True
        break

    elif com_choice == "ROCK" and user_input == "SCISSORS":
        print("You Lost")
        print("Please try again")

    elif com_choice == "PAPER" and user_input == "SCISSORs":
        print("You Won")
        won = True
        break

    elif com_choice == "PAPER" and user_input == "ROCK":
        print("You Lost")
        print("Please try again")

    elif com_choice == "SCISSORS" and user_input == "ROCK":
        print("You Won")
        won = True
        break

    elif com_choice == "SCISSORS" and user_input == "PAPER":
        print("You Lost")
        print("Please try again")

    
    
    print(f"Computers choice {com_choice}")
    print(f"your choice {user_input}")

    count += 1
    
    
    if count <= 3:
        print(f"You have ({4 -count} ) attempts left")
        print()

if won:
    print(f"Congradulations, it took you {count} attmpts")
else:
    print("Game over, please try again tommorrow")

#Compare both choices and display whether the user won, lost, or tied.

##############################################################################################################################

#Problem 3 — Guessing Game
#Create a program that randomly selects a number between 1 and 100 using the random module.

#The user repeatedly guesses the number until correct.

#“Too high” if the guess is above the number.

#“Too low” if the guess is below the number.

#Congratulates the user when correct.

#Bonus: Display how many attempts the user made.

random_num = random.randint(1,101)

count = 0
won = False
while count <= 3:
    user_guess = int(input("Guess an number between 1 and 100 : "))
    if user_guess == random_num :
        print("you guessed corretly")
        won = True
        break
   
    elif user_guess > random_num:
        print("Your number was to high")

    elif user_guess < random_num:
        print("your guess was to low")

    count +=1 
if won:
    print("Congradulation!")
    print(f"you guessed it in {count} times")

else:
    print(f"You reached the maxiumn attepts today please try again tommorrow.")
    print(f"you attmepeted {count} times")
    print(f"Answer was {random_num}")
    
###############################################################################################################################

#Write a program to help you track your student’s grades.  Ask the user how many students 
#are in the class.  For each student, ask their name and their grade.  Display the class 
#average.  Display the highest grade in the class. Display the lowest grade in the class.
#Bonus:  Display who got the highest grade in the class

students = []

size_ofclass = int(input("How many students are in the class: "))



for i in range(size_ofclass):
    print(f"n\Enter the information of student {i + 1}")

    name = input("Enter student first and last name: ")
    grade = float(input("Enter student grade: "))



    if grade >= 90:
        letter_grade = "A" 
    elif grade >=80:
        letter_grade = "B"
    elif grade >=70:
        letter_grade = "C"
    elif grade >=60:
        letter_grade = "D"
    else:
        letter_grade ="F"
        print("you are failing this class")

    students.append({
        "name" : name,
        "grade" : grade,
        "letter grade" : letter_grade
})





