# def is_palindrome(word):
#     word = word.strip().lower()
#     if word == word[::-1]:
#         return True
#     else:
#         return False
   

# phrase = input ("enter a word (enter '' to stop): ")

# while phrase !='':
#     if is_palindrome(phrase):
#         print(f'{phrase} is a palindrome ')

#     else:
#         print(f'{phrase} is not a palindrome ')

#     #get something
#     phrase = input ("enter a word (enter '' to stop): ")

# print('End of Program')



# word= input("enter a word: ")
# word = word.strip()
# word_length = len(word)
# print('-' * word_length)
# print(word)
 
# while len(word) > 1:
#     word = word[1:-1]
#     print(word)

# print('-' * word_length)



# word= input("enter a word: ")
# word = word.strip()
# word_length = len(word)
# indentation = " "
# print('-' * word_length)
# print(word)
 
# while len(word) > 1:
#     indentation = indentation + " "
#     word = word[1:-1]
#     print(indentation + word + indentation)

# print('-' * word_length)


# Dont under stand this is there a better way to write this. 
# def repeated_letter(sentance):
    
#     repeated = ""
#     for letter in sentance:
#         if letter in sentance[sentance.find(letter)+1:]:

#             if letter not in repeated: 
#                 repeated += letter
        
#     return repeated



# phrase = input('Enter a word (stop to exit): ').lower()

# while phrase != 'stop':
#     print(repeated_letter(phrase))


#     phrase = input('Enter a word (stop to exit): ').lower()


rows = int(input("Enter number of row: "))
cols = int(input("entput number of columns: "))

for r in range(rows): # 0 1 2 3 4 5 6
    print(f"Row{r+1}: ", end = '')
    for c in range(cols):
        print(c, end=' ')
    print()

rows = 7
for i in range(rows):
    print(i, "*" * i)

