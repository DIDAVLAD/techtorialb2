# Given a string , return a version where all
# the "X" have been removed.
# Except the "X" at the very start or
# end should not be removed. 
# "xxHxix" -> "Hxi" 
# "abxxxcd"-> "abcd" 
# "xabxxxcdx" _> "xabcdx" 
print("Enter any word")
str = input()

first_letter = str[0]
last_letter = str[-1] 
# I need to get part of the string without first and last letter. 
middle = str[1:-1] 

converted = first_letter + middle.replace("x","")+ last_letter

print(converted)
#      -6 -5 -4 -3 -3 -1 
#      012345   index numbers 
str = "python"
# I need to get part of the string without first and last letter. 
str[1:-1] 
str[1:5]
str[1:len(str)-1]

print(str[1:-1]==str[1:5]==str[1:len(str)-1]) # True 






 


















