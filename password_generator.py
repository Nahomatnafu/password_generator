import random

#  letters in a list
letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z"
letters = letters.split()

#  numbers in a list
numbers = "0 1 2 3 4 5 6 7 8 9"
numbers = numbers.split()

#  symbols in a list
symbols = "! @ # $ % ^ & * ( )"
symbols = symbols.split()


print("Welcome to the Password Generator!")

nr_letters = int(input('How many letters would you like in your password? \n'))
nr_symbols = int(input('How many symbols would you like in your password? \n'))
nr_numbers = int(input('How many numbers would you like in your password? \n'))


#  empty password list to append random letters, numbers and symbols to
password = []
for i in range(nr_letters):
    password.append(random.choice(letters))
for i in range(nr_numbers):
    password.append(random.choice(numbers))
for i in range(nr_symbols):
    password.append(random.choice(symbols))

#  shuffling the password list to make it more randomized and strong 
random.shuffle(password)

#  changing the randomized password list into a string
shuffled_password = ""
for letter in password:
    shuffled_password += letter
print(f"Your more random password is: {shuffled_password}")
