import random

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
             'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbol = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@',
          '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '']
password = []
num_alphabets = input("how many letters you want:")
num_digits = input("how many integers you want:")
num_symbols = input("how many symbols you want:")

for i in range(int(num_digits)):
    password.append(random.choice(digits))
for i in range(int(num_symbols)):
    password.append(random.choice(symbol))
for i in range(int(num_alphabets)):
    password.append(random.choice(alphabets))
new_password = ""

for i in range(0,len(password)):
   new_password += password[i]
print(new_password)
