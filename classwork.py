# ### Problem 1:
# Create code and define the variable below outside of any function. After you create the list variable write a function called ```stupid_array_tricks``` that takes an array as a parameter, and performs the functions listed below in the instructions.
#
# ```
# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# ```
# a) Print the 2nd and 3rd elements of the person_array using a *range*
#
# b) Print the last 2 elements of the person_array using a *range*
#
# c) Insert the new element ```Chuck``` between the 2nd (```Kevin```) and 3rd (```Erin```) elements
#
# d) Take out the 2nd element (```Kevin```) from the list


# person_array = ["Kenn", "Kevin", "Erin", "Autumn"]
# def stupid_array_tricks(name):
#     print(name[1:3])
#     print(name[2:4])
#     name.insert(2, "chuck")
#     name.pop(1)
#     print(name)


#stupid_array_tricks(person_array)

### Problem 2:
##### We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
# def loop():
#     userInput = input("enter a string ")
#     while userInput != "q":     # if userinput is not equal to "q" loop continues
#         userInput = input("enter another string ")
#
#
# loop()


### Problem 3:
# Create a function that uses the data list below.
# ```
# ['GOOD_DATA',
#  'DECENT_DATA',
#  'BAD_DATA',
#  'DECENT_DATA',
#  'GOOD_DATA'
#  'BAD_DATA',
#  'GOOD_DATA',
#  'DECENT_DATA',
#  'BAD_DATA',
#  'GOOD_DATA']
# ```
#
# Write the code to do the following:
# * Print the length of the original DATA list/array (ex. ```Starting length of data list is 10```)
# * Remove all ```BAD_DATA``` from the DATA list/array
# * Print the length of the final DATA list/array (ex. ```Ending length of data list is 7```)

# def problem3():
#     goodBad = ['GOOD_DATA',
#      'DECENT_DATA',
#      'BAD_DATA',
#      'DECENT_DATA',
#      'GOOD_DATA',
#      'BAD_DATA',
#      'GOOD_DATA',
#      'DECENT_DATA',
#      'BAD_DATA',
#      'GOOD_DATA']
#     print(len(goodBad))
#     goodBad.pop(2)
#     goodBad.pop(4)
#     goodBad.pop(6)
#     print(len(goodBad))
# problem3()
#
# Problem 4
# Use the following list of 5 numbers.
# ```score_list = [21,14,6,8,28,42,21]```
#
#
# Write the code to do the following:
# * Print the sum of the numbers (ex. ```The SUM of the numbers is 140 ```)
# * Print the maximum value from the numbers (ex. ```The MIN value of the numbers is 140 ```)
# * Print the minimum value from the numbers (ex. ```The MIN value of the numbers is 6 ```)

score_list = [21,14,6,8,28,42,21]
add = 0
for x in score_list:
    add = x + add
print(f"The SUM of the numbers is 140 {add}")
print(f"The MIN value of the numbers is {min(score_list)}")
print(f"The MIN value of the numbers {max(score_list)}")
