choice = input("Would you like to enter Miles above Mars or Kilometers above Mars? ").lower()

if choice == "miles above mars":
    miles_enter= float(input("enter the number of miles: "))
    yards = miles_enter * 1760
    feet = miles_enter * 5280
    inches = miles_enter * 63360
    print(f"Miles entered: {miles_enter} it would take {yards} yards, or {feet} feet, or {inches} inches to to reach Mars!")
    #make mile conversion
elif choice == "kilometers above mars":
    kilo_enter= float(input("enter the number of kilometers: "))
    meters = kilo_enter * 1000
    centimeters = kilo_enter * 100000
    millimeters = kilo_enter * 1000000
    print(f"Kilometers entered: {kilo_enter} it would take {meters} meters, or {centimeters} centimeters, or {millimeters} millimeters to to reach Mars!")

import math
#Pizza 1 Automation 2 15 inch pizza 


def two_circular_pizzas():
    diameter = 15
    radius = diameter /2
    area = math.pi * radius ** 2
    total_area = area * 2
    dough = 20
    efficiency = total_area / dough
    return efficiency 

def equilateral_triangle_pizza():
    side = 20
    area = (math.sqrt(3) / 4) * side ** 2
    dough = 20
    efficiency = area / dough
    return efficiency

def square_pizza():
    side = 18
    area = side * side
    dough = 18
    efficiency = area / dough
    return efficiency

print(" ==== Pizza Options ==== ")
print(f"Two circular pizzas: {two_circular_pizzas():.2f}")
print(f"Equilateral triangle pizza: {equilateral_triangle_pizza():.2f}")
print(f"Square pizza: {square_pizza():.2f}")

if two_circular_pizzas > equilateral_triangle_pizza and two_circular_pizzas > square_pizza:
    print("Automatron 1 is the best deal!")
elif equilateral_triangle_pizza > two_circular_pizzas and equilateral_triangle_pizza > two_circular_pizzas:
    print("Automatron 2 is the best deal!")
else:
    print("Automatron 3 is the best deal!")


# #chief.tech@python-practical:/Problem3$ cat problem3_statement.txt 
# Our inbound colonists rapidly approach Mars atmosphere, but we still do not have reliable comms with them.
# We must rapidly launch our spare rocket to establish comms and share the correct telemetry data with them before they smash into Mars!

# There's no time to unload the modules that are on the rocket, and we must begin fueling right away.
# The problem is, we do not know how much fuel we need.

# As you rush to the rocket, you notice a list of all of the modules' mass on board (your python file input).

# Fuel required to launch a given module is based on its mass.
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# For example:

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.

# As the Chief Engineer, you need to calculate the total fuel requirement.
# To find the total fuel requirement, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.

# What is the sum of the fuel requirements for all of the modules on your spacecraft?

# Once you solve this problem, issue a pull request with all three of your solutions to the International Space Station (https://github.com/Ryan-L-N/cohort-7-practical.git).
# To keep the International Space Station's file system clean, your solutions should be inside of a folder with your last name.

# Finally, create a broadcast beacon with Earth to state that the crisis was averted.
# To do this, create a VM, host a website with a picture of your choice on the VM, and share the public IP address of your website with the International Space Station.