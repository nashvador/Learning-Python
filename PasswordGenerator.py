
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

result = []
for x in range(nr_letters):
  a = (random.choice(letters))
  result.append(a)

result1 = []
for y in range(nr_symbols):
  c = (random.choice(symbols))
  result1.append(c)

result2 = []
for z in range(nr_numbers):
  d = random.choice(numbers)
  result2.append(d)

result3 = result2 + result1 + result
random.shuffle(result3)

mystring = ''.join(map(str,result3))
print(f"Your password is {mystring}")