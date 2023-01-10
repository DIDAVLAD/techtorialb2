#Veera wants to lose 10 pounds in 1 month
#There are multiple conditions to lose 10 pounde in a month
# Veera needs to walk 10000 stepts daily OR needs to run at least 4 miles a day
# and Addition to those , Veera needs to eat less than 1500 calories daily. 
# We should create a programe to calculate if Veera can loose weight or not.

daily_calory_taken = 2000
running_distance = 5
walking_steps = 12000 

can_loose = (running_distance>=4 or walking_steps>=10000) and daily_calory_taken<1500
print("Veera can loose weight", can_loose)











