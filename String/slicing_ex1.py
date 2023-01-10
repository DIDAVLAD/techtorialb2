#Ask user to enter a string and print a rotated 
# left 2 version where the first 2 charachters 
# of the strig moved to the end .
# 'Hello" -> 'lloHe' 
# 'java'  -> 'vaja' 

print("please enter a word")
word = input()

# Using slicing we got first two letters from the word
first_two_letter = word[0:2] 
# since the ferst number is 0 we will not use like above , instead 
fisrt_two_letters = word[:2]

rest_of_word = word[2:]

rotated = rest_of_word + first_two_letter

print(rotated)















