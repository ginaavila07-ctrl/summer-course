def time_color(time):
    if time > 5 and time <=10:
        return 'orange'
    elif time <=  5:
        return 'red'
    else: 
        return 'black'
    



assert time_color(25) == 'black'
assert time_color(10) == 'orange'
assert time_color(6) == 'orange'
assert time_color(5) == 'red'
assert time_color(3) == 'red'
assert time_color(-100) == 'red'



COLORS = ["red", "orange", "blue", "green", "yellow", "pink", "black", "gray",
          "purple"]

def is_correct(bg_color, text_color, text, input_color, mode):
    if mode == 'Background Color':
        return input_color == bg_color
    elif mode == "Text Color":
        return input_color == text_color
    elif mode == 'Text':
        return input_color == text
    elif mode == 'Neither':
        return (input_color in COLORS
                and input_color != bg_color
                and input_color != text_color
                and input_color != text)
    
    
# Assert statements to check validity of your code
# assert is_correct('black', 'red', 'blue', 'blue', 'Background Color') == False
# assert is_correct('black', 'red', 'blue', 'black', 'Background Color') == True
# assert is_correct('black', 'red', 'blue', 'red', 'Text Color') == True
# assert is_correct('black', 'red', 'blue', 'blue', 'Text Color') == False
# assert is_correct('black', 'red', 'blue', 'pink', 'Text') == False
# assert is_correct('black', 'red', 'blue', 'red', 'Text') == False
# assert is_correct('black', 'red', 'blue', 'red', 'Neither') == False
# assert is_correct('black', 'red', 'blue', 'pink', 'Neither') == True


# def pretty_print_int(num):
#     num = str(num)
#     text = num[-3::]
#     return text
# test1 = pretty_print_int(456789)
# print(test1)

# def pretty_print_int(num):
#     num = str(num)
#     first6 = num[:-3]
#     first3 = num[0:3]
#     next3 = first6[-3:]
#     last3 = num[-3:]
    
    
#     togehter = first3 + "," + next3 + "," + last3 
    
#     return togehter
# test1 = pretty_print_int(123456789)
# print(test1)

# print(pretty_print_int(5))
# print(pretty_print_int(999))
# print(pretty_print_int(1000))
# print(pretty_print_int(547475874))
# print(pretty_print_int(-84989))


# def pretty_print_int(num):
#     num = str(num)
#     first9 = num[:9]
#     first6 = num[:-3]
#     first3_1 = num[0:3]
#     next3_2 = first6[-3:]
#     last6_3 = first9[-3:]
#     last3_4= num[-3:]
    
    
#     togehter = first3_1 + "," + next3_2 + "," + last6_3 + "," +last3_4
    
#     return togehter

# print(pretty_print_int(123456))
# print(pretty_print_int(123456789012))


def pretty_print_int(number):
    number = str(number)

    negative = False

    if number.startswith("-"):
        negative =True    
        number = number[1:]

    if len(number) <= 3:
        return number
    elif len(number) <=6:
        first3 = number[:-3]
        last3 = number[-3:]
        
        combined =  first3 + "," + last3
       
    elif len(number) <= 9:
        first = number[:-6]
        middle = number[-6:-3]
        last = number[-3:]

        combined = first + "," + middle + "," + last
    
    elif len(number) <=12:
        first3 = number[0:3]
        first6 = number[:6]
        next3 = first6[-3:]
        last3 = number[-3:]
        last6 = number[-6:]
        mid6 = last6[0:3]

        combined =  first3 + "," + next3 + "," + mid6 + "," + last3

    if negative:
        combined = "-" + combined 
    return combined

                
    

print(pretty_print_int(123456789096))
print(pretty_print_int(-84989))


def pretty_print_dollars(number):
    negative = False

    if number < 0:
        negative =True
        number =abs(number)    
        dollars = f"${number:,.2f}"
    else:
        dollars = f"${number:,.2f}"

    if negative:
        dollars = "-" + dollars
        return dollars
    else:
        return dollars

    
       
    
    

    return dollars
    


print(pretty_print_dollars(1000.0))
print(pretty_print_dollars(-800.0))

    # negative = False
    
    # if number.startswith("-"):
    #     negative =True    
    #     number = number[1:]

# def make_field(content, length):
#     content = str(content)

#     if len(content) > length -2:
#         contentlength = content[:length - 2]
#         buffers = length - len(contentlength) - 1
#         buffers = " " * buffers
    
#         return "|" + buffers + contentlength + buffers + "|"

#     else:
#         buffers = length - len(content) - 1
#         buffers = " " * buffers
#         return "|" + buffers + content + buffers + "|"


# print(make_field(1000, 7))
# print(make_field("year", 8))
# print(make_field("world", 5))



def make_line(length):
    make_line = "+" + ("-" * length) + "+"
    return make_line

print(make_line(10)) 


import math
population = 1000000
initial_infected = 1000
r_number = 1.1


