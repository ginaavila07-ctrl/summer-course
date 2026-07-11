#Input for the user
name = input("What is your name? ")
fnumber = input("what is your favoirte number? ")

#adding the display message (strip() Removes spaces before and after the name..title()Capitalizes the first letter of each word.)
content1 = 'Hello, ' + name.strip().title() +'!'
content2 = 'Your favorite number is ' + fnumber

#Creating White space 
white_space = (30 - len(content1) - 3)

#making a varible when called upon the number of astrekis needed
border_ask = 30


# chosing the symbol and calling the border varible numberto create top border(The * operator repeats a string.)
print("*"*border_ask)

#calling the contnet created adding * in front with one space, calling on What space 30 spaces and then *
print('* ' + content1 + ' ' * white_space +'*')
print('* ' + content2 + ' *')

# chosing the symbol and calling the border varible number to create bottom border (The * operator repeats a string.)
print("*"*border_ask)
