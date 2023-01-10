 #   012345
 #  -6 -5 -4 -3 -2 -1 

s = "python"

print(s[-1]) #n

# index -1 will always give the last letter from the string. 

print(s[-3])

print(s[-4 : -1])

print(s[-4 :-6]) # there is no letter in this scope
# This lime will nbot print anyting 

print(s[3:1]) # There is no letter in this scope

str1 = "Python is an object oriented"

print(str1[1:15:3])

# in slicing when there is 3 arguments 
# first one is starting index
# second one is ending index
# tird one is step

# What do you thong will happen when the step
# number is negative?

city = "Chicago" 

print(city[::-1]) # Will reverse string. 

# Ask user to enter any integer number and print trhat number 
# reversed. 

print("Enter any integer number") 

number = input()

print(number) 

reversed_num = number[::-1] 
reversed_num = int(reversed_num)
print(reversed_num)
print("Data type of this number is" , type (reversed_num))

# In 2 argement scicing what happend?

s = "Techtorial"
print(s[4:2]) #Nothing 

# In 3 argument slicing when the step is negative 

print(s[4:2:-1]) #th 
print(s[4:0-2]) # c
print(s[4:2:-2])









































