
bool1 = True
bool2 = False

print(type(bool1)) # <class 'bool'>

print(type(bool2)) # <class 'bool'>

print(bool1) # True 
print(bool2) # False 

# We are trying to use arithmetical operation
# Using numerical value of the boolean variable 
# The Python will make sense out of the expression below 
print(bool1 + 6) # 7

# When ever we see + in python,python will see it like math and try to do 
# some calculation

print(bool2 * 112) # 0 

# What happens when we use comma betwee a number and a boolean variable. 

print(bool1,6) # True 6 or 7 or Syntax error 
               # True 6  

print(bool2,6) # False 6 

# How to print string and boolean in single print function ?
# Just use comma between two variable. 

print("The value of the bool1 is",bool1)
print("The value of bool2 is",bool2)










































