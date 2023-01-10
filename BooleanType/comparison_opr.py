
a = 5
b = 7 

# Let's compare this two value using 
# comparison operators.

print( a > b) # False 
print( a ==b) # False 

# Line below will generate syntax error

print( a < b) # True

# We can give our priorities 
print( (a < b) ==1) # True

#a = 5
#b = 7 
 
print(a != b) # True b is not equal to 7 

c= 7
d=7 
print(c >= d) # True 

print( c <= d) # True 

print(True > False) # True 

print(True != True )
 
print(False ==False) # True 

print(True<= True) # True 

print((True>=True)==(True<=True ))


What is the difference  = and == sign?
 
 = sign is assigment operator in python

 == sign is comparison operator in python 

 == will compare the values wheras = sign will assing 
 values to variables.

------------------------------------------------------------------------------------------------------------

Logical Operators in Python 


And 

To graduate from bootcamp 
your mock interviw score should be more than 
7 and your attendency should be more than %80


Student 1 -> Mock Score - 6
             Attendency - %90     FAIL

Student 2 -> Mock Score - 8
             Attendency - %81    PASS

Student 3 -> Mock Score - 7
             Attendency - %80    FAIL




There is a concert in downtown to enter a field 
the fans should bring their ticket and 
their id.

First Fan - > Only ID 

Second Fan -> ID and Ticket 

Third Fan -> Only ticket



True and True -> True
True and Fals -> Fals
Fals and Fals -> Fals

# and operator will return True only if both side 
# of the and is True .



--------------------------------------------------------------------------------------------------------------------------

OR 


To graduate from bootcamp 
your mock interviw score should be more than 
7 or  your attendency should be more than %80


Student 1 -> Mock Score - 6           PASS
             Attendency - %90

Student 2 -> Mock Score - 8           PASS
             Attendency - %81 

Student 3 -> Mock Score - 7           FAIL 
             Attendency - %80 




True or Fals -> True
Fals or Fals -> Fals
True or True -> True 



-------------------------------------------------------------------------------------------------------------------------

NOT OPERATOR 

It changes the value of the boolen variable 

a = True  

print(not a) # False 

b = False 

print(not b) # True 

print( a not b) # True 




Precedence in Logical operators

and is calculated first then the rest 


 a = 5

 b = 7 

 print( a < b ==1) # False 


In Python when multiple comparison operators are used , python will automatically add 
operator between multiple comparisons .

a < b == 1 

a < b and b== 1
True and False -> False































