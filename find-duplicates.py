# Find all the duplicates and put them in a separate list. The Duplicate List should not have duplicates of the duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# My Code

new_list = []                                                   # creates an empty list in which we'll put the duplicates
for x, letter in enumerate(some_list):                          # for each letter loop around the list, starting at that letter's postion
  i = x                                                         # define the "index" for While Loop 
  while i < (len(some_list) - 1):                               # since we use "i+1", we cannot exceed len(list) - 1
    if (letter == some_list[i+1]) and (letter not in new_list):  # checks if the letter we are at = the letter to its right, but not letter in the Duplicate List
      new_list.append(letter)                                   # if the condition is True, add it to the new_list
    i += 1                                                      # increment by one to get the While Loop to loop again
print(new_list)                                                 # after it's done looping around, print the resulting list


# Andrei's Code:

# duplicates = []
# for value in some_list:
#   if some_list.count(value) > 1:        # count the number of occurrences and if more than once...
#     if value not in duplicates:         # ... and not already in the "duplicates" List...
#       duplicates.append(value)          # ... then add them to the "duplicates List"
# print(duplicates)