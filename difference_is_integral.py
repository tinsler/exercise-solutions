from operator import truediv
from pickle import TRUE


first_number = float(input("Input the first number: "))
second_number = float(input("Input the second number: "))
difference = first_number - second_number
print(f"The difference between {first_number} and {second_number} is an \
integer? {difference.is_integer()}!")
