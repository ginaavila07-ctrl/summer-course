#Step 1: Receive the weight and height from the user
weight = int(input("Enter the weight in pounds:"))

height = int(input("Enter the height in inches:"))


#Step 2: Calculate BMI
def caculateBMI(weight: int, height:int)->int:
    bmi = weight / height ** 2 * 703
#Step 3: Round up BMI
    bmi= round(bmi)
    return bmi

bmi = caculateBMI(weight,height)
#Step 4: Print results
print("The BMI rounded to the nearest integer is:", bmi)

# decide BMI Value means under or over



def bmi_status(bmi):
    if bmi <= 20:
        print ("You are underweight")
    elif bmi <= 25:
        print ("You are in a helathy BMI")
    else:
        print("You are over weight")

bmi_status(bmi)

pennies_per_dollar = 100
pennies_per_quarter = 25
pennies_per_dime = 10
pennies_per_nickle = 5

dollar_value = int(input("Enter bill value in dollars (1 = $1 bill, 5 = $5 bill, etc.): "))
item_price = float(input("Enter item price: "))

def convert_to_pennies(dollar:int)->int:
    dollar_pennie_amount = dollar * pennies_per_dollar
    return dollar_pennie_amount



def convert_price_pennies(price:float)->float:
    price_pennie_amount = price * pennies_per_dollar
    return price_pennie_amount



def change_given(bills_to_pennies, price_pennies):
    change= bills_to_pennies - price_pennies
    return change

bill_pennies = convert_to_pennies(dollar_value)
price__pennies = convert_price_pennies(item_price)

change = change_given(bill_pennies, price__pennies)
change_in_dollars = change /100
print(f"change in pennie: {change}")
print(f"change in dollars: {change_in_dollars}")


total_dollars = change // pennies_per_dollar
dollars_pennies = change % pennies_per_dollar

total_quaters = dollars_pennies // pennies_per_quarter
quaters_pennie = dollars_pennies % pennies_per_quarter

total_dimes = quaters_pennie // pennies_per_dime
dimes_pennie = quaters_pennie % pennies_per_dime

total_nickle = dimes_pennie // pennies_per_nickle


print(F"Dollars:  {total_dollars}")
print(f"Quarters:  {total_quaters}")
print(f" Dimes: {total_dimes}")
print(f"Nickles: {total_nickle}")
print(f" your total amount of change is {change_in_dollars}")









