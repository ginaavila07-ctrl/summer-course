#loops
# fruits = ["apple", "banana", "cherry"]
# for fruits in fruits:
#     print(fruits)

# #when creating the varible number inside a FOR LOOP it onlt exist in the loop
# for number in range(1,11):
#     print(number)

# my_listN = ["bob", "tina", "janet" "sally"]

# my_listN.append("Zack")
# my_listN.append("chris")

# for my_listN in my_listN:
#     print(my_listN)

# print(my_listN[2])

# # will print numbers 20 through 50 by 5s
# for number in range(20,51):
#     if number % 5 ==0:
#         print(number)


#number = 100
#while number != 40:
 #   print("the numer is not 40 ")

# make user put in a number till they put in a even number

# user_input = int(input("enter a even integer number: "))
# while user_input % 2 == 1:
#     user_input = int(input("enter a even integer number: "))
    
# print(f" Good job you enetered a even number, {user_input} ")
    
# #user guess number and tells them if they are too high or low until they guess the number. 
# secret_number = 22

# user_guess = int(input(" Guess a interger number: "))

# count = 1

# #having it count how many times you guessed

# while user_guess != secret_number:
#     if count > 4 :
#         print("Better luck next time: Must wait 24 hours before next guess")
#         break
        
#     elif user_guess < secret_number:
#         print("Your guess was to loo")

#     else:
#         print("Your Guess was to high!")
    
#     count += 1   
#     user_guess = int(input(" Guess a interger number: "))
    

# if user_guess == secret_number :
#     print(f"Congradulation's you guessed the right numer: {user_guess} !")
#     print(f"it took you {count} guesses")


####****need to put this into the chat to  figure out why it doesnt stop once it hits 5 times**********************

#Exercise 6: String Length Check
#Goal: Write a Python Script that asks the user for an input string. Then check if a string has more than 10 characters. Print "Long string" if it is longer than 10 characters, print "Short string" if it is shorter.

#Check: Should print "Long string" if length is greater than 10, otherwise "Short string".

# entertext = input("use yhe street you live on: ")

# #using len will count the number of stings in text entered 
# if len(entertext) >= 10:
#     print("long string of text")
# else:
#     print("short string of text")

# print(f" your text was {len(entertext)} strings long")

# #Exercise 7: Logical AND Operator
# #Goal: Write a Python script that asks the user for a number. Check if a number is between 10 and 20 (inclusive) 
# #using the and operator. Print "Number is in range" if it is in between 10 and 20. Otherwise it should print "Out of range."

# # User input 
# user_num = int(input("Please enter a number: "))

# # If statmente is grater or equal to 10 and user number is less or equal to 20 print in range
# while True:
#     if user_num >= 10 and user_num <= 20:
#         print("Number is in range")
#         break

# # if not print out of range
#     else:
#         print("Out of range.")
#         user_num = int(input("Please enter a number: "))


# #Exercise 8: Logical OR Operator
# #Goal: Write a python script that checks if a character is a vowel using the or operator. 
# # Print "vowel" or "consonant" depending on the input.

# vowel_list = ["A", "E", "I", "O", "U","Y"]

# letter = input("Please enter a letter to see if it is a vow: ").upper()

# if letter in vowel_list: 
#     print(f"Letter is a vow, you entered {letter}")

# else:
#     print(f"This letter is not a vow, you entered {letter}")

# #Stretch: Exercise 9: Leap Year Checker
# #Goal: Write a Python Script that asks the user for the year. Determine if a year is a leap year. Print the result.

# year = int(input("Input a year to see if it is Leap Year: "))

# # using % modular lets me know if a number is divisable with any reminder, 
# # year entered divieded by 4 is reminder is 0 it is true, if it left a 1 it would be false. 
# #                      reminder
# # 8 % 4	   8 ÷ 4 = 2	0	0
# # 9 % 4	   9 ÷ 4 = 2	1	1
# if (year % 4 == 0 and year % 100 == 100) or (year % 400 == 0):
#     print(f"{year} is a leap year ")

# else:
#     print(f"{year} is not a leap year")


# #Stretch: Exercise 10: Nested Conditionals - BMI Calculator
# #Goal: Write a Python Script that asks the user for their weight in kilograms and their height in meters. Calculate BMI category using correct if-elif-else structure.

# #BMI < 18.5: "Underweight"
# #BMI 18.5-24.9: "Normal weight"
# #BMI 25-29.9: "Overweight"
# #BMI 30+: "Obese"
# #Formula: BMI = weight (kg) / height (m)²

# weight = float(input(" Input your current weight in Kilograms: "))
# height = float(input(" Input your current height in Meters: "))

# bmi = weight / (height **2)

# if bmi < 18.5:
#     print("Under weight")
# elif bmi <= 24.9:
#     print("Normal weight")
# elif bmi <= 29.9:
#     print("Overweight")
# else:
#     print("Obese")


#Exercise 11: Create and Print a List
# Goal: Create a list of your favorite colors and print each color using a for loop.

colors = ["red", "blue", "green"]
for colors in colors:
    print(colors)

#Exercise 12: List Length
#Goal: Create a list of numbers and print how many items are in the list.

numbers = [5, 10, 15, 20, 25]

print(f"the list has {len(numbers)} numbers in it")

#Exercise 13: Append to a List
#Goal: Start with an empty list and add 5 different items to it using append().

my_list = ["gina","tom", "tom", "tank", "sally"]
my_list.append("tommy")
print(my_list)

#Exercise 14: Loop Through a Range
#Goal: Use a for loop with range() to print numbers 1 through 10.
# i is creates the loop but you can use anything in its place it is just cleaner: 
# The basket (i) only holds one value at a time, and it changes each time the loop repeats.

for i in range(1,11):
    print(i)

#Exercise 15: Sum Numbers in a List
#Goal: Calculate the sum of all numbers in a list using a for loop.

numbers = [4, 7, 2, 9, 12]
total = 0

#Go through each item in the numbers list and store the current item in a variable called num.
for num in numbers:
    total += num
    print(f"The total number is {total}")

#Exercise 16: List Membership
#Goal: Check if a fruit is in a list of available fruits.

available_fruits = ["apple", "banana", "orange", "mango"]
fruit = "banana"

if fruit in available_fruits:
    print("Fruit in Stock")
else:
    print("Out of Stock")

#Exercise 17: Count Even Numbers
#Goal: Count how many even numbers are in a list using a for loop.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
        
print(f"There are {count} even numbers in the list")

#Exercise 18: While Loop Countdown
#Goal: Use a while loop to count down from 10 to 1.

count = 10

#"Keep repeating the code below as long as count is greater than or equal to 1."
while count >= 1:
    print(count)
#the loop would never end because count would always stay 10. This is called an infinite loop.
    count -= 1

#Stretch: Exercise 19: While Loop with Condition
#Goal: Use a while loop to keep doubling a number until it exceeds 100.

number = 1
while number <= 100:
    print(number)
    number *= 2 

#Stretch: Exercise 20: Create a List with Range
#Goal: Use range() to create a list of even numbers from 0 to 20.

even_list = list(range(0,21,2))
print(even_list)

#Exercise 21: Build a List with Loop
#Goal: Create a new list containing the squares of numbers 1 through 5.

#creates the list but empty
sq_list = []

# the loop "for" and range
for num in range(1, 6):

#will Sq each number in the range
    sq_list.append(num ** 2)

print(sq_list)