# def simulate_infection(population, initial_infected, r_number):
#     infected = initial_infected
#     deceased = 0
#     day = 1

#     print(day, population - deceased)

#     while population - deceased > 0:
#         deceased = deceased + infected
#         infected = math.ceil(infected * r_number)

#         day = day + 1

#         alive = population - deceased

#         if alive < 0:
#             alive = 0

#         print(day, alive)

# simulate_infection(1000000, 1000, 1.1)

import math

def make_line(length, second_lenght):
    return "+" + "-" * length + "++" + "-" * second_lenght + "+"
    

# print(make_line(5, 12)) 
# print("| Day || Population |")
# print(make_line(5, 12)) 

def compound_interest(init_principal:float,acc_rate:float,acc_cmp_freq:int,years:int):
    if acc_cmp_freq == 0:
        A = init_principal * math.e **(acc_rate*years)
        return A
    else:
        A=  init_principal*(1+(acc_rate/acc_cmp_freq))**(acc_cmp_freq*years)
        return A

def simulate_account_balance(init_principal:float,acc_rate:float,acc_cmp_freq:int, setup_fee:float, years:int):

    for year in range (2, years + 1, 2):

        balance = compound_interest(init_principal - setup_fee, acc_rate, acc_cmp_freq, year)

        print(f"| {year}   ||  {round(balance, 2)}  |")

simulate_account_balance(10000.00, 0.025, 12, 25.00, 10)
print(make_line(5, 12)) 


def make_field(content, length):
    content = str(content)

    if len(content) > length - 1:
        content = content[:length - 1]

    buffers = length - len(content) - 1
    buffers = " " * buffers

    return "|" + buffers + content + " |"


    # else:
    #     buffers = length - len(content) -2
    #     buffers = " " * buffers
    #     return "|" + buffers + content + "  |"


print(make_field(1000, 7))
print(make_field("year", 8))
print(make_field("world", 5))


def make_line(length, second_lenght):
    return "+" + "-" * length + "++" + "-" * second_lenght + "+"


def simulate_infection_pp(population, initial_infected, r_number):
    print(make_line(5,12))
    print("| Day || Population |")
    print(make_line(5,12))


    infected = initial_infected
    deceased = 0
    day = 1

    print( make_field(day,5) +  make_field(pretty_print_int(population - deceased),12) )
    # print(day, population - deceased)

    while population - deceased > 0:
        deceased = deceased + infected
        infected = math.ceil(infected * r_number)

        day = day + 1

        alive = population - deceased

        if alive < 0:
            alive = 0

        print( make_field(day,5) +   make_field(pretty_print_int(alive),12) )

print(make_line(5,12))
simulate_infection_pp(1000000, 1000, 1.1)

import math
def make_line(length, second_lenght):
    return "+" + "-" * length + "++" + "-" * second_lenght + "+"

def make_field(content, length):
    content = str(content)

    if len(content) > length - 2:
        content = content[:length - 2]

    return "|" + content.rjust(length - 1) + " |"


def pretty_print_dollars(number):
    negative = False

    if number < 0:
        negative =True
        number =abs(number)    
        dollars = f"${number:,.2f}"
    else:
        dollars = f"${number:,.2f}"

    if negative:
        dollars = "-" + dollars
        return dollars
    else:
        return dollars


def pretty_print_int(number):
    number = str(number)

    negative = False

    if number.startswith("-"):
        negative =True    
        number = number[1:]

    if len(number) <= 3:
        return number
    elif len(number) <=6:
        first3 = number[:-3]
        last3 = number[-3:]
        
        combined =  first3 + "," + last3
       
    elif len(number) <= 9:
        first = number[:-6]
        middle = number[-6:-3]
        last = number[-3:]

        combined = first + "," + middle + "," + last
    
    elif len(number) <=12:
        first3 = number[0:3]
        first6 = number[:6]
        next3 = first6[-3:]
        last3 = number[-3:]
        last6 = number[-6:]
        mid6 = last6[0:3]

        combined =  first3 + "," + next3 + "," + mid6 + "," + last3

    if negative:
        combined = "-" + combined 
    return combined


def simulate_account_balance_pp(init_principal:float, acc_rate:float, acc_cmp_freq:int, setup_fee:float, years:int):

    balances = []

    for year in range(2, years + 1, 2):
        balance = compound_interest(
            init_principal - setup_fee,
            acc_rate,
            acc_cmp_freq,
            year
        )

        balances.append((year, pretty_print_dollars(balance)))

    balance_length = max(len(balance) for year, balance in balances) + 1

    print(make_line(6, balance_length))
    print(make_field("Year", 6) + make_field("Balance", balance_length))
    print(make_line(6, balance_length))

    for year, balance in balances:
        print(make_field(year, 6) + make_field(balance, balance_length))
        print(make_line(6, balance_length))
simulate_account_balance_pp(10000.00, 0.025, 12, 25.00, 10)

    

