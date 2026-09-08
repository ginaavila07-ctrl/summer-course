# num = 4
# while num < 500:
#     print(num)
#     num = num * 5
# print(num + 1)

# num = 4
# while num < 500:
#     num = num * 5
#     print(num)

# print(num +1)

# amount = int(input("enter amount"))
# tip_rate = 15
# while tip_rate <= 25:
#     print(amount * tip_rate / 100)
#     tip_rate = tip_rate + 1

for word in ['this', 'is', 'it']:
    print(f'{word:>6}')
#      this
#      is
#      it

# row = 1
# for item in [3, 'abc', '2.17']:
#     print(f'{row}: {item}')
#     row +=1

#     for letters in ("a","b", "c"):
#         print(letters.upper())

# for i in range(3,6):
#     print(i)

# for num in range(1,5):
#     print(num, end=' ')
#     print(num)
# print('.')
# print('---->')

# amount = 50
# for tip_rate in range(15,26):
#     print(amount * tip_rate / 100)

# amount = 50
# tip_rate = 15
# while tip_rate < 26:
#     print(amount * tip_rate/100)
#     tip_rate =tip_rate +1

def prime(number):
    for divisor in range(2,number):
        if number % divisor == 0:
            return False
    return True

first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

print("prime number from", first, "to", second)
for i in range(first, second):
    if prime(i):
        print(f'{i} is a prime number')

def is_ordered(letters):
    if letters == sorted(letters):
        return True
    else:
        return False

def is_ordered(text):
    for i in range(len(text)-1):
        if text[i].lower() > text[i + 1].lower():
            return False

    return True

text = input("Enter String:  ")
if is_ordered(text):
    print(f'{text} is aplhabetically in order')
else:
    print("is in order")

print(is_ordered('abcde'))

with open("mt_file.txt") as f:
    text = f.read()
    print(text)

with open("mt_file.txt") as f:
    for line in f:
        print(line)