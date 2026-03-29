import random
import re
from tkinter import *
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#easy
'''password=""
for char in range(0,nr_letters):
    password+=random.choice(letters)
for char in range(0,nr_symbols):
    password+=random.choice(symbols)
for char in range(0,nr_numbers):
    password+=random.choice(numbers)
print(password)
'''
#hard
password_list=[]
for char in range(0,nr_letters):
    password_list.append(random.choice(letters))
for char in range(0,nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0,nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(password)
def check_strength(password):
    score=0
    if len(password)>=8:
        score+=1
    if re.search("[a-z]",password):
        score+=1
    if re.search("[A-Z]",password):
        score+=1
    if re.search("[0-9]",password):
        score+=1
    if re.search("!#$%&()*+",password):
        score+=1
    if score<=2:
        return "Weak❌"
    if score==3 or score==4:
        return "Medium⚠️"
    else:
        return "Strong✅"
print(check_strength(password))
window = Tk()
window.mainloop()




