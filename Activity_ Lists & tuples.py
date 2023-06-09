## Task 1: Create lists and use tuples

## Create lists
# You'll work with state names and county names indicated below.
# state_name	county_name
# Arizona	    Maricopa
# California	Alameda
# California	Sacramento
# Kentucky	    Jefferson
# Louisiana	    East Baton Rouge

# In this task, assign two variables:
#     1. `state_names` - a `list` of each state in the `state_name` column in the table above, in order, as strings
#     2. `county_names` - a `list` of each county in the `county_name` column in the table above, in order, as strings

state_names = ["Arizona", "California", "California", "Kentucky", "Louisiana"]
county_names = ["Maricopa", "Alameda", "Sacramento", "Jefferson", "East Baton Rouge"]

#1b: Use a loop to combine the lists into a single list of tuples
# Use state_names and county_names to:
# Create a new list of tuples, where each tuple contains a pair of state name and county name.
# Assign the new list to a variable called state_county_tuples.
# Print the result
# Expected result:

# [OUT] [('Arizona', 'Maricopa'),
#        ('California', 'Alameda'),
#        ('California', 'Sacramento'),
#        ('Kentucky', 'Jefferson'),
#        ('Louisiana', 'East Baton Rouge')]

state_county_tuples = []
for i in range(len(state_names)):
    state_county_tuples.append((state_names[i], county_names[i]))
print(state_county_tuples)

# 1c: Use the zip() function to combine the lists into a single list of tuples
# Python has a built-in function to make the above process much easier. It's called the zip() function. This function accepts any number of iterable objects as arguments. If the arguments are all of equal length, the function returns an iterator object of tuples, where each tuple contains element[i] of each argument.

# You can then either loop over the iterator object or pass it to the list() function to unpack its values.

# Use the zip() function to generate the same output created in Task 1b.

# Use state_names and county_names to:
# Create a new list of tuples, where each tuple contains a pair of state name and county name.
# Assign the new list to a variable called state_county_zipped.
# Check that state_county_zipped is the same as state_county_tuples.

state_county_zipped = list(zip(state_names, county_names))

state_county_zipped == state_county_tuples