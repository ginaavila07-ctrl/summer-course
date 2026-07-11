print("hello")


name = input("what is your name?")
number = input("what is your favorite number")
minus10 =10
print("hello",name)
print("Your favorite numner is", number)

print("your favorite number minus 10 is", int(number)-10)

print(1,2,3,4, sep =",")

#Enter the Size of all 3 Pizza's
pizza_size1 = input("what is the size of small pizza 1? ")
pizza_size2 = input("what is the size of of small pizza 2? ")
pizza_size3 = input("what is the size of large pizza? ")

int(pizza_size1)
int(pizza_size2)
int(pizza_size3)


#Calauate Pizza Radius
sm_pizza_radius =(int(pizza_size1)+ int(pizza_size2)) /2
lg_pizza_radius = int(pizza_size3)/2

#Caculate the Pizza Area by dividing the Diameter of the Pizza by 2
pizza_area1= 3.14 * float(sm_pizza_radius) /2
pizza_area3= 3.14 * float(lg_pizza_radius ) /2 



#Print the Area of of both small Pizza and the Larage Pizza
print("The total area of both small pizza is ", float(pizza_area1))
print("The area of the large pizza is ", float(pizza_area3))


#Enter the the Price of both small Pizza and the Large Pizza
costumer_cost1 = input("what is the total price of the two small pizza's? ")
costumer_cost3 = input("what is the total price of the large pizza? ")

#Change the cost into a decimal numer 
costumer_cost1 = float(costumer_cost1)
costumer_cost3 = float(costumer_cost3)

# Toatl Area divided by Cost
price_prearea1 = int(pizza_area1) / int(costumer_cost1)
price_prearea3 = int(pizza_area3) / int(costumer_cost3)

#Print Price per area for 2 small pizza's and 1 lage pizza
print(f"Your total price per area for both small pizza is {price_prearea1:.02f}")

print(f"Yur total price per area for a large pizza is {price_prearea3:.02f}")























