import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s',
          't','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M',
          'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','&','*','(',')']
print("Welcome to password generater!")
n_letters = int(input("How many letters you want in password\n"))
n_numbers = int(input("How many numbers you want in password\n"))
n_symbols = int(input("How many symbols you want in password\n"))
password_list=[]
for m in range(1,n_letters+1):
   char = random.choice(letters)
   password_list += char
for m in range(1,n_numbers+1):
   char = random.choice(numbers)
   password_list += char
for m in range(1,n_symbols+1):
   char = random.choice(symbols)
   password_list += char
print(password_list)
random.shuffle(password_list)
print(password_list)
password=""
for char in password_list:
    password += char
    print(password)