# DEFAULT_FETCH Gives the default information stored in an employee.
DEFAULT_FETCH = """
    SELECT 
        a.animal_id,
        a.email,
        a.name,
        a.species,
        a.dob,
        a.years_in_circus
    FROM 
        animals a
    WHERE
        a.animal_id = a.animal_id
""" # Last line is default since we need to have at least 1 WHERE statement, even in the default.

# INSERT SQL statement to insert a new row into animal table.
INSERT = """
    INSERT INTO animals VALUES({id}, '{email}', '{name}', '{species}', '{dob}', {years_in_circus})
"""

# queryMap stores the potential specifications a user can make about their search.
queryMap = {
    'id': " AND a.animal_id = {}", # Two % needed to write %
    'email': "AND a.email LIKE '%%{}%%'",
    'name': " AND a.name LIKE '%%{}%%'",
    'species': "AND a.species LIKE '%%{}%%'",
    'sort_by_years': "ORDER BY a.years_in_circus"
}

# Run whenever a user wants to search for a new animal.
def fetch(args):
    query = DEFAULT_FETCH

    if  args['id'] != '': # Search by animal id
        query += queryMap['id'].format(args['id'])
    if  args['email'] != '': # Search by trainer email
        query += queryMap['email'].format(args['email'])
    if  args['name'] != '': # Search by name
        query += queryMap['name'].format(args['name'])
    if  args['species'] != '': # Search by species
        query += queryMap['species'].format(args['species'])
    if 'sort_by_years' in args: # Sort by years in circus
        query += queryMap['sort_by_years']
    return query

# Run whenever a user wants to create a new animal.
def add_animal(args):
    id = args['id'] # ID is a primary key, it must be entered.
    email = args['email'] # email is not null, it must be entered.
    name = args['name'] # name is not null, it must be entered.
    species = "null"
    dob = "null"
    years_in_circus = "null"

    if args['species'] != '':
        species = args['species']
    if args['dob'] != '':
        dob = args['dob']
    if args['years_in_circus'] != '':
        years_in_circus = args['years_in_circus'] 

    add_animal = INSERT.format(id=id, email=email, name=name, species=species, dob=dob, years_in_circus=years_in_circus)
    return add_animal
    