# # lesson notes for lesson 3

# for number in range(1,101):
#     print(number)
#     if number % 3 == 0 and number % 5 == 0:
#         print(f"fuuz_Bizz {number}")
#     elif number % 3 == 0:
#         print(f"Fizz {number}")
#     elif number % 5 == 0:
#         print(f"Buzz {number}")
#     else:
#         print(number)


# answer = ("rock")
# response = input("enter rock, paper or , scissors: ").lower()

# if response == "rock" and answer =="paper":
#     print("You won")
# elif response == "scissor" and answer =="paper":
#     print("You won")
# elif response == "paper" and answer == "rock":
#     print("You won")
# elif response == "scissors" and answer == "rock":
#     print("You Lost")
# elif response == "rock" and answer == "rock":
#     print("Tied")
# else:
#     print("invalid response")




# import random
# random_number = random.randint(1,100)
# count = 1 
# guess = int(input(" Please guess a number: "))

# while guess != random_number and count <= 5:
#     if guess > random_number:
#         print("guess is to high")

#     else:
#         print("you guessed to low")
#     guess = int(input(" Please guess a number: "))
#     count += 1

# if guess == random_number:
#     print(f"you guessed, correctly it took you {count} guesses")
# else:
#     print(" Better next next time, you reched your maxiumn attepts")



# random_num =random.randint(0,100)
# coutt = 1
# user_guess = int(input("User guess a number between 1 and 100: "))

# if random < 50 :
#     print("the number is less than 50")
# elif random > random_num :
#     print("your guess is to low")

# print(random_num)


# look back at this to see if you can do this. 

# Defining Function 
def add_together (num1,num2):
    sum = num1 + num2
    return sum

# Call Function 
result = add_together(10,20)

# show the answer you need a print funtion
print(result)



# new problem 
lenght = int(input("Enter the base of the rectangle: "))
width = int(input(" Enter the width of the rectangle: "))

# the :int lets it know we are expexcting intergers. 
def area_retangle (len: int, wid: int) -> int:
    area = len * wid
    return area

answer = area_retangle (lenght, width)
print(f" the area is {answer}")


total = float(input("input the toatl amount of your bill: "))
tip_percentage = float(input("What percentage you want to tip: "))

def tip (total: float, percentage:float) -> float:
    percentage = percentage/100
    amount = total * percentage
    return amount

tip_amount = tip (total, tip_percentage)
print(f" Baseed on you total cost of {total} you should tip {tip_amount:.02f}")


def has_more_characters (first_word:str, Second_word:str) -> str:
    length1 = len(first_word)
    length2 = len(Second_word)
    if (length1) < (length2):
        return Second_word 
    elif (length1) > (length2):
        return first_word 
    else:
        return "they are equal"


more_charaters = has_more_characters ("sally", "tom")


print(more_charaters)

# need to helpwith these make it also show how many characteres it is




        






    



