# Bro Code #6: user input
# Week 1
# https://www.youtube.com/watch?v=XKHEtdqhLK8&t=1814s

name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))

age = age + 1

print("Hello "+name)
print("Your age is "+str(age)+ " years old")
print("Your height is "+str(height) + "cm tall")