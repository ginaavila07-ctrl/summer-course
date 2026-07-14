# #Creating If condtions example
# score = int(input("what is your score? : "))
# if score >= 90 :
#     print("Grade: A")
# elif score >= 80 :
#     print("grade B")
# elif score >= 70 :
#     print("grade C")
# elif score >= 60 :
#     print("grade d")
# else:
#     print("you failed")

# #In Class Exerise 1 (Postive, Negative, or Zero)
# number = float(input(" please enter your favorite number: "))
# if number >= 0 :
#     print("postive number")
# elif number == 0 :
#     print("number is zero")
# else:
#     print("negative number")

#highlight what you dont want to run and press ctrl ? to comment out what you dont want to run. do the same to undo

# #In class Exercise 2: Even or Odd

#Goal: Write a Python script that asks a user for an integer number. Check if the number is even or odd using if and else.
#Check: Should print "Even" or "Odd" based on the number.

# number1 = int(input("input a integer number: "))
# if number1 % 2 == 0:
#     print("the number is a even number: ")
# else: 
#     print("the number is odd")

# #exercise 3: Age Category
# #Goal: Write a python script that asks a user for their age, and then uses if, elif, and else to print the 
# #correct category for the person by based on their age.

# age = int(input("what is your age: "))
# if age <= 13 :
#     print("You are a Child")
# elif age <= 19 :
#     print("You are a Teenager")
# elif age <= 65 :
#     print("You are a Adult")
# else:
#     print("You are a Senior")


# #Exercise 4: Compare Two Numbers
# #Goal: Write a Python Script that asks a user for two numbers. Compare the two numbers and print which is larger, or if they're equal.
# #Should print "{first_number} is larger", "{second_number} is larger", or "The numbers are equal".
# two_num = int(input("What is your favoirte number: "))
# two_num1 = int(input("What is your favoirte second number: "))

# if two_num > two_num1 :
#     print(two_num , "is larger")
# elif two_num == two_num1:
#     print("The numbers are equal")
# else:
#     print(two_num1 , "is greater")

#Exercise 5: Grade Converter
#Goal: Write a Python Script that asks a user for a numeric grade, and then converts a numeric grade to a 
# letter grade and prints the letter grade.

score = int(input("what is your score? : "))
if score >= 90 :
    print("Grade: A")
elif score >= 80 :
    print("grade B")
elif score >= 70 :
    print("grade C")
elif score >= 60 :
    print("grade d")
else:
    print("you failed")