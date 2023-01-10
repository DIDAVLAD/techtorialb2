#Ask user to enter a password
# The password should contain
# both upper and lower case letters
# If it contains both upper and lower case letter
# print True , otherwise False.  


print("Enter your password") 
password = input() # Techtorial
# Variable lower is lower case of password 
lower = password.lower() # techtorial
# Variable upper is upper case versin of password
upper = password.upper() # TECHTORIAL 

# How can I understand if there is a lower case in 
# this password?
# I am going to create a boolean condition to check this. 
# If this password is all upper case
# this password should be equal to its upper case version 
# Therefore I can say if this password is not equal to its upper 
# version it means it contains some lower cases. 
is_there_lower = password != upper 

is_there_upper = password != lower 

is_valid = is_there_lower and is_there_upper 

print(is_valid)




















