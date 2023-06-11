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

new_team = {}
for name, age, position in team:
    if position in new_team:
        new_team[position].append((name, age))
    else:
        new_team[position] = [(name, age)]

new_team = ['center']