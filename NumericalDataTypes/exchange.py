# Create a python program to give
# most efficient exchange possible using only
# coins
# quarter 25 cents
# nickel 5 cents 
# dime 10 cents 
# penny 1 cents 
# $2.34 excange 
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies 
# $1.89
# 7 quarters 1 dimes 0 nickels 4 pennies 
# Create a program to give a change using least coin possible 
exchange = 1.89
# from the given amount of exchange how many quarter can i give?
# we are using integer divison (line 27 to 34 ), but the results is with decimals . 
# Better solution
# I will convert excange to cents 
total_cents = exchange * 100

count_of_q = total_cents // 25
print(count_of_q)
# I have ti check what is left after i gave the quarters. 
# To find the left over after giving quarters 
left_after_quarter = total_cents % 25 
# I have to find how many dimes I can give it back 
count_of_dimes = left_after_quarter % 10
#I have to find hoe many nickel i can give. 
count_of_nickel = left_after_dimes // 5

count_of_pennies = left_after_dimes % 5


print("For $",exchange,"I will give",count_of_q,"quarters"
, count_of_dimes,"dimes" , count_of_nickel,"nickels",count_of_pennies,
"pennies")





count_of_q = exchange // 0.25 
print(count_of_q)
# I give enough quarters, however how can i complete rest of the 
# exchange 
# I have to check what is left over after i gave the quarters.
# To find the left overs afyter giving quarters 
left_after_quarter = exchange % 0.25 
print(left_after_quarter)

exchange = 0.42 
total_cents = exchange * 100
count_of_q = total_cents // 25 
print(count_of_q)

left_after_quarter = total_cents % 25
count_of_dimes = left_after_quarter // 10
print(count_of_dimes)

left_after_dimes = total_cents % 10
count_of_nickel = left_after_dimes // 5
print(count_of_nickel)

count_of_pennies = left_after_dimes % 5 



print("For $",exchange,"I will give",count_of_q,"quarters" ,
count_of_dimes,"dimes",count_of_nickel, "nickel",count_of_pennies,
"pennies")



