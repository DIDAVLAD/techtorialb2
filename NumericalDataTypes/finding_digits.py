
a = 123
# The number a can be any three digit number.
# Solution should work for any 3 digit number .
# Multiply the each digit of number a .

# When we integer divide number with 10 it will get rid of 
# the last digit of the number .

# When I find remainder with 10 I get last digit of the number.

# multiplicatin = a% * (a//10%10) * (a//100)
#print(multiplication)

last_digit = a % 10 

first_two_digits = a // 10 

middle_digit = first_two_digits % 10

first_digit = first_two_digits // 10 

print("Multiplication of each digit of number a is",(first_digit*
last_digit*middle_digit))

# pot fi intrebafri la interviu-este ce ma facut in liniile de la 2 la 21
# Create a function to find each digit of the given number.
# Create a program to find each digit of the number and sort them.
# Create a program to find each prime digit of the number.
















