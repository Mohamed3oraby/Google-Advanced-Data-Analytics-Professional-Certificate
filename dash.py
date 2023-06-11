# For following along with the instructor

# Dictionary Methods 

team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
    ('Sandra', 19, 'center'),
    ('Mari', 18, 'point guard'),
    ('Esme', 18, 'shooting guard'),
    ('Lin', 18, 'power forward'),
    ('Sol', 19, 'small forward'),
    ]

# User Dictionary instead of lists

# Instantiate an empty dictionary
new_team = {}

# Loop over the tuples in the list of players and unpack their values
for name, age, position in team:
    if position in new_team:                    # If position already a key in new_team,
        new_team[position].append((name, age))  # append (name, age) tup to list at that value
    else:
        new_team[position] = [(name, age)]      # If position not a key in new_team,
                                                # create a new key whose value is a list
                                                # containing (name, age) tup
new_team

print(new_team['center'])
