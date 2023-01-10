
a,b,c,= 5, 4.2, 3.9 

# Cast a + b to an integer 
# 5 + 4.2 is 9.2  , when I cast 9.2 to an integer is 9
sum = int(a) + int(b)
print(sum)

# Cast b + c to an integer 
# 4.2 + 3.9 is 8.1 when i cast 8.1 to an integer is 8 
sum2 = int(b) + int(c)
print(sum2)
sum2 = int(b+ c)
print(sum2)

# What will be the result of print on the following line?
print(type(sum2))

# Convert data type of sum2 to a float 
sum2 = float(sum2)
print(type(sum2))




