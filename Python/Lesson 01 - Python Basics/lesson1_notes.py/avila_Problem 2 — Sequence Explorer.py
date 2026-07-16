#Problem 2 — Sequence Explorer
# Printing number range in one line 1-15
numbers = list(range(1,16))
print(numbers)

# Print even numbers from 2 to 30
even_numbers = list(range(2,31,2))
print(even_numbers)

# how to remove commas using *
print(*numbers)
print(*even_numbers)


#create a count down 20 t0 2 counting only even
count_down = list(range(20,2,2))

print(*count_down)

#part 2 have user input the start and finish and how many to count by
start = int(input("What is the starting number you want to start with: "))
finish = int(input("What number do you want to stop with: "))
count = int(input("What number do you want to count by: "))

# create the range with the above varibles 
numbers_input = range(start,finish,count)

#print the outcome using the * to create a space instead of a comma
print(*numbers_input)


#Problem 3 — Drill Sergeant Fitness Test

#Have user input name, how many push they completed, how many minutes it took to complete 2 mile run
name = input("What is your first and last name?: ")
rank = input("What is your rank?: ")
pushup = int(input("How many pushup do your complete?:"))
run = float(input("How amny minutes did take fro you to complete 2 mile run?: "))

#avg_pace caculations
avg_pace = run/2

#Create Banner 
banner = " == After Action Report == "

print(banner)
print("Solider:" , rank , name)
print("Pushups: " , pushup)
print("2 mile run:" , run , "minutes")
print("Average pace:" , avg_pace , "per mile")
print("Dismissed")


#Problem 4 — Road Trip Fuel Calculator

# Asking user for input  ( int in front of places I want whole numbers Float in fron if input that needs a decimal number)
distance = float(input("What is distance of the trip in miles? "))
mpg = float(input("What is your car's fuel efficiency in miles per gallon? "))
gas_price = float(input(" What is current price of gas per gallon in dollars? "))

#cacluations distances divided by mpg & gallons needed multipled by gas price
gallons_needed = distance / mpg
total_price = gallons_needed * gas_price

#Create header
header = ("--- Road Trip Fuel Estimate ---")

#create a space
space = ("             ")


print(header)
print(f"Distance:        {distance:.0f} miles")
print(f"Fuel efficiency: {mpg:.0f} MPG")
print(f"Gas Price:       {gas_price:.02f} / gallon")
print(space)
print(f"Gallons need:    ${gallons_needed:.02f}")
print(f"Total fuel cost: ${total_price:.02f}")

#Advanced: Extend the program to also calculate the cost for 3 different gas price scenarios using range():     

#Price user entered plus .50 and 1.00
second_price = float(.50) + gas_price
third_price = float(1) + gas_price


#Ceate Border
second_border = ("--- Price Scenarios ---")
print(second_border)
print(f"Gas @ ${gas_price:.02f}: Total = ${total_price} ")
print(f"Gas @ ${second_price:.02f}: Total = ${second_price * gallons_needed:.02f} ")
print(f"Gas @ ${third_price:.02f}: Total = ${third_price * gallons_needed:.02f} ")


