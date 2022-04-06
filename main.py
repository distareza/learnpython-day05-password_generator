#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
simplePassword=""
for index in range(nr_letters):
  simplePassword+=random.choice(letters)
for index in range(nr_symbols):
  simplePassword+=random.choice(symbols)
for index in range(nr_numbers):
  simplePassword+=random.choice(numbers)
print("Simple Passsword: ")
print(simplePassword)  
print() 

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# 1st Solution
complexPassword=""
for index in range(nr_letters + nr_symbols + nr_numbers):

  randomList = []
  if nr_letters > 0:
    randomList += [1]
  if nr_symbols > 0:
    randomList += [2]
  if nr_numbers > 0:
    randomList += [3]
  choice = random.choices(randomList)[0]
  
  if choice == 1:
    complexPassword+=random.choice(letters)
    nr_letters-=1
  elif choice == 2:
    complexPassword+=random.choice(symbols)
    nr_symbols-=1
  else:
    complexPassword+=random.choice(numbers)
    nr_numbers-=1
print("Complex Password:")
print(complexPassword)
print()
    
## 2nd Solution
print("2nd Complex Password")
def split(word):
    return [char for char in word]

complexPassword=split(simplePassword)
random.shuffle(complexPassword)
print(''.join(complexPassword))

  
    
    
    